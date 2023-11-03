from logging import basicConfig, exception, warning

def log_error(path, msg_error):
    basicConfig(level=warning,
                filename='log_errors.log',
                filemode='a',
                path=path,
                format='%(asctime)s | %(levelname)s | %(message)s',
                datefmt='%d.%m.%Y %I:%M:%S',
                encoding='utf8')

    exception(msg_error)