"""App main"""

from src.get_person_data import get_name_and_age

if __name__ == "__main__":
    try:
        person = get_name_and_age(112)
        print(person)
    except KeyError:
        print("Not a good user ID")

