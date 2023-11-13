

file_train = './dataset_nRC_test.fasta'
file_train_out = './dataset_nRC_test_oneLine.fasta'


# Convert dataset
# Multiline RNA sequences to One line sequences
# -------------------------------------------------------------
def nRC_datasets_convert_to_one_line_sequence():
    
    file_out = open(file_train_out,'w')
    for line in open(file_train):
        if line[0] == '>':
            file_out.write('\n'+line)
        else:
            file_out.write(line[:-1])
# -------------------------------------------------------------







# SELECT THE SCRIPT TO EXECUTE
# -------------------------------------------------------------
if __name__ == '__main__':
    nRC_datasets_convert_to_one_line_sequence()