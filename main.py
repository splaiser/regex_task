import re
from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_contacts_list = []

for people in contacts_list:
    update_people = []
    name_pattern = r"[\w]+"
    result1 = re.findall(name_pattern, people[0])
    if len(result1) == 3:
        update_people.append(result1[0])
        update_people.append(result1[1])
        update_people.append(result1[2])
    elif len(result1) == 2:
        update_people.append(result1[0])
        update_people.append(result1[1])
    elif len(result1) == 1:
        update_people.append(result1[0])
    result2 = re.findall(name_pattern, people[1])
    if len(result2) == 2:
        update_people.append(result2[0])
        update_people.append(result2[1])
    elif len(result2) == 1:
        update_people.append(result2[0])
    if len(result1) != 3 and len(result1) != 3 and len(result2) != 2:
        update_people.append(people[2])

    update_people.append(people[3])
    update_people.append(people[4])
    phone_pattern = r"(8|\+7)( )?\(?(\d\d\d)\)?( )?(-)?(\d\d\d)?(-)?(\d\d)?(-)?(\d+)?( )?"
    people[5] = re.sub(phone_pattern, r"+7(\3)\6-\8-\10", people[5])
    people[5] = re.sub(r"\(?(доб. )(\d+)\)?", r" доб.\2", people[5])
    update_people.append(people[5])
    update_people.append(people[6])

    new_contacts_list.append(update_people)
print("complete")

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
