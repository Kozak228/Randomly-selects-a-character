from logging import basicConfig, exception

def log_error(path, msg_error):
    basicConfig(filename='log_errors.log', path=path,
                format='%(asctime)s | %(levelname)s | %(message)s',
                datefmt='%d.%m.%Y %I:%M:%S',
                encoding='utf8')

    exception(msg_error)