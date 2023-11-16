# NCC - non-Coding RNA Classifier
Anew NN AI model trained and tested with fresh updated dataset of Non-coding RNA (or ncRNA) sequences to resolve efficiently the classification of small non-coding RNA.
Biological experimental methods for identifying ncRNA families are not only time-consuming and labor-intensive but also expensive, making
them impractical for the demands of high-throughput technology.




## The main modules of this Repo 
| Functions                         | Files |
| --------------------------------- | ---- |
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




