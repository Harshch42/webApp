# -*- coding: utf-8 -*-


import pickle
import requests
from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

st.set_page_config(page_title="CodeZilla",page_icon="trollface",layout="wide")

# loading the saved models

diabetes_model = pickle.load(open('diabetes_prediction.sav', 'rb'))

heart_disease_model = pickle.load(open('Heart_disease_prediction.sav', 'rb'))

liver_model = pickle.load(open('liver_prediction.sav', 'rb'))

#Loading assets


def lottiefile(url):

    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_Doc=lottiefile("https://assets7.lottiefiles.com/packages/lf20_zpjfsp1e.json")
imgDiabetes=Image.open("homeDiabetes1.jpg")
imgHeart=Image.open("homeHeart.png")
imgLiver=Image.open("homeLiver1.jpg")

# for homepage

with st.container():
    leftCol , rightCol = st.columns(2)
    with leftCol: 

        st.subheader("CodeZillas :v:")
        st.write('---')
        st.title("Health Care Service Using Machine Learning and web applications")
        st.write("##")
        st.write(
            """
            This Health Care Service Provider will help you predict diseases like diabetes , 
            Heart disease , Liver disease and the chatbot(Docbot) will help you with some remedies
            for commonly happening bodily causes as well as recommend readily available
            Doctors for the same.

            """
        )
        

    with rightCol:
        st_lottie(lottie_Doc)
          
    
st.write("---")


st.write("##")

# sidebar for navigation
with st.container():
    
    selected = option_menu(
                          menu_title='Disease Prediction',
                          menu_icon='cpu',
                          options=['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Disfunctionality Prediction',
                           'ChatBot',
                           'Select an Option'],
                          icons=['coin','activity','cup-straw','robot','arrow-left-circle-fill'],
                          default_index=4,
                          orientation="horizontal",
                          )
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col1:
        Glucose = st.text_input('Glucose Level')
    
    with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col1:
        Insulin = st.text_input('Insulin Level')
    
    with col1:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col1:
        Age = st.text_input('Age of the Person')
    
    with col2:
        st.image(imgDiabetes) 
        st.write("##")
        st.write("""
                    Diabetes

                    - Make healthy eating and physical activity part of your daily routine. 
                    - Maintain a healthy weight.
                    - Avoid Smoking.
                    - Keep your blood pressure and cholesterol under control
                    - Schedule regular physicals and eye exams
                    - Take care of your teeth
                    - Consider a daily aspirin
                    - If you drink alcohol, do so responsibly
                    - Take stress seriously , Get plenty of sleep
                    
                    """)
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
          warn_diabetic="""
                        There is a high probability that the person has Diabetes , It is Recommended to visit a Specialist Doctor as soon as possible
                            Here is a list of Some Doctors that are available ,
                            1) Dr. Vivek Chaudhari , lower Parel
                            2) Dr Nagraj G Huilgol , Vile Parle
                            3) Dr Nandkishore Kapadia , Andheri
                            4) Dr Yogesh Kulkarni , Andheri

                            For any further queries :-
                            Contact - 878*****97          
                        """
        else:
          diab_diagnosis = 'The person is not diabetic'
          warn_diabetic='To avoid diabetes follow the precautions given'
        
    st.success(diab_diagnosis)
    st.warning(warn_diabetic)



# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.text_input('Age')
        
    with col1:
        Sex = st.text_input('Sex')
        
    with col1:
        Chest_pain_type = st.text_input('Chest Pain types')
        
    with col1:
        BP = st.text_input('Resting Blood Pressure')
        
    with col1:
        Cholesterol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col1:
        FBS_over_120 = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        EKGresults = st.text_input('Resting Electrocardiographic results')
        
    with col1:
        MAX_HR = st.text_input('Maximum Heart Rate achieved')
        
    with col1:
        Exercise_angina = st.text_input('Exercise Induced Angina')
        
    with col1:
        ST_depression = st.text_input('ST depression induced by exercise')
        
    with col1:
        Slope_of_ST = st.text_input('Slope of the peak exercise ST segment')
        
    with col1:
        Number_of_vessels_fluro = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        Thallium = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    with col2:
        st.image(imgHeart)
        st.write("""
                    Heart

                    - Control your blood pressure.
                    - Keep your cholesterol and triglyceride levels under control.
                    - Stay at a healthy weight.
                    - Eat a healthy diet.
                    - Get regular exercise. 
                    - Limit alcohol. 
                    - Don't smoke. 
                    - Manage stress.
                    - Manage diabetes.
                    -  Make sure that you get enough sleep
                                                 
                    """)   
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[Age, Sex, Chest_pain_type, BP, Cholesterol, FBS_over_120, EKGresults,MAX_HR,Exercise_angina,ST_depression,Slope_of_ST,Number_of_vessels_fluro,Thallium]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
       
   
# Liver Prediction Page
if (selected == "Liver Disfunctionality Prediction"):
    
    # page title
    st.title("Liver Disfunctionslity Prediction using ML")
    
    col1, col2= st.columns(2)  
    
    with col1:
        age = st.text_input('Age of the patient')
        
#    with col1:
#        gender = st.text_input('Gender of the patient')
        
    with col1:
        tot_bilirubin = st.text_input('Total Bilirubin')
        
    with col1:
        direct_bilirubin = st.text_input('Direct Bilirubin')
        
    with col1:
        alkphos = st.text_input('Alkaline Phosphotase')
        
    with col1:
        sgpt = st.text_input('Alamine Aminotransferase')
        
    with col1:
        sgot = st.text_input('Aspartate Aminotransferase')
        
    with col1:
        tot_proteins = st.text_input('Total Protiens')
        
    with col1:
        albumin = st.text_input('Albumin')
        
    with col1:
        ag_ratio = st.text_input('Albumin and Globulin Ratio')

    with col2:
        st.image(imgLiver)
        st.write("""
                    Liver 

                    - A healthy lifestyle
                    - A well-balanced diet
                    - Avoiding excess alcohol consumption
                    - Weight management with a regular physical exercise regimen

                    """)

    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Liver Disease Test Result"):
        liver_prediction = liver_model.predict([[age, tot_bilirubin, direct_bilirubin, alkphos, sgpt, sgot, tot_proteins, albumin, ag_ratio]])                          
        
        if (liver_prediction[0] == 1):
          liver_diagnosis = "The person has Liver Disfunctionality"
        else:
          liver_diagnosis = "The person does not have Liver Disfunctionality"
        
    st.success(liver_diagnosis)

if (selected=='ChatBot'):
    col_1,col_2=st.columns(2)
    with col_2:
        components.html(

                        """
                        
                        <script type="text/javascript">
                        (function(d, m) {
                            var kommunicateSettings = {
                                "appId": "2d9631449b3776d1855e65191902bfe81",
                                "popupWidget": true,
                                "automaticChatOpenOnNavigation": true
                            };
                            var s = document.createElement("script");
                            s.type = "text/javascript";
                            s.async = true;
                            s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
                            var h = document.getElementsByTagName("head")[0];
                            h.appendChild(s);
                            window.kommunicate = m;
                            m._globals = kommunicateSettings;
                            })(document, window.kommunicate || {});
                        </script>
                        
                        """,height=600,
                        width=400,
                        )
