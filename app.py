import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pickle

with open('model.pickle', 'rb') as m:
    modelo = pickle.load(m)
df = pd.read_csv('wage_data.csv')
st.title('DATOS')

tab1,tab2,tab3 = st.tabs(['TAB 1','TAB 2','TAB 3'])

with tab1:

    frec1 = df['Race'].value_counts().reset_index()
    frec2 = df['Gender'].value_counts().reset_index()
    frec3 = df['Marital status'].value_counts().reset_index()

    fig1 = px.histogram(df,x='Wage (mean wage per hour)',title='WAGE')
    fig2 = px.histogram(df,x='Educ (years)',title='EDUCATION')
    fig3 = px.histogram(df,x='Exper (years)',title='EXPERIENCE')
    fig4 = px.bar(frec1 ,x='Race', y='count',title='RACE')
    fig5 = px.bar(frec2 ,x='Gender',y='count',title='GENDER')
    fig6 = px.bar(frec3 ,x='Marital status',y='count',
    title='MARITAL STATUS')

    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)

with tab2: 

    fig = make_subplots(rows=3,cols=2,
    subplot_titles=('EDUC VS WAGE', 'EXPER VS WAGE', 
    'RACE VS WAGE', 'GENDER VS WAGE', 'MARITAL STATUS VS WAGE'))

    fig.add_trace(go.Scatter(x=df['Educ (years)'], y=df['Wage (mean wage per hour)'], mode='markers', name='EDUC VS WAGE'),row=1,col=1)
    fig.add_trace(go.Scatter(x=df['Exper (years)'], y=df['Wage (mean wage per hour)'], mode='markers', name='EXPER VS WAGE'),row=1,col=2)
    fig.add_trace(go.Box(x=df['Race'], y=df['Wage (mean wage per hour)'], name='RACE VS WAGE'),row=2,col=1)
    fig.add_trace(go.Box(x=df['Gender'], y=df['Wage (mean wage per hour)'], name='GENDER VS WAGE'),row=2,col=2)
    fig.add_trace(go.Box(x=df['Marital status'], y=df['Wage (mean wage per hour)'], name='MARITAL STATUS VS WAGE'),row=3,col=1)

    st.plotly_chart(fig)
    
with tab3:
    educ = st.slider('Years of education',0,25)
    exper = st.slider('Years of Experience',0,50)
    raza = st.selectbox('Race',['white','nonwhite'])
    if raza == 'white':
        raza = 0
    else:
        raza = 1
    sexo = st.selectbox('Gender',['male','female'])
    if sexo == 'male':
        sexo = 0
    else:
        sexo = 1
    estado_civil = st.selectbox('Marital status',['single','married'])
    if estado_civil == 'single':
        estado_civil = 0
    else:
        estado_civil = 1
    if st.button('PREDICCIÓN'):
        pred = modelo.predict(np.array([[educ, exper, raza, sexo, estado_civil]]))
        st.write(pred[0])





