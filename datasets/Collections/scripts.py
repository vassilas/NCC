


def read_all_sequences_of_given_class_from_fasta_file(fasta_file_name:str,class_name:str)->list:
    fasta_file = open(fasta_file_name,"r")
    ret = []
    valid_seq = False

    for line in fasta_file:
        if line[:-1] == '>'+class_name:
            valid_seq = True
            continue
        if valid_seq == True:
            valid_seq = False
            ret.append(line[:-1])
    return ret






#

def extend_class_db():
    class_name = "HACA-box"
    out_file_name = "./dataset_003_update_"+ class_name +".fasta"


    updated_seq = []
    

    # READ ALL THE SEQIENCES OF CLASS IN INIT FILE
    train_seq = read_all_sequences_of_given_class_from_fasta_file(fasta_file_name='./dataset_003.fasta',class_name=class_name)
    test_seq = read_all_sequences_of_given_class_from_fasta_file(fasta_file_name='./dataset_002.fasta',class_name=class_name)
    # READ ALL THE SEQIENCES OF CLASS FROM CLASS FILE
    class_seq = read_all_sequences_of_given_class_from_fasta_file(fasta_file_name='../Finalsets/HACA-box.fa',class_name=class_name)
    
    new_seq = list( set(class_seq) - set(train_seq) )
    new_seq = list( set(new_seq) - set(test_seq) )

    count = 0
    for seq in new_seq:
        if len(seq) < 250 and len(seq) > 130:
            updated_seq.append(seq)
            count+=1
        if count >= 300:
            break
    
    out_file = open(out_file_name,"w")
    for seq in updated_seq:
        out_file.write(">"+class_name+'\n')
        out_file.write(seq+'\n')





if __name__ == '__main__':
    extend_class_db()