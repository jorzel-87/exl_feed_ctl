#!/usr/bin/python3

import yaml
import os
import json

JSON_FILE = open("feed.json","r")

def _convert_file_to_yaml():
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    yaml_file = yaml.dump(json.loads(JSON_FILE.read()),sort_keys=False)
    print(yaml_file)

if __name__ == '__main__':
    _convert_file_to_yaml()
