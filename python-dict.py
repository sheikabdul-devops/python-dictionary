#! /usr/bin/python3

import sys
import json

keys = sys.argv[2]
data=json.loads(sys.argv[1])


def get_values(data,keys):

  list = keys.split("/")

  for i in list:
       v = data[i]      
       data = v
  return data

result = get_values(data,keys)
result = json.dumps(result)
print(result)

