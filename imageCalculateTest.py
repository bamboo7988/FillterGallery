import sys
import json
# import requests

params = {
    'a': int(sys.argv[1]),
    'b': int(sys.argv[2]),
    'c': int(sys.argv[3]),
}

def variableCalculate(percentage, max, reverse):
    if reverse:
        if percentage > 0:
            return (1-percentage/100)*max
        else:
            return max
    else:
        if percentage > 0:
            return percentage / 100 * max
        else:
            return 1

# test = json.loads(sys.argv)
# print(test)

# sigma1 = int(sys.argv[1])

params['a'] = variableCalculate(params['a'], 20, False)
test = params['a']


result = {
    'a': test,
    'b': int(sys.argv[2]),
    'c': int(sys.argv[3]),
    'isOk': True,
    'message': 'Image calculate success'
}

json = json.dumps(result)
print(json)
# sigma = str(json['a'])
# print(sigma)

sys.stdout.flush()