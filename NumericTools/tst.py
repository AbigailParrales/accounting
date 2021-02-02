import json
num = json.load(open("./numeros.json"))

a = 4000
keys = list(num['NIVELES'].keys())
print(list(keys))
include = []
for key in num['NIVELES']:
    level = num['NIVELES'][key]
    include.append(level)
    if not a > int(key):
        print(level)
        print({key:include})
        break

