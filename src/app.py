import streamlit as st
import numpy as np

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})



st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


st.header("Gorillllaa🦍")
st.subheader("Lion🦁")



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])


st.write("                                                                                ")
st.write("                                                                                ")
st.write("                                                                                ")
st.line_chart(chart_data)



st.write("                                                                                ")
st.write("                                                                                ")
st.write("                                                                                ")

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [19.076, 72.8777],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)


st.write("                                                                                ")
st.write("                                                                                ")
st.write("                                                                                ")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.write("                                                                                ")
st.write("                                                                                ")
st.write("                                                                                ")


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)