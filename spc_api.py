import requests
import json


req = requests.post('http://127.0.0.1:8891/predict', json = {})
print(json.loads(req.content))
# {'predictions': 'Lipstick', 'success': True}


req = requests.get('http://127.0.0.1:8891/performance'})
print(json.loads(req.content)["performance"])
# ['classes number: 7 ',
# 'use pretrained: True ',
# 'epochs: 21 ',
# 'batch size: 32 ',
# 'learning rate: 0.001 ',
# 'momentum: 0.9 ',
# 'accuracy: 0.8591549295774648 ']