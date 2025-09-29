"""CLI entry point."""
from pathlib import Path
import typer
import geopandas as gpd
from . import operations

app = typer.Typer(help="Spatial analysis toolkit")

@app.command()
def buffer(input: Path, distance: float, out: Path):
    gdf = gpd.read_file(input)
    result = operations.buffer(gdf, distance)
    result.to_file(out)
    typer.echo(f"Wrote {out}")

@app.command("spatial-join")
def spatial_join_cmd(left: Path, right: Path, out: Path,
                     predicate: str = "intersects"):
    l = gpd.read_file(left); r = gpd.read_file(right)
    result = operations.spatial_join(l, r, predicate)
    result.to_file(out)
    typer.echo(f"Wrote {out} ({len(result)} rows)")

if __name__ == "__main__":
    app()
