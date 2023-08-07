import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from datetime import time, datetime

st.header('st.write')
st.subheader('LMAO')
st.write('Hello World! :sunglasses:')

st.write('1234')

df = pd.DataFrame({
    "first column" : [1,2,3,4],
    "second column" : [10,20,30,40]
    })

st.write(df)

st.write('Below is a dataframe', df, 'Above is a dataframe')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a','b','c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c'])

st.write(c)            

st.header('Slider : ')

st.subheader('Slider')                            

age = st.slider('How old are you', 0,130,25)
st.write("I'm", age, 'years old')

st.subheader('Range Slider')
range = st.slider('Select a range of values' , 0.00, 100.00, (25.00, 75.00))

st.write('Values : ', range)

ploo = st.slider(
    "Schedule your appointment: ",
    value = (time(11,30), time(12,45)))

st.write("You're scheduled for appointment at", ploo)
    

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 10, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
