from dataclasses import dataclass
import mysql.connector
import wget

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

mycursor = mydb.cursor()




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
    mycursor.execute("SELECT DISTINCT type FROM family ORDER BY type")
    for family in mycursor:
        print(family)

    mycursor.execute("SELECT type, COUNT(*) FROM family GROUP BY type")
    for family in mycursor:
        print(family)

    mycursor.execute("SELECT * FROM family WHERE type=\"Gene; tRNA;\"")
    for family in mycursor:
        print(family)

    mycursor.execute("SELECT * FROM rfamseq LIMIT 10")
    for family in mycursor:
        print(family)



def __Rfam_download_fasta_file(filename: str):
    URL = "http://http.ebi.ac.uk/pub/databases/Rfam/CURRENT/fasta_files/"
    URL += filename + ".fa.gz"
    print(URL)
    response = wget.download(URL, "../datasets/Rfam/"+filename+".fa.gz")




if __name__ == "__main__":
    file_id = 12
    file_name = "RF"+str(file_id).zfill(5)
    __Rfam_download_fasta_file(file_name)
