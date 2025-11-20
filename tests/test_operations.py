import geopandas as gpd
from shapely.geometry import Point, box
from src.operations import buffer, overlay, spatial_join

def test_buffer_area_grows():
    g = gpd.GeoDataFrame(geometry=[Point(0, 0)], crs="EPSG:3857")
    b = buffer(g, 100)
    assert b.geometry.area.iloc[0] > 0

def test_overlay_intersection():
    a = gpd.GeoDataFrame(geometry=[box(0, 0, 2, 2)], crs="EPSG:4326")
    b = gpd.GeoDataFrame(geometry=[box(1, 1, 3, 3)], crs="EPSG:4326")
    r = overlay(a, b, "intersection")
    assert len(r) == 1

def test_spatial_join_basic():
    pts = gpd.GeoDataFrame({"id": [1]},
                           geometry=[Point(0.5, 0.5)], crs="EPSG:4326")
    poly = gpd.GeoDataFrame({"name": ["box"]},
                            geometry=[box(0, 0, 1, 1)], crs="EPSG:4326")
    r = spatial_join(pts, poly)
    assert len(r) == 1
    assert r.iloc[0]["name"] == "box"
