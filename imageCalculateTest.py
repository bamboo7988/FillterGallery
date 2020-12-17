import sys 
import json

result = {
    'sigma': sys.argv[1],
    'phie': sys.argv[2],
    'tau':sys.argv[3]
}
  

json = json.dumps(result)

print(str(json))

sys.stdout.flush()