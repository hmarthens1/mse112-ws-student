import yaml
import os
import sys
_base = os.path.join(os.path.expanduser('~'), 'mse112-ws-student', 'MasterPi')
lab_file_path = os.path.join(_base, 'lab_config.yaml')
Deviation_file_path = os.path.join(_base, 'Deviation.yaml')

def get_yaml_data(yaml_file):
    file = open(yaml_file, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
    
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    
    return data

def save_yaml_data(data, yaml_file):
    file = open(yaml_file, 'w', encoding='utf-8')
    yaml.dump(data, file)
    file.close()
