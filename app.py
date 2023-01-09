import streamlit as st
import pandas as pd
from deta import Deta
import json
import base64
#from PIL import Image
from streamlit.runtime.runtime import Runtime as Runtime

#image = Image.open('image1.png')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

col1.header("My Mental Health App")

col1.write("tracking my mental health so i can predict my mood with enough data accurately and become better")

#col2.image(image)

deta = Deta(st.secrets["deta_key"])

db = deta.Base("menatal-health")
 
          

with st.form("Submit", clear_on_submit=True):
     date = col3.date_input("Input Date", datetime.date(2023, 1, 1))
     time = col4.time_input('Input Time', datetime.time(8, 01))
     emotions = col3.text_input("How do i feel today?")
     depression = col4.text_input("Expressing how i feel depressed today")
     anxiety = col3.text_input("Expressing how i feel anxious today")
     maniac = col4.text_input("Expressing how i feel excessively happy today")
     submitted = st.form_submit_button("Submit")
     if submitted:
        st.write("Submitted Successfully")
        db.put({"Date":date, "Time":time, "Emotions":emotions, "Depression":depression, "Anxiety":anxiety, "Maniac":maniac})
