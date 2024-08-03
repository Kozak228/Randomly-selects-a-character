from logging import getLogger, WARNING, FileHandler, Formatter

from Create_and_remove_forders import proverka_path_dir_icon

def logger_init(name):
    logger = getLogger(name)
    format ='%(asctime)s | %(name)s : %(lineno)s | %(levelname)s | %(message)s'
    logger.setLevel(WARNING)

    fh = FileHandler(filename = f'{proverka_path_dir_icon("log")}log_errors.log', encoding = 'utf-8')
    fh.setFormatter(Formatter(format))
    fh.setLevel(WARNING)

    logger.addHandler(fh)