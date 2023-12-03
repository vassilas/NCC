import numpy as np
import csv
import h5py


# Ribisome encoding
# 
# Encoding method : one-hot coding
# naming : <ribosome>_rep_<num_of_digits>d
# --------------------------------------
A_rep_8d = [1, 0, 0, 0, 0, 0, 1, 0]
U_rep_8d = [0, 1, 0, 0, 0, 0, 0, 1]
G_rep_8d = [0, 0, 1, 0, 1, 0, 0, 0]
C_rep_8d = [0, 0, 0, 1, 0, 1, 0, 0]
X_rep_8d = [0, 0, 0, 0, 0, 0, 0, 0]



# Class label dictionary
# --------------------------------------
class_dict = {
    '5S_rRNA'       : 0,
    '5_8S_rRNA'     : 1,
    'tRNA'          : 2,
    'ribozyme'      : 3,
    'CD-box'        : 4,
    'miRNA'         : 5,
    'Intron_gpI'    : 6,
    'Intron_gpII'   : 7,
    'HACA-box'      : 8,
    'riboswitch'    : 9,
    'IRES'          : 10,
    'leader'        : 11,
    'scaRNA'        : 12
}



# One hot encoding of RNA bases
# --------------------------------------
def RNA_data_encoding(in_file: str):
    RNA_encoded = [] 
    RNA_class = [] 
    for line in open(in_file):
        
        # Non-Coding RNA Enumaration
        # --------------------------------------
        if(line[0] == '>'):
            RNA_class.append(class_dict[line[1:-1]])

        # Sequence Encoding 
        # --------------------------------------
        else:
            seq_List = []
            for i in range(len(line[0: -1])):
                if (i < len(line) - 1):
                    if (line[i] == 'A'):
                        seq_List.append(A_rep_8d)
                    elif (line[i] == 'T' or line[i] == 'U'):
                        seq_List.append(U_rep_8d)
                    elif (line[i] == 'C'):
                        seq_List.append(C_rep_8d)
                    elif (line[i] == 'G'):
                        seq_List.append(G_rep_8d)
                    else:
                        seq_List.append(X_rep_8d)
                else:
                    seq_List.append(X_rep_8d)
            RNA_encoded.append(seq_List)

    return RNA_encoded, RNA_class



# cut or pad with X RNA sequences from input file
# output sequences will have the same lentght
# --------------------------------------
def RNA_Seq_padding_and_cutting(in_file: str, out_file: str, length = 500) -> None:

    output_file = open(out_file,'w')

    for line in open(in_file):

        if(line[0] == '>'):
            output_file.write(line)
        else:
            if(len(line[:-1]) > length):
                # Cutting
                output_file.write(line[:length] + '\n')
            else:
                # Padding
                line = line[:-1] + 'X'*(length - len(line) + 1)
                output_file.write(line + '\n')



# Create CSV Dataset
# --------------------------------------
def Create_CSV_RNA_dataset(in_file: str, out_file: str) -> None:
    csv_file = open(out_file, 'w', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Label','Sequence','Length'])
    label = ''

    for line in open(in_file):
        if(line[0] == '>'):
            label = line[1:-1]
        else:
            sequence = line[:-1]
            csv_writer.writerow([label,sequence,len(sequence)])
            label = ''



if __name__ == '__main__':

    # Create CSV file
    # --------------------------------------
    Create_CSV_RNA_dataset(in_file='../datasets/Finalsets/dataset.fasta', out_file='../datasets/Finalsets/dataset.csv')

    # Sequence Padding and Cutting
    # --------------------------------------
    RNA_Seq_padding_and_cutting(in_file='../datasets/Finalsets/dataset.fasta', out_file='../datasets/Finalsets/dataset_padded_cutted.fasta', length=500)

    # # Sequence One-hot encoding
    # # --------------------------------------
    rna,label = RNA_data_encoding(in_file='../datasets/Finalsets/dataset_padded_cutted.fasta')

    # # Saving dataset as HDF5
    # # --------------------------------------
    rna = np.array(rna)
    label = np.array(label)
    h5_file = h5py.File("../datasets/Finalsets/dataset_padded_cutted.hdf5", 'w') # Save the original data as h5 files.
    h5_file.create_dataset('RNA_Sequence', data=rna)
    h5_file.create_dataset('RNA_Class', data=label)
