import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import warnings

print(warnings)
data_complete=pd.read_csv('Forest_fire.csv')
data_head=data_complete.head()
data_tail=data_complete.tail()
a=st.sidebar.radio('navigation',['show database','show visualization','use ML module','make module powerfull'])


y0 = np.array(data_complete['Fire Occurrence']).reshape(-1,1)
x0= np.array(data_complete['Temperature']).reshape(-1,1)
x=data_complete.drop(data_complete.columns[[0,4]],axis=1)
y=data_complete.drop(data_complete.columns[[0,1,2,3]],axis=1)
lr=LinearRegression()
lr.fit(x,y)

if a=='show database':

    if st.checkbox("complete database"):
        st.text("showing complete database")
        data_complete

    elif st.checkbox('show head of database'):
        st.text("showing head of database")
        data_head

    elif st.checkbox('show tail of database'):
        st.text("showing tail if database")
        data_tail



elif a=='show visualization':
    if st.checkbox("graph"):
        st.line_chart(data_complete)

    elif st.checkbox('2'):
        st.image('bb.png')


    elif st.checkbox('3'):
        st.image('dd.jpg')



elif a=='use ML module':
    oxygen1=st.number_input('oxygen')
    temp1=st.number_input('temrature')
    humidity1=st.number_input('humdity')
    model=LinearRegression()
    if st.button('predict'):
        model.fit(x,y)
        op=(model.predict([[oxygen1,temp1,humidity1]]))
        op
        if op >10:
            st.warning('forrest in danger')
        else:
            st.success('forrest in safe')
    r=st.radio('view data',['input','outout'])
    if r=='input':
        x
    elif r=='outout':
        y

    elif st.checkbox('view all inputs'):
        x
    elif st.checkbox('view output on data'):
        y
    else:
        st.spinner('in process')

elif a=='make module powerfull':
    st.text('we are designing it please wait...')
