import streamlit as st
from read_pandas import load_activity, make_Plot


df = load_activity()
fig = make_Plot(df)
st.plotly_chart(fig)





'''
# Wo startet sie Zeitreihe
# Wo endet sich
# Was ist die Maximale und Minimale Spannung
# Grafik
tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = load_activity()
    fig = make_Plot(df)

    st.plotly_chart(fig)

with tab2:
    st.header("Power-Data")'''



