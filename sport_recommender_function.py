# Import Streamlit
import streamlit as st
st.title('Sport Recommender App')  # Create a Title
st.write('Welcome to my Sport Recommender App on Streamlit!')


# For data usage

import pandas as pd
import numpy as np

# For performance measures
from time import time   # measure time it takes to run a model

# Stuff for modelling (Decision Tree)
-m pip install scikit-learn
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
    # Introduction
    input('Welcome to the Olympic sport recommender!')
    print('')
    print('This application will ask you a few questions about yourself.')
    print('Then using data from real athletes, it will give you the Olympic sport that is most compatible to your choices and attributes.')
    print('')
    input('Press Enter to start.')

    x=0
    while x==0:
        try:
            height = float(input('Enter your height in cm: '))
            if (height >= 120) & (height <= 230):
                x=1
            else:
                print('Unfortunately the height you entered is out of range (120cm - 230cm). Please try again.')
        except:
            print('You did not enter a valid height. Please try again. ')
            continue
    print('')
    while x==1:
        try:
            weight = float(input('Enter your weight in kg: '))
            if (weight >=20) & (weight <= 250):
                x=2
            else:
                print('Unfortunately the weight you entered is out of range (20kg - 250kg). Please try again.')
        except:
            print('You did not enter a valid weight. Please try again. ')
            continue
    print('')
    while x==2:
        try:
            age = float(input('Enter your age in years: '))
            if (age >= 10) & (age <= 75):
                x=3
            else:
                print('Unfortunately the age you entered is out of range (10 - 75). Please try again.')
        except:
            print('You did not enter a valid age. Please try again. ')
            continue
    print('')
    while x==3:
        gender = input('Are you male or female? (Enter M or F): ').lower()
        if gender == 'm':
            x=4
        elif gender == 'f':
            x=4
        else:
            print('You did not enter either M or F. Please try again.')
            
    print('')
    print('Would you prefer a more physically challenging sport (e.g. Athletics), or a less physical sport that requires a specialised skill (e.g. Shooting)?')
    while x==4:
        physical = input('Enter P if you would prefer a physical sport. Enter N if not: ').lower()
        if physical == 'p':
            x=5
        elif physical == 'n':
            x=5
        else:
            print('You did not enter either P or N. Please try again.')

    while x==5:
        team = input('Would you prefer a team sport or an individual sport? Enter T for team. Enter I for individual: ').lower()
        if team == 't':
            x=6
        elif team == 'i':
            x=6
        else:
            print('You did not enter either T or I. Please try again.')
    print('\n')
    time.sleep(1)
    print('Thank you for answering the questions. Here are the details you entered:')
    print('')
    time.sleep(.5)
    print(f"Height : {height}cm")
    time.sleep(.5)
    print(f"Weight : {weight}kg")
    time.sleep(.5)
    print(f"Age : {age}")
    time.sleep(.5)
    if gender == 'm':
        print(f"Gender : Male")
        gender = True
    else:
        print(f"Gender : Female")
        gender = False
    time.sleep(.5)
    if physical == 'p':
        physical = True
        if team == 't':
            print(f"Preferred Sport Type : Physical and Team")
            team = True
        else:
            print(f"Preferred Sport Type : Physical and Individual")
            team = False
    else:
        physical = False
        if team == 't':
            print(f"Preferred Sport Type : Non-physical and Team")
            team = True
        else:
            print(f"Preferred Sport Type : Non-physical and Individual")
            team = False
    time.sleep(1)
    print('\n')
    input('Press Enter to view your results')
    
    # Model
    data = pd.DataFrame({'height_cm' : [height], 'weight_kg' : [weight], 'age' : [age], 'male' : [gender],
               'physical' : [physical], 'team' : [team]})
    

    result = model.predict(data)[0]
    return f"Based on the information that you have entered, the sport we think is most suited to you is:   {result}"


predictor()
