import streamlit as st
from Vorlesung_2 import read_data
from Vorlesung_3 import read_pandas
from Vorlesung_4 import funktions
from PIL import Image
from streamlit_option_menu import option_menu


# read_pandas.print_hallo()
#sidebar erstellen

with st.sidebar:
    selected = option_menu (menu_title= "Menu", options= ["Personen", "EKG", "Power Curve"])


if selected == "Personen":

    # Zwei Spalten erzeugen
    col1, col2 = st.columns(2, gap = "large")

    # Text in der ersten Spalte
    with col1:
        ### !!! NAMEN EINFÜGEN!!!
        list_person_names = read_data.get_person_list()
        # print (list_person_names)


        st.title("# EKG APP")
        st.write("## Versuchsperson auswählen")

        # Session State wird leer angelegt, solange er noch nicht existiert
        if 'current_user' not in st.session_state:
            st.session_state.current_user = 'None'

        # Dieses Mal speichern wir die Auswahl als Session State
        st.session_state.current_user = st.selectbox('Versuchsperson', options = list_person_names, key="sbVersuchsperson")

        # st.write("Der Name ist: ", st.session_state.current_user)
    
    
        # if st.session_state.current_user == "Huber, Julian":
            # st.write ("hier sind daten von Julian Huber ")
        
        # suchstring_ = st.session_state.current_user 



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
        # image = Image.open("../" + st.session_state.picture_path)
        image = Image.open(st.session_state.picture_path)
        st.image(image)

        # Personen Daten
        st.write ("Vorname: " + read_data.find_person_data_by_name(st.session_state.current_user)["firstname"])
        st.write ("Nachname: " + read_data.find_person_data_by_name(st.session_state.current_user)["lastname"])
        st.write ("Geburtsjahr: " + str (read_data.find_person_data_by_name(st.session_state.current_user)["date_of_birth"]))

if selected == "EKG":
    # st.write ("Hier ist die Grafik der EKG Aufzeichnung")
    df = read_pandas.load_activity()
    fig = read_pandas.make_plot_EKG(df)
    st.plotly_chart(fig)


if selected == "Power Curve":
    # st.write ("Hier ist die Grafik der Power Curve")
    df = funktions.load_activity()
    fig = funktions.make_plot_PowerCurve(df)
    st.plotly_chart(fig)

