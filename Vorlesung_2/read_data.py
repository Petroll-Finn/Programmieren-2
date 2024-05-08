import json

# Opening JSON file
# file = open("data/person_db.json")

# Loading the JSON File in a dictionary
# person_data = json.load(file)

'''print (type (person_data))
print ('____________________')
eintrag_1 = person_data [0]
print (eintrag_1['lastname'])
print (len(person_data))
# print (type(test))

list1 = []
list1.append(eintrag_1['lastname']+ "," +  eintrag_1["firstname"])
print (list1)'''

'''def load_person_data():
    """A Function that knows where the person database is and returns a dictionary with the persons"""
    file = open("data/person_db.json")
    person_data = json.load(file)
    return person_data'''

def get_person_list():
    """A Function that takes the persons-dictionary and returns a list auf all person names"""
    file = open("../data/person_db.json")
    person_data = json.load(file)

    list1 = []
    for Eintrag in person_data:
        list1.append(Eintrag['lastname']+ "," +  Eintrag["firstname"])

    return list1



print (get_person_list())


'''# Opening JSON file
file = open("data/person_db.json")
# Loading the JSON File in a dictionary
person_data = json.load(file)

List_Namen = load_person_data(person_data)
print (List_Namen)'''
