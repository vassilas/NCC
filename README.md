# NCC - non-Coding RNA Classifier

## Requirements
* python
    * [docker](https://github.com/docker/docker-py) - Docker SDK for Python
    * wget
    * [fastaparser](https://fastaparser.readthedocs.io/en/latest/) - A Python FASTA file Parser and Writer

## RUN 
```
mkdir ./datasets/Rfam
mkdir log
pip install -r requirements.txt
cd src/
python ncc.py
```

## Recources
---

### Rfam
[Rfam](https://rfam.org/) database is a collection of RNA families, each represented by multiple sequence alignments, consensus secondary structures and covariance models
* [Public Rfam MySQL Database](https://docs.rfam.org/en/latest/database.html#main-tables)
* [Rfam API](https://docs.rfam.org/en/latest/api.html)

### Knotify
An Efficient Parallel Platform for RNA Pseudoknot Prediction Using Syntactic Pattern Recognition [Article](https://www.mdpi.com/2409-9279/5/1/14), [Github](https://github.com/ntua-dslab/knotify/tree/02-mdpi-2021-r2).



