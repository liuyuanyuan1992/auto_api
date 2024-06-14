from configparser import ConfigParser


def load_ini(path: str, Api_name: str) -> list:
    # configparser实例化
    text = ConfigParser()

    # 读取ini文件内容
    text.read(path)

    # text.items()返回list，元素为tuple,元组格式为 key,value
    db_tuple = text.items(Api_name)
    return db_tuple