# -*- coding: utf-8 -*-


import pickle
import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="CodeZilla",page_icon=":trollface:",layout="wide")

# loading the saved models

diabetes_model = pickle.load(open('diabetes_prediction.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

#Loading assets


def lottiefile(url):

    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_Doc=lottiefile("https://assets7.lottiefiles.com/packages/lf20_zpjfsp1e.json")
imgDiabetes=Image.open("images/homeDiabetes1.jpg")
imgHeart=Image.open("images/homeHeart.png")
imgLiver=Image.open("images/homeLiver1.jpg")

# for homepage

with st.container():
    leftCol , rightCol = st.columns(2)
    with leftCol: 

        st.subheader("CodeZillas :v:")
        st.write('---')
        st.title("Disease Prediction using Machine Learning")
        st.write("##")
        st.write(
            """
            Lopem ispum
            -
            
            -

            -

            -

            """
        )
        

    with rightCol:
        st_lottie(lottie_Doc)
    st.markdown("Select Below Images to navigate thourgh diseases")
    
st.write("---")

#Homepage image section
with st.container():
    LeftCol,MidCol,RightCol=st.columns(3)
    with LeftCol:
        st.image(imgDiabetes)
        st.markdown("Diabetes")
    with MidCol:
        st.image(imgHeart)
        st.markdown("Heart Disease")
    with RightCol:
        st.image(imgLiver)
        st.markdown("Liver Disfunctionlity")

st.write("##")

# sidebar for navigation
with st.container():
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Disfunctionality Prediction',
                           'Select an Option'],
                          icons=['activity','heart','person','arrow'],
                          default_index=3,
                          orientation="horizontal",
                          )
                        
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
       
    
## Liver Prediction Page
#if (selected == "Liver Disease"):
#    
#    # page title
#    st.title("Liver Disease Prediction using ML")
#    
#    col1, col2, col3 = st.columns((1,2))  
#    
#    with col1:
#        age = st.text_input('MDVP:Fo(Hz)')
#        
#    with col2:
#        gender = st.text_input('MDVP:Fhi(Hz)')
#        
#    with col1:
#        tot_bilirubin = st.text_input('MDVP:Flo(Hz)')
#        
#    with col2:
#        direct_bilirubin = st.text_input('MDVP:Jitter(%)')
#        
#    with col1:
#        alkphos = st.text_input('MDVP:Jitter(Abs)')
#        
#    with col2:
#        sgpt = st.text_input('MDVP:RAP')
#        
#    with col1:
#        sgot = st.text_input('MDVP:PPQ')
#        
#    with col2:
#        tot_proteins = st.text_input('Jitter:DDP')
#        
#    with col1:
#        albumin = st.text_input('MDVP:Shimmer')
#        
#    with col2:
#        ag_ratio = st.text_input('MDVP:Shimmer(dB)')
#        
#    with col1:
#        is_patient = st.text_input('Shimmer:APQ3')
#    
#    
#    # code for Prediction
#    parkinsons_diagnosis = ''
#    
#    # creating a button for Prediction    
#    if st.button("Liver Disease Test Result"):
#        parkinsons_prediction = parkinsons_model.predict([[age, gender, tot_bilirubin, direct_bilirubin, alkphos, sgpt, sgot, tot_proteins, albumin, ag_ratio, is_patient]])                          
#        
#        if (parkinsons_prediction[0] == 1):
#          parkinsons_diagnosis = "The person has Liver Disfunctionality"
#        else:
#          parkinsons_diagnosis = "The person does not have Liver Disfunctionality"
#        
#    st.success(parkinsons_diagnosis)












