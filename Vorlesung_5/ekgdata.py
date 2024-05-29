import json
import pandas as pd
import plotly.express as px

# %% Objekt-Welt

# Klasse EKG-Data für Peakfinder, die uns ermöglicht peaks zu finden

class EKGdata:

## Konstruktor der Klasse soll die Daten einlesen
    @staticmethod
    def load_Data():
        file = open("data/person_db.json")
        person_data = json.load(file)
        return person_data

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])


    def make_plot(self):

        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        #return self.fig 

    def load_by_id (self,id_EKG):
        person_data = self.load_Data()
        # print (len(person_data))
        for eintrag_person in range(len(person_data)):
            # print (eintrag_person)
            for eintrag_EKG_tests in person_data[eintrag_person]["ekg_tests"]:
                # print (eintrag_EKG_tests)
                if eintrag_EKG_tests["id"] == id_EKG:
                    # print (eintrag_EKG_tests)
                    return eintrag_EKG_tests
        
    # def find_peaks (self):

        

    
    

if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")

    person_data = json.load(file)
    # print(person_data)

    ekg_dict = person_data[0]["ekg_tests"][0]
    print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    print(ekg.df.head())

    # print (ekg.load_by_id(4))




# %%
