pets = []

pet = {
    'type': 'fish',
    'name': 'john',
    'owner': 'guido',
    }
pets.append(pet)

pet = {
    'type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    }
pets.append(pet)

pet = {
    'type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    }
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
