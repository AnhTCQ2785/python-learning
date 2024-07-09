pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")
