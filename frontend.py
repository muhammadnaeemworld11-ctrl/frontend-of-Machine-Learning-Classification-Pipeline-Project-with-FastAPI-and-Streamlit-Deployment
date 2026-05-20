import streamlit as st 
import requests


st.title("ML model with streamlit")

st.write("this is your health report of diabete")

# inputs felid 

age = st.number_input("how much age")

workclass = st.number_input("enter your workclass")

fnlwgt = st.number_input("fnlwgt")

education = st.text_input("enter your education level")

educational_num = st.number_input("enter your educational number")

marital_status = st.text_input("enter your marital status")

occupation = st.text_input("enter your occupation")

relationship = st.text_input("enter your relationship")

race = st.text_input("enter your race")

gender = st.text_input("enter your gender")

capital_gain = st.number_input("enter your capital gain")

capital_loss = st.number_input("enter your capital loss")

hours_per_week = st.number_input("enter your hours per week")

native_country = st.text_input("enter your native country")


# prediction button 

if st.button("prediction"):
    # API URL
    
    
    data = {
            
            "age": age,
            "workclass": workclass,
            "fnlwgt": fnlwgt,
            "education": education,
            "educational-num": educational_num,   
            "marital-status": marital_status,     
            "occupation": occupation,             
            "relationship": relationship,
            "race": race,
            "gender": gender,
            "capital-gain": capital_gain,         
            "capital-loss": capital_loss,         
            "hours-per-week": hours_per_week,     
            "native-country": native_country
        }
    
    
    # API request generate
    
    resp = requests.post("https://muhammad-naeem-adult-income-fastapi.hf.space/pred", params=data)
    
    
    result = resp.json()
    
    if result["prediction"]==1:
        st.warning("you have diabetes")
    else:
        st.success("you don't have diabetes")




     