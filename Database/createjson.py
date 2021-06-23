import json

monkey = {}
monkey['Levels'] = []

for i in range(666):
    monkey['Levels'].append({i+1: (i**2)*4+20})

with open("levels.json", "w") as file:
    json.dump(monkey, file)
