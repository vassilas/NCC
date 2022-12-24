
import rfam_query
import config

import logging
log = logging.getLogger()

if __name__ == "__main__":

    # Configure the logger
    config.config_logger()

    
    log.info("START NCC")
    
    
    # Download RF00012 from Rfam
    file_name = "RF00012" # "RF"+str(12).zfill(5)
    rfam_query.__Rfam_download_fasta_file(file_name)

    # Show all types
    rfam_query.__Rfam_get_all_types()

    rfam_query.__Rfam_get_type_by_file_name(file_name)
    
    log.info("END NCC")
