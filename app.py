

import streamlit as st

if st.button('Show TXT'):
   st.title('First WebPage')
   st.divider()
   st.header('Portfolio')
   st.divider()
   st.subheader('Parvathala Charansai')
   st.divider()
   st.text('Iam charan currently pursuing B.Tech 2nd year')
   st.markdown('CSE - Know Languages:')
   st.caption('C,Java,HTML,DBMS')
   st.latex('A^2+B^2+2AB')
   st.code('import pandas as ps')
   st.code('code writen in python')

if st.button('Show Widgets'):
   st.text_input('Name')
   st.number_input('Age')
   st.date_input('D.O.B')
   st.time_input('Time')
   st.radio('Gender',['Male','Female','Others'])
   st.selectbox('Course',['CSE','ECE','CIVIL','MECH','EEE'])
   st.multiselect('Skills',['C','Java','Python','C++'])
   st.file_uploader('Resume')
if st.button('click'):
   st.sidebar.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
   st.sidebar.slider('Select a range of values',0.0, 100.0, (25.0, 75.0))
   st.sidebar.progress(0.75)

   with st.expander('Expand'):
        st.write('Charansai')
