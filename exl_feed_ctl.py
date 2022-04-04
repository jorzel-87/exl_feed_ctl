#!/usr/bin/python3

import json
import sys
import requests


JSON_URL = 'http://3.64.207.71:5555/exl_hands_on_lab/feeds.json'
JSON_DATA = json.loads(requests.get(JSON_URL).text)['feeds']


def display_list():
  [print(item[sys.argv[2]]) for item in JSON_DATA]

def _create_json_file():
  json_object = json.dumps(JSON_DATA, indent=4)
  with open("feed.json", "w") as json_file:
    json_file.write(json_object)

def _update_json_file():
  with open("feed.json", "r") as json_file:
    json_object = json.load(json_file)
  for item in json_object:
    if str(item['id']) == (sys.argv[2]):
      if sys.argv[3] in ['lng', 'lat', 'userId', 'mediatype', 'commentCount']:
        item[sys.argv[3]] = int(sys.argv[4])
      else:
        item[sys.argv[3]] = sys.argv[4]
  with open("feed.json", "w") as json_file:
    json.dump(json_object, json_file, indent=4)

def set_argument():
  _create_json_file()
  _update_json_file()

if __name__ == '__main__':
  if len(sys.argv) == 3 and sys.argv[1] == 'list':
    display_list()
  elif len(sys.argv) == 5 and sys.argv[1] == 'set':
    set_argument()
  else:
    raise Exception("Operation forbidden. Try checking your number of arguments.")