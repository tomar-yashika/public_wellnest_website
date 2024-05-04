# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:29:30 2023

@author: Yashika Tomar
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
Parkinsons_model = pickle.load(open('Parkinsons_model.sav', 'rb'))
breast_cancer_model = pickle.load(open('breast_cancer_model.sav', 'rb'))

# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart disease Prediction',
                            'Parkinsons Disease Prediction',
                            'Breast Cancer Prediction'],
                           
                           icons=['bandaid', 'activity', 'lightbulb', 'gender-female'],
                           
                           default_index=0)
    
# diabetes prediction page
if(selected == 'Diabetes Prediction'):
    
    #page title
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
    
    
    # code for prediction
    diab_diagnosis = ''
    
    # creation a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
# Heart disease prediction page    
if(selected == 'Heart disease Prediction'):
    
    #page title
    st.title('Heart disease Prediction using ML')
    
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
        





# parkinsons disease prediction page    
if(selected == 'Parkinsons Disease Prediction'):
    
    #page title
    st.title('Parkinsons Disease Prediction using ML')
    
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = Parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    
    
    
    
    
    
    
    
 
# breast cancer prediction page
if(selected == 'Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        radius_mean = st.text_input('Mean radius')
    with col2:
        texture_mean = st.text_input('mean texture')
    with col3:
        perimeter_mean = st.text_input('mean perimeter')
    with col4:
        area_mean = st.text_input('mean area')
    with col5:
        smoothness_mean = st.text_input('mean smoothness')
    with col6:
        compactness_mean = st.text_input('mean compactness')
    with col1:
        concavity_mean = st.text_input('mean concavity')
    with col2:
        concavepoints_mean = st.text_input('concave points mean') 
    with col3:
        symmetry_mean = st.text_input('symmetry mean')    
    with col4:        
        fractal_dimension_mean  = st.text_input('fractal dimension mean')
    with col5:
        radius_se = st.text_input('radius error') 
    with col6:
        texture_se = st.text_input('texture error')  
    with col1:
        perimeter_se = st.text_input('perimeter error')
    with col2:         
        area_se = st.text_input('area error')              
    with col3:
        smoothness_se = st.text_input('smoothness error')      
    with col4:
        compactness_se = st.text_input('compactness error')      
    with col5:
        concavity_se = st.text_input('concavity error')       
    with col6:
        concavepoints_se = st.text_input('concavepoints error')  
    with col1:
        symmetry_se = st.text_input('symmetry error')       
    with col2:
        fractal_dimension_se = st.text_input('fractal dimension error')
    with col3:
        radius_worst = st.text_input('worst radius')            
    with col4:
        texture_worst = st.text_input('worst texture')           
    with col5:
        perimeter_worst = st.text_input('worst perimeter')        
    with col6:
        area_worst = st.text_input('worst area')            
    with col1:
        smoothness_worst = st.text_input('worst smoothness')     
    with col2:
        compactness_worst = st.text_input('worst compactness')      
    with col3:
        concavity_worst = st.text_input('worst concavity')      
    with col4:
        concavepoints_worst = st.text_input('worst concave points')  
    with col5:
        symmetry_worst = st.text_input('worst symmetry')   
    with col6:
        fractal_dimension_worst = st.text_input('worst fractal dimension')
        
        
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breast_cancer_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_prediction = "The person has Breast Cancer"
        else:
          parkinsons_diagnosis = "The person does not have Breast Cancer"
        
    st.success(breast_cancer_diagnosis)
