"""Core spatial operations with CRS validation."""
import geopandas as gpd

def _require_projected(gdf):
    if gdf.crs is None or not gdf.crs.is_projected:
        raise ValueError("A projected CRS is required for distance operations")

def buffer(gdf, distance, resolution=16):
    _require_projected(gdf)
    if distance < 0:
        raise ValueError("distance must be non-negative")
    return gdf.copy().assign(geometry=gdf.geometry.buffer(distance, resolution=resolution))

def overlay(a, b, how="intersection"):
    if a.crs != b.crs: raise ValueError("CRS values must match")
    return gpd.overlay(a, b, how=how)

def spatial_join(left, right, predicate="intersects"):
    if left.crs != right.crs: raise ValueError("CRS values must match")
    return gpd.sjoin(left, right, predicate=predicate, how="inner")

def nearest(left, right):
    _require_projected(left)
    if left.crs != right.crs: raise ValueError("CRS values must match")
    return gpd.sjoin_nearest(left, right, how="left", distance_col="dist")
