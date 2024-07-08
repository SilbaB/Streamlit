import pandas as pd
import streamlit as st
import plotly.express as px
st.title('Titanic Dataset Analysis')
st.write('This app analyses the titanic dataset using streamlit')
@st.cache_data
def load_data():
    # url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    url='https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
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
gender_survival = data.groupby('Sex')['Survived'].mean().reset_index()
fig_gender_survival = px.bar(gender_survival, x='Sex', y='Survived', title='Survival Rate by Gender')
st.plotly_chart(fig_gender_survival)

Pclass_survival=data.groupby('Pclass')['Survived'].mean().reset_index()
fig_pclass_survival=px.bar(Pclass_survival,x='Pclass',y='Survived',title='Pclass survival rates')
st.plotly_chart(fig_pclass_survival)
#DATE
date=st.date_input("Select a date: ")
st.write(f"Selected date is: {date}")
#TIME
time=st.time_input("Select a time: ")
st.write(f"selected time is {date} {time}")
#Selectbox
options=['option 1','Option 2','option 3']
choice=st.selectbox('choose one option:' ,options)
st.write(f"you choose : {choice}")
#Multiselection
options=['OPT1','opt2','opt3']
selections=st.multiselect('choose multiple options',options)
st.write(f"you choose: {' and '.join(selections)}")
#radio
options=['option 1','Option 2','option 3']
choice=st.radio('choose one option:' ,options)
st.write(f"you choose : {choice}")
options=['option 1','Option 2','option 3']
shoice=st.checkbox('choose one option:' ,options)
st.write(f"you choose : {shoice}")
import time
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.1)
st.write("Before the sleep statement")
time.sleep(5)
st.write("After the sleep statement")

with st.spinner("Please wait..."):
    time.sleep(5)
st.write("Task completed.")

startTime = time.time()
for i in range(0,5):
   st.write(i)
   # making delay for 1 second
   time.sleep(1)
endTime = time.time()
elapsedTime = endTime - startTime
st.write("Elapsed Time = %s" % elapsedTime)