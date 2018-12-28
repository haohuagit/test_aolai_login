import os
import yaml

def read_yaml(file_name):
    with open("./data" + os.sep + file_name, "r", encoding="utf-8") as f:
        datas = yaml.load(f)
        return datas

