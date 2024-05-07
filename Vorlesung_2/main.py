import streamlit as st
import read_data


# list_person_names = read_data.get_person_list()
# print (list_person_names)

person_dict = read_data.load_person_data()
person_names = read_data.get_person_list(person_dict)

st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Dieses Mal speichern wir die Auswahl als Session State
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")

st.write("Der Name ist: ", st.session_state.current_user) 


