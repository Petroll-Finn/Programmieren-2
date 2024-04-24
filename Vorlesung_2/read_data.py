import json

# Opening JSON file
file = open("data/person_db.json")

# Loading the JSON File in a dictionary
person_data = json.load(file)

# print (type (person_data))
print ('____________________')
eintrag_1 = person_data [0]
print (eintrag_1['lastname'])
print (len(person_data))
# print (type(test))

# for i in :
    # print (i)





# def load_person_data(person_data):
"""A Function that knows where the person database is and returns a dictionary with the persons"""
    
    # return person_data





