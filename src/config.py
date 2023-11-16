import logging
log = logging.getLogger()

def config_logger():

    # LOGGING CONFIG
    log.setLevel(logging.DEBUG)
    
    # format = "%(asctime)-24s| %(levelname)-8s |\t%(message)s"
    format = "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"

    # LOGS TO FILE
    filelog = logging.FileHandler("../log/ncc_logfile.log")
    filelog.setLevel(logging.DEBUG)
    logformat = logging.Formatter(format,datefmt='%Y-%m-%d %H:%M:%S')
    filelog.setFormatter(logformat)
    log.addHandler(filelog)

    # LOGS TO CONSOLE
    streamlog = logging.StreamHandler()
    streamlog.setLevel(logging.DEBUG)
    streamformat = logging.Formatter(format,datefmt='%Y-%m-%d %H:%M:%S')
    streamlog.setFormatter(streamformat)
    log.addHandler(streamlog)
    
