from db import Session
from models.shelter import Shelter
from models.pet import Pet

def list_shelters():
    session = Session()
    shelters = session.query(Shelter).all()
    for shelter in shelters:
        print(f"{shelter.id}: {shelter.name} - {shelter.location}")
    session.close()

def list_pets():
    session = Session()
    pets = session.query(Pet).all()
    for pet in pets:
        print(f"{pet.id}: {pet.name} ({pet.species}), {pet.age} years old - Shelter: {pet.shelter.name}")
    session.close()

def add_pet():
    session = Session()
    name = input("Pet name: ")
    species = input("Species: ")
    age = int(input("Age: "))
    list_shelters()
    shelter_id = int(input("Enter shelter ID: "))
    new_pet = Pet(name=name, species=species, age=age, shelter_id=shelter_id)
    session.add(new_pet)
    session.commit()
    print("Pet added successfully!")
    session.close()

def update_pet():
    session = Session()
    list_pets()
    pet_id = int(input("Enter the pet ID to update: "))
    pet = session.query(Pet).get(pet_id)
    if pet:
        pet.name = input(f"New name (current: {pet.name}): ") or pet.name
        pet.species = input(f"New species (current: {pet.species}): ") or pet.species
        pet.age = int(input(f"New age (current: {pet.age}): ") or pet.age)
        session.commit()
        print("Pet updated successfully!")
    else:
        print("Pet not found.")
    session.close()

def delete_pet():
    session = Session()
    list_pets()
    pet_id = int(input("Enter the pet ID to delete: "))
    pet = session.query(Pet).get(pet_id)
    if pet:
        session.delete(pet)
        session.commit()
        print("Pet deleted successfully.")
    else:
        print("Pet not found.")
    session.close()

def main():
    while True:
        print("\n--- Pet Adoption System ---")
        print("1. List shelters")
        print("2. List pets")
        print("3. Add a pet")
        print("4. Update a pet")
        print("5. Delete a pet")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            list_shelters()
        elif choice == "2":
            list_pets()
        elif choice == "3":
            add_pet()
        elif choice == "4":
            update_pet()
        elif choice == "5":
            delete_pet()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
