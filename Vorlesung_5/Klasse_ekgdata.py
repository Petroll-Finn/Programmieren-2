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
    
    @staticmethod
    def load_by_id (id_EKG):
        person_data = EKGdata.load_Data()
        # print (len(person_data))
        for eintrag_person in range(len(person_data)):
            # print (eintrag_person)
            for eintrag_EKG_tests in person_data[eintrag_person]["ekg_tests"]:
                # print (eintrag_EKG_tests)
                if eintrag_EKG_tests["id"] == id_EKG:
                    # print (eintrag_EKG_tests)
                    return eintrag_EKG_tests


    @staticmethod
    def find_peaks(id_EKG, respacing_factor=5):
        # series, threshold, 
        # A function to find the peaks in a series
        # Args:
            # - series (pd.Series): The series to find the peaks in
            # - threshold (float): The threshold for the peaks
            # - respacing_factor (int): The factor to respace the series
        # Returns:
            # - peaks (list): A list of the indices of the peaks
    
        # Respace the series
        
        dict_Person = EKGdata.load_by_id (id_EKG)
        
        
    
        series = series.iloc[::respacing_factor]
        
        # Filter the series
        series = series[series>threshold]


        peaks = []
        last = 0
        current = 0
        next = 0

        for index, row in series.items():
            last = current
            current = next
            next = row

            if last < current and current > next and current > threshold:
                peaks.append(index-respacing_factor)

        return peaks

    def __init__(self, ekg_dict):
        #pass
        self.id = ekg_dict["id"]
        self.date = ekg_dict["date"]
        self.data = ekg_dict["result_link"]
        self.df = pd.read_csv(self.data, sep='\t', header=None, names=['Messwerte in mV','Zeit in ms',])


    def make_plot(self):
        # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
        self.fig = px.line(self.df.head(2000), x="Zeit in ms", y="Messwerte in mV")
        return self.fig 

    
        


if __name__ == "__main__":
    print("This is a module with some functions to read the EKG data")
    file = open("data/person_db.json")

    person_data = json.load(file)
    # print(person_data)
    
    
    ekg_dict = person_data[0]["ekg_tests"][0]
    # print(ekg_dict)
    ekg = EKGdata(ekg_dict)
    # print (ekg)
    # print(ekg.df.head())
    # EKGdata.find_peaks(1)

    print (EKGdata.load_by_id(4))




# %%
