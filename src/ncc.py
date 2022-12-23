
import fram_query
import logging
import config


if __name__ == "__main__":

    config.config_logger()

    # file_id = 12
    # file_name = "RF"+str(file_id).zfill(5)
    file_name = "RF00012"
    fram_query.__Rfam_download_fasta_file(file_name)

