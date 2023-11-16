# NCC : non-Coding RNA Classifier
A new AI model trained and tested with fresh updated dataset of small Non-coding RNA (ncRNA or sncRNA) sequences to resolve efficiently the classification of small non-coding RNA.
Biological experimental methods for identifying ncRNA families are not only time-consuming and labor-intensive 
but also expensive, making them impractical for the demands of high-throughput technology.

Performance comparison of several prediction methods
 <table align="center">
  <tr>
    <th>Method/Model</th>
    <th>Accuracy</th>
    <th>Sensitivity</th>
    <th>Precesion</th>
    <th>F-score</th>
    <th>MCC</th>
  </tr>
  <tr>
    <td>RNAcon</td>
    <td>0.3737</td>
    <td>0.3787</td>
    <td>0.4500</td>
    <td>0.3605</td>
    <td>0.3341</td>
  </tr>
  <tr>
    <td>GeaPPLE</td>
    <td>0.6487</td>
    <td>0.6684</td>
    <td>0.7325</td>
    <td>0.7050</td>
    <td>0.6857</td>
  </tr>
  <tr>
    <td>nRC</td>
    <td>0.6960</td>
    <td>0.6889</td>
    <td>0.6878</td>
    <td>0.6878</td>
    <td>0.6627</td>
  </tr>
  <tr>
    <td>ncRFP</td>
    <td>0.7972</td>
    <td>0.7878</td>
    <td>0.7904</td>
    <td>0.7883</td>
    <td>0.7714</td>
  </tr>
  <tr>
    <td>ncDLRES</td>
    <td>0.8430</td>
    <td>0.8344</td>
    <td>0.8419</td>
    <td>0.8407</td>
    <td>0.8335</td>
  </tr>
  <tr>
    <td>ncDENSE</td>
    <td>0.8687</td>
    <td>0.8677</td>
    <td>0.8703</td>
    <td>0.8667</td>
    <td>0.8574</td>
  </tr>
  <tr>
    <td> --> NCC </td>
    <td>0.9844</td>
    <td> 0.9808 </td>
    <td> 0.9830 </td>
    <td> 0.9819 </td>
    <td> 0.9831 </td>
  </tr>
  <tr>
    <td>MncR</td>
    <td> > 97%</td>
    <td> - </td>
    <td> - </td>
    <td> - </td>
    <td> - </td>
  </tr>
</table> 


## The main modules of this Repo 

| Functions                         | Files |
| --------------------------------- | ------------------------------------ |
| Data collection functions         | [rfam_query.py](https://github.com/vassilas/NCC/blob/main/src/rfam_query.py)                  |
| Data Analysis                     | [Analysis.ipynb](https://github.com/vassilas/NCC/blob/main/src/Analysis.ipynb)                |
| Data transformation               | [ncc_DataTransform.py](https://github.com/vassilas/NCC/blob/main/src/ncc_DataTransform.py)    |
| AI Models                         | [ncc_Model.py](https://github.com/vassilas/NCC/blob/main/src/ncc_Model.py)                    |
| Training and testing the model    | [ncc_TrainTest.py](https://github.com/vassilas/NCC/blob/main/src/ncc_TrainTest.py)            |

### Data collection functions
---
To collect datasets from [Rfam](https://rfam.org/) database and assemble the main used dataset you will find methods in [rfam_query.py](https://github.com/vassilas/NCC/blob/main/src/rfam_query.py) file
```python
# Update if you need more or less RNA families to be downloaded form Rfam db
def get_RNA_Families_in_interest() -> []:
    return [
        'Cis-reg; IRES;',
        'Cis-reg; leader;',
        'Cis-reg; riboswitch;',
        'Cis-reg; riboswitch;',
        'Gene; ribozyme;',
        'Gene; rRNA;',
        'Gene; miRNA;',
        'Gene; snRNA; snoRNA; CD-box;',
        'Gene; snRNA; snoRNA; HACA-box;',
        'Gene; snRNA; snoRNA; scaRNA;',
        'Gene; tRNA;',
        'Intron;'
    ]
```
### Data Analysis
If a Jupiter Notebook with some statictic analysis of the dataset that can help finalize the data input of the AI model.
The final dataset has more than 50.000 labeld RNA sequences in fasta format as shown bellow:
```fasta
>IRES
ATACCTTTCTCGGCCTTTTGGCTAAGATCAAGTGTAGTATCTGTTCTTATCAGTTTAATATCTGATACGTGGGCCA ...
>tRNA
GCACCACTCTGGCCTTTTGGCTTAGATCAAGTGTAGTATCTGTTCTTATTAGTTTAACCACTAATATGGTCGCACC ...
>tRNA
ATACCTTTCTCGGCCTTTTGGCTAAGATCAAGTGTAGTATCTGTTTTTATCAGTTTAATATCTGATATGTGGTCCA ...
>riboswitch
ATTACTTCTCAGCCTTTTGGCTAAGATCAAGTGTAATAAATCTCATTGTGCTTTATGCCTAATGTGTGCTTATATT ...
>HACA-box
CCAGCTCTCTTTGCCTTTTGGCTTAGATCAAGTGTAGTATCTGTTCTTTTCAGTTTAATCTCTGAAAGTGTTCTAA ...
>tRNA
ACAGCTGATGCCGCAGCTACACTATGTATTAATCGGATTTTTGAACTTGGAGTACGGTTCTGGAGCTTGCTCCACC ...
```


<div align="center">
    <img src="https://raw.githubusercontent.com/vassilas/NCC/main/doc/images/RNA_Sqg_len_histogram.png" width=60% />
</div>

### Data transformation 
Padding, cutting and encoding the RNA sequences before loading them to AI model. If you and to change the encoding method edit this file.
One-hot encoding is used.
```python
# Ribisome encoding
# --------------------------------------
A_rep_8d = [1, 0, 0, 0, 0, 0, 1, 0]
U_rep_8d = [0, 1, 0, 0, 0, 0, 0, 1]
G_rep_8d = [0, 0, 1, 0, 1, 0, 0, 0]
C_rep_8d = [0, 0, 0, 1, 0, 1, 0, 0]
X_rep_8d = [0, 0, 0, 0, 0, 0, 0, 0]
```

### AI Models 
The keras model used for this task. Consists of an Biderectional RRN in the input and Densenet CNN. 

### Training and testing the model
A jupiter Notepad for training evaluating/tasting the selected model and some metrics along.

<table>
    <tr>
        <td><img src="https://raw.githubusercontent.com/vassilas/NCC/main/doc/images/train_metrics.png" width=100%/></td>
        <td><img src="https://raw.githubusercontent.com/vassilas/NCC/main/doc/images/ConfusionMatrix.png" width=90%/></td>
    </tr>
</table> 


## Requirements
* python
    * [docker](https://github.com/docker/docker-py) - Docker SDK for Python
    * wget
    * [fastaparser](https://fastaparser.readthedocs.io/en/latest/) - A Python FASTA file Parser and Writer

NEED TO UPDATE


## Recources
### Rfam
[Rfam](https://rfam.org/) database is a collection of RNA families, each represented by multiple sequence alignments, consensus secondary structures and covariance models
* [Public Rfam MySQL Database](https://docs.rfam.org/en/latest/database.html#main-tables)
* [Rfam API](https://docs.rfam.org/en/latest/api.html)




