import json

with open('favorite_number.json') as f:
    number = json.load(f)

print("I know your favorite number! It's " + str(number) + ".")