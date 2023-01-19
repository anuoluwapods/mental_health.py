import streamlit as st
import pandas as pd
from deta import Deta
import json
import base64
#from PIL import Image
#from streamlit.runtime.runtime import Runtime as Runtime

#image = Image.open('image1.png')

tab1, tab2, tab3 = st.tabs(["Mood Check", "Maniac Signs", "Depression Signs", "Wellness Signs"])

with tab1:
 col1, col2 = st.columns(2)
 col3, col4 = st.columns(2)
 col1.header("My Mental Health App")
 col1.write("tracking my mental health so i can predict my mood with enough data accurately and become better")

#col2.image(image)

 deta = Deta(st.secrets["deta_key"])

 db = deta.Base("mood-check") # Happy, Sad, write
 
 mood = st.radio("How Do You Feel Today",
    ('Happy', 'Sad', 'Let me explain'))
 if mood == 'Happy':
  db.put({"Mood":mood})
  
 if mood == 'Sad':
  db.put({"Mood":mood})
          
 if mood == 'Let me explain':
  st.textinput()
  db.put({"Mood":mood})
          
  
     #with st.form("Submit", clear_on_submit=True):
     #submitted = st.form_submit_button("Submit")
     #if submitted:
        #st.write("Submitted Successfully")
        #db.put({"Emotions":emotions, "Depression":depression, "Anxiety":anxiety, "Maniac":maniac})
