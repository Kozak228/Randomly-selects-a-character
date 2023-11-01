from json import dumps

def write_file(dicts, file_name, file_path):
    json_file = dumps(dicts, indent=4, ensure_ascii=False)


    with open(f'{file_path}{file_name}.json', 'w') as f:
        f.write(json_file)