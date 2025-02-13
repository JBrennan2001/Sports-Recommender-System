# Import Streamlit
import streamlit as st
st.title('Sport Recommender App')  # Create a Title
st.write('Welcome to my Sport Recommender App on Streamlit!')
st.write('This application will ask you a few questions about yourself.')
st.write('Then using data from real athletes, it will give you the Olympic sport that is most compatible to your choices and attributes.')

# For data usage

import pandas as pd
import numpy as np

# For performance measures
from time import time   # measure time it takes to run a model

# Stuff for modelling (Decision Tree)
from sklearn.tree import DecisionTreeClassifier  # the model itself
from sklearn import tree   # visualising the model
from sklearn.model_selection import train_test_split  # Train-test splitting
#from sklearn.model_selection import GridSearchCV  # For Grid Search

# For my function
import time

# Import the model dataset
model_df = pd.read_csv('Model Data.csv')


# Feature columns
feature_cols = ['height_cm', 'weight_kg', 'age', 'male', 'physical', 'team']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(model_df[feature_cols],  # X
                                                    model_df['discipline'],  # y
                                                    test_size = 0.3, # Define a training %
                                                    random_state = 42)

# Best parameters found using a grid search
model = DecisionTreeClassifier(max_depth = 50, max_features = 6, min_samples_leaf = 2, min_samples_split = 100)
model.fit(X_train,y_train)
#print(f'Score on training set: {model.score(X_train,y_train)}')
#print(f'Score on testing set: {model.score(X_test, y_test)}')


def predictor():
    # Inputs
    height = st.slider('Enter you height in cm: ', 120, 230)
    weight = st.slider('Enter your weight in kg: ', 20, 250)
    age = st.slider('Enter your age in years: ', 10, 75)
    gender = st.selectbox('What is your gender?', ['(Please Select)', 'Male', 'Female'])
  
    st.write('Would you prefer a more physically challenging sport (e.g. Athletics), or a less physical sport that requires a specialised skill (e.g. Shooting)?')
    physical = st.selectbox('Which type?', ['(Please Select)', 'Physical', 'Non-physical'])

    st.write('Would you prefer a team sport or an individual sport?')
    team = st.selectbox('Which type?', ['(Please Select)', 'Team', 'Individual'])

    
    if gender == 'Male':
      genderbool = True
    elif gender == 'Female':
      genderbool = False
    
    if physical == 'Physical':
      physicalbool = True
    elif physical == 'Non-physical':
      physicalbool = False
      
    if team == 'Team':
      teambool = True
    elif team == 'Individual':
      teambool = False
   

    # Model
    if (gender != '(Please Select)') & (physical != '(Please Select)') & (team != '(Please Select)'):
      time.sleep(1)
      st.write('Thank you for answering the questions. Here are the details you entered:')
      time.sleep(.5)
      st.write('Height : ', height, 'cm')
      time.sleep(.5)
      st.write('Weight : ', weight, 'kg')
      time.sleep(.5)
      st.write('Age : ', age)
      time.sleep(.5)
      st.write('Gender : ', gender)
      time.sleep(.5)
      st.write('Preferred Sport Type : ', physical, ' and ', team)
      time.sleep(1)
      
      data = pd.DataFrame({'height_cm' : [height], 'weight_kg' : [weight], 'age' : [age], 'male' : [genderbool],
               'physical' : [physicalbool], 'team' : [teambool]})
      result = model.predict(data)[0]
      st.write('Based on the information that you have entered, the sport we think is most suited to you is:')
      st.subheader(result)


predictor()
