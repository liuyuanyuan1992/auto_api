
import yaml

def load_yaml(path):
    file = open(path, 'r', encoding='utf-8')
    # Loader=yaml.FullLoader，这个是默认的载入方式，载入全部YAML
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data
