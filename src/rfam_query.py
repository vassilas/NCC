from dataclasses import dataclass
from os import listdir
import mysql.connector
import wget
import gzip
import shutil
import os
import config
import logging

log = logging.getLogger()

# --------------------------------------------------------------
# RFAM - MYSQL DATABASE
# --------------------------------------------------------------
# 
# Description: The Rfam database is a collection of RNA families, 
# each represented by multiple sequence alignments, consensus 
# secondary structures and covariance models
# 
# Link: https://rfam.org/
# --------------------------------------------------------------
RFAM_MYSQL_DB_HOST = "mysql-rfam-public.ebi.ac.uk"
RFAM_MYSQL_DB_PORT = "4497"
RFAM_MYSQL_DB_USER = "rfamro"
RFAM_MYSQL_DB_NAME = "Rfam"

list_of_tables = []


# CONNECT TO DATABASE
# --------------------------------------------------------------
mydb = mysql.connector.connect(
    host = RFAM_MYSQL_DB_HOST,
    port = RFAM_MYSQL_DB_PORT,
    user = RFAM_MYSQL_DB_USER,
    database = RFAM_MYSQL_DB_NAME
)

mycursor = mydb.cursor(buffered=True)




# LIST OF TABLES
# --------------------------------------------------------------
def __Rfam_list_of_tables():
    mycursor.execute("SHOW TABLES")
    for table in mycursor:
        list_of_tables.append(table[0])

    print(list_of_tables)


# PRINT - DESCRIBE TABLES
# --------------------------------------------------------------
def __Rfam_Describe_Tables():
    for table in list_of_tables:
        print("\nTABLE: "+table)
        print("--------------------------------------------")
        mycursor.execute("DESCRIBE "+ table)
        myresult = mycursor.fetchall()
        for res in myresult:
            print(res)


# TEST QUERY 
# --------------------------------------------------------------
def __Rfam_query_test():
    query = "SELECT DISTINCT type FROM family ORDER BY type"
    print("\nQuery: " + query)
    mycursor.execute(query)
    for family in mycursor:
        print(family)

    query = "SELECT type, COUNT(*) FROM family GROUP BY type"
    print("\nQuery: " + query)
    mycursor.execute(query)
    for family in mycursor:
        print(family)

    query = "SELECT * FROM family WHERE type=\"Gene; tRNA;\""
    print("\nQuery: " + query)
    mycursor.execute(query)
    for family in mycursor:
        print(family)

    query = "SELECT * FROM rfamseq LIMIT 10"
    print("\nQuery: " + query)
    mycursor.execute(query)
    for family in mycursor:
        print(family)



def __Rfam_download_fasta_file(filename: str):
    URL = "http://http.ebi.ac.uk/pub/databases/Rfam/CURRENT/fasta_files/"
    URL += filename + ".fa.gz"

    
    # Downlaod the file from Rfam
    try:
        log.info("wget URL: "+URL)
        response = wget.download(URL, "../datasets/Rfam/"+filename+".fa.gz")
    except:
        log.error("wget download FAILED, check URL and path of downloaded file")
        return
    else:
        print()
        log.info("wget response "+response)
    

    # Unzip the downloaded .gz file
    with gzip.open("../datasets/Rfam/"+filename+".fa.gz", 'rb') as f_in:
        with open("../datasets/Rfam/"+filename+".fa", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    # Delete the .gz file
    os.remove("../datasets/Rfam/"+filename+".fa.gz")


def __Rfam_get_type_by_file_name(filename: str):
    log.info("SEARCH type for {filename}".format(filename=filename))
    try:
        mycursor.execute("SELECT type FROM family WHERE rfam_acc LIKE '{filename}'".format(filename=filename))
        for type in mycursor:
            log.debug(type)
    except:
        log.error("MySQL SELECT error")


def __Rfam_get_all_types()->list:
    type_list = []
    # mycursor.execute("SELECT type , COUNT(type) FROM family GROUP BY type")
    mycursor.execute("SELECT type FROM family GROUP BY type")
    for type in mycursor:
        log.debug(type[0])
        type_list.append(type[0])
    
    return type_list


def __Rfam_count_nSequence_per_type():
    type_list = __Rfam_get_all_types()
    print(type_list)



def __Rfam_select_rfam_acc_query_by_type(type: str):
    
    rfam_acc_list = []

    query = "SELECT rfam_acc FROM family WHERE type=\"" + type + "\""
    log.debug("\tQuery: " + query)
    mycursor.execute(query)
    for rfam_acc in mycursor:
        rfam_acc_list.append(rfam_acc[0])
    
    return rfam_acc_list
        


def __Rfam_get_all_rfam_acc_of_all_RNA_family_types():
    RNA_Family_List = [] # RNA family types list
    rfam_acc_Lists = []  # list of lists of rfam_acc per RNA family type

    query = "SELECT DISTINCT type FROM family ORDER BY type"
    log.debug("Query: " + query)
    mycursor.execute(query)
    for family in mycursor:
        RNA_Family_List.append(family[0])

    for family in RNA_Family_List:
        res = __Rfam_select_rfam_acc_query_by_type(type=family)
        rfam_acc_Lists.append(res)
    
    return RNA_Family_List, rfam_acc_Lists



def __Rfam_get_all_rfam_acc_of__RNA_family_types_of_interest():

    rfam_acc_Lists = []  # list of lists of rfam_acc per RNA family type

    for family in get_RNA_Families_in_interest():
        res = __Rfam_select_rfam_acc_query_by_type(type=family)
        rfam_acc_Lists.append(res)
    
    return get_RNA_Families_in_interest(), rfam_acc_Lists


# Update if you need more or less RNA families to be downloaded form Rfam db
# 
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

def __Rfam_download_all_fasta_files_in_interest():
    RNA_Family_List,rfam_acc_Lists = __Rfam_get_all_rfam_acc_of__RNA_family_types_of_interest()
    
    for list in rfam_acc_Lists:
        for file in list:
            __Rfam_download_fasta_file(filename=file)



def __create_fasta_file_with_class(fasta_files: list[str] ,RNA_class: str) -> int:
    
    num_of_sequences = 0
    output_filename = "../datasets/Rfam/"+RNA_class+".fa"

    output_file = open(output_filename,'w')
    for fasta_filename in fasta_files:
        fasta_file = open("../datasets/Rfam/"+fasta_filename+".fa",'r')
        for line in fasta_file:
            if(line[0] == '>'):
                output_file.write(">"+RNA_class+"\n")
                num_of_sequences += 1
            else:
                output_file.write(line)

    return num_of_sequences
        


def __combine_fasta_files_per_class():
    
    rfam_acc_list = []
    num_of_sequences_per_family = {}

    # For 9 of 13 families the process of querying and grouping is the same 
    # By using only the type of family in Rfam query
    # ------------------------------------------------------------------
    RNA_Families_9 = {
        'IRES'          : 'Cis-reg; IRES;',
        'leader'        : 'Cis-reg; leader;',
        'riboswitch'    : 'Cis-reg; riboswitch;',
        'miRNA'         : 'Gene; miRNA;',
        'ribozyme'      : 'Gene; ribozyme;',
        'CD-box'        : 'Gene; snRNA; snoRNA; CD-box;',
        'HACA-box'      : 'Gene; snRNA; snoRNA; HACA-box;',
        'scaRNA'        : 'Gene; snRNA; snoRNA; scaRNA;',
        'tRNA'          : 'Gene; tRNA;'
        }

    for RNA_Class, Rfam_type in RNA_Families_9.items():
        print("\nCreating Dataset for RNA_Class: "+RNA_Class)
        print("--------------------------------------------------")
        rfam_acc_list.clear()
        query = "SELECT rfam_acc FROM family WHERE type=\""+Rfam_type+"\""
        print("Query: " + query)
        mycursor.execute(query)
        for rfam_acc in mycursor:
            rfam_acc_list.append(rfam_acc[0])
        
        num_of_sequences = __create_fasta_file_with_class(fasta_files=rfam_acc_list, RNA_class=RNA_Class)
        num_of_sequences_per_family[RNA_Class] = num_of_sequences


    # Creating fasta datasets for the rest 4 RNA_Classes
    # By using the type of family and the rfam_id in Rfam query
    # ------------------------------------------------------------------
    RNA_Families_4 = [
        '5S_rRNA',
        '5_8S_rRNA',
        'Intron_gpI',
        'Intron_gpII'
        ]

    for RNA_Class in RNA_Families_4:
        print("\nCreating Dataset for RNA_Class: "+RNA_Class)
        print("--------------------------------------------------")
        rfam_acc_list.clear()
        query = "SELECT rfam_acc FROM family WHERE rfam_id=\""+RNA_Class+"\""
        print("Query: " + query)
        mycursor.execute(query)
        for rfam_acc in mycursor:
            rfam_acc_list.append(rfam_acc[0])

        num_of_sequences = __create_fasta_file_with_class(fasta_files=rfam_acc_list, RNA_class=RNA_Class)
        num_of_sequences_per_family[RNA_Class] = num_of_sequences

    print(num_of_sequences_per_family)




def __delete_all_downloaded_fasta_files():
    dir_path = "../datasets/Rfam/"
    files = listdir(dir_path)
    print(files)
    for file in files:
        if file[:2] == 'RF':
            print(file)
            os.remove(dir_path+file)


def __extending_IRES_from_IRESbase_database():
    rfam_IRES_filename = 'IRES.fa'
    IRESbase_filename = 'All_IRES.fa'
    rfam_IRES_sequences = []
    IRESbase_sequences = []
    IRES_Combined = []

    rfam_file = open('../datasets/Rfam/'+rfam_IRES_filename,'r')
    for line in rfam_file:
        if line[0] != '>' :
            rfam_IRES_sequences.append(line[:-1])
    rfam_file.close()

    IRESfile_file = open('../datasets/IRESbase/'+IRESbase_filename,'r')
    for line in IRESfile_file:
        if line [0] != '>' :
            IRESbase_sequences.append(line[:-1])
    IRESfile_file.close

    IRES_Combined = rfam_IRES_sequences + list(set(IRESbase_sequences) - set(rfam_IRES_sequences))
    rfam_file = open('../datasets/Finalsets/'+rfam_IRES_filename,'w')
    for seq in IRES_Combined:
        rfam_file.write('>IRES\n')
        rfam_file.write(seq+'\n')


    
def __count_seq_per_family():
    RNA_Families_list = [
        'IRES'          , 
        'leader'        ,
        'riboswitch'    ,
        'miRNA'         ,
        'ribozyme'      ,
        'CD-box'        ,
        'HACA-box'      ,
        'scaRNA'        ,
        'tRNA'          ,
        '5S_rRNA'       ,
        '5_8S_rRNA'     ,
        'Intron_gpI'    ,
        'Intron_gpII'
    ]

    RNA_Families_Seq_count = {}

    for RNA_Family in RNA_Families_list:
        file = open('../datasets/Finalsets/'+RNA_Family+'.fa','r')
        count = 0
        for line in file:
            count += 1
        RNA_Families_Seq_count[RNA_Family] = int(count/2)
    
    return RNA_Families_Seq_count
    


if __name__ == '__main__':
    # Configure the logger
    config.config_logger()

    # Download all fasta files in interes from Rfam database
    # Fasta files in interest are the ones that have 
    # small non-coding RNA sequences
    __Rfam_download_all_fasta_files_in_interest()

    # 
    __combine_fasta_files_per_class()

    # Delete all Downloaded fasta files 
    __delete_all_downloaded_fasta_files()


    print(__count_seq_per_family())



    


