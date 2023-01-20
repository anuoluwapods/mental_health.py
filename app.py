import streamlit as st
import pandas as pd
from deta import Deta
import json
import base64
#from PIL import Image
#from streamlit.runtime.runtime import Runtime as Runtime

#image = Image.open('image1.png')

tab1, tab2, tab3 = st.tabs(["Mood Check", "Maniac & Depression Signs", "Wellness Signs"])

with tab1:
 col1, col2 = st.columns(2)
 col3, col4 = st.columns(2)
 col1.header("My Mental Health App")
 col1.write("tracking my mental health so i can predict my mood with enough data accurately and become better")

#col2.image(image)

 deta =  Deta(st.secrets["deta_key"])
 

 db = deta.Base("mood-check") 
 
 mood = st.radio("How Do You Feel Today",
    ('Choose', 'Happy', 'Sad', 'Let me explain'))
 if mood == 'Happy':
  db.put({"Mood":mood})
  
 if mood == 'Sad':
  db.put({"Mood":mood})
          
 if mood == 'Let me explain':
  st.textinput("Explain Your Mood")
  db.put({"Mood":mood})
  
with tab2:
 col1, col2 = st.columns(2)
 col3, col4 = st.columns(2)
 
 col1.header("My Mental Health App")
 col1.write("tracking my mental health so i can predict my mood with enough data accurately and become better")
 
 deta1 = Deta(st.secrets["deta_key1"])
 db1 = deta1.Base("maniac-depression-signs")
 
 with st.form("form", clear_on_submit=True):
    maniac = st.text_input("Explain Your Mood ")
    submitted = st.form_submit_button("Submit")
    if submitted:
     db.put({"Maniac Signs": maniac})


 with tab3:
  col1, col2 = st.columns(2)
  col3, col4 = st.columns(2)
  col1.header("My Mental Health App")
  col1.write("tracking my mental health so i can predict my mood with enough data accurately and become better")

#col2.image(image)

  deta3 =  Deta(st.secrets["deta_key3"])
 

  db3 = deta3.Base("mood-check") 
 
  healthy = st.radio("How Do You Feel Today",
    ('Healthy', 'Sick'))
  if healthy == 'Healthy':
    db.put({"Healthy":healthy})
  
  if healthy == 'Sick':
    db.put({"Healthy":healthy})
          
  
    
