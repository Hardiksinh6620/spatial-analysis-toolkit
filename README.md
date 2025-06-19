# Spatial Analysis Toolkit

Vector spatial operations: buffer, overlay, spatial join, nearest neighbour,
and network analysis with OSMnx.

## Install
```bash
pip install -r requirements.txt
```

## CLI
```bash
python -m src.cli buffer --input data/points.geojson --distance 500 --out buffered.geojson
python -m src.cli spatial-join --left a.geojson --right b.geojson --out joined.geojson
```

## Provenance

See [HISTORY.md](HISTORY.md) for collaboration and reconstruction details.
