import pandas as pd
import streamlit as st
import plotly.express as px
st.title('Titanic dataset Analysis')
st.write('This app analyses the titanic dataset')
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    data = pd.read_csv(url)
    data['Age'].fillna(data['Age'].median(), inplace=True)
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
    data.drop('Cabin', axis=1, inplace=True)
    data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
    data['IsAlone'] = data['FamilySize'].apply(lambda x: 1 if x == 1 else 0)
    return data

data = load_data()

if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)

