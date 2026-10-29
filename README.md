# Mosaic

Mosaic helps people find real problems worth working on. It looks for ideas from unrelated fields that solve the same underlying problem, and shows the sources and the limits.

Built during the Meta Global AI Developer Hackathon (Indie track). 

## What it uses
- muse-spark-1.3, through the Meta Model API: reads and structures problems and cases, judges matches, argues against them, and runs the agent loop
- facebook/contriever, run locally: finds similar text. An open-weights Meta model, licensed CC BY-NC 4.0 (non-commercial)
- BM25: keyword search