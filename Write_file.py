from json import dumps
from logging import getLogger

def write_file(dicts, file_name, file_path):
    logger = getLogger('app.write_file')

    try:
        json_file = dumps(dicts, indent=4, ensure_ascii=False)

        with open(f'{file_path}{file_name}.json', 'w') as f:
            f.write(json_file)

    except Exception as ex:
        logger.error(ex)