import sys
import json
# import requests

# result = {
#     'a': sys.argv[1],
#     'b': sys.argv[2],
#     'c':sys.argv[3]
# }
result = {
    'a': sys.argv[1],
    'b': sys.argv[2],
    'c':sys.argv[3],
    'isOk': True,
    'message': 'Image calculate success'
}

json = json.dumps(result)

print(json)

sys.stdout.flush()