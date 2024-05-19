import streamlit as st
import read_data
from PIL import Image


# Zwei Spalten erzeugen
col1, col2 = st.columns(2, gap = "large")

# Text in der ersten Spalte
with col1:
    ### !!! NAMEN EINFÜGEN!!!
    list_person_names = read_data.get_person_list()
    # print (list_person_names)

    # person_dict = read_data.load_person_data()
    # person_names = read_data.get_person_list(person_dict)

    st.title("# EKG APP")
    st.write("## Versuchsperson auswählen")

    # Session State wird leer angelegt, solange er noch nicht existiert
    if 'current_user' not in st.session_state:
        st.session_state.current_user = 'None'

    # Dieses Mal speichern wir die Auswahl als Session State
    st.session_state.current_user = st.selectbox(
        'Versuchsperson',
        options = list_person_names, key="sbVersuchsperson")

    # st.write("Der Name ist: ", st.session_state.current_user) 




# Bild in der zweiten Spalte
with col2:
    ### !!! BILD EINFÜGEN!!!

    # Anlegen des Session State. Bild, wenn es kein Bild gibt
    if 'picture_path' not in st.session_state:
        st.session_state.picture_path = 'data/pictures/none.jpg'

    # Suche den Pfad zum Bild, aber nur wenn der Name bekannt ist
    if st.session_state.current_user in list_person_names:
        st.session_state.picture_path = read_data.find_person_data_by_name(st.session_state.current_user)["picture_path"]

    # Öffne das Bild und Zeige es an
    image = Image.open("../" + st.session_state.picture_path)
    st.image(image)

    st.write ("Vorname: " + read_data.find_person_data_by_name(st.session_state.current_user)["firstname"])
    st.write ("Nachname: " + read_data.find_person_data_by_name(st.session_state.current_user)["lastname"])
    st.write ("Geburtsjahr: " + str (read_data.find_person_data_by_name(st.session_state.current_user)["date_of_birth"]))


