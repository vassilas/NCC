import logging


def config_logger():

    # LOGGING CONFIG
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    
    # LOGS TO FILE
    filelog = logging.FileHandler("ncc_logfile.log")
    filelog.setLevel(logging.DEBUG)
    logformat = logging.Formatter("[%(asctime)s]\t[%(levelname)s]:\t%(message)s")
    filelog.setFormatter(logformat)
    log.addHandler(filelog)

    # LOGS TO CONSOLE
    streamlog = logging.StreamHandler()
    streamlog.setLevel(logging.DEBUG)
    streamformat = logging.Formatter("[%(asctime)s]\t[%(levelname)s]:\t%(message)s")
    streamlog.setFormatter(streamformat)
    log.addHandler(streamlog)