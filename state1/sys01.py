import sys
import json

a = sys.argv[0]
print('sys.argv[0]', a)

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
jsonstr = json.dumps(data)
print('jsonstr : ' , jsonstr)

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)
print('python object : ', text)
