import json

with open('gui-config.json') as f:
    data=json.load(f)
    print(data)

# with open('gui-config2.json','w') as f:
#     json.dump(data,f,indent=2)
print(data['configs'])