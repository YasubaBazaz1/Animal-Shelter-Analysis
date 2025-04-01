import pandas as pd


animal_data = pd.read_csv('aac_intakes_outcomes.csv')

#print(animal_data.isnull().sum())
animal_data.drop(['outcome_subtype'], axis=1, inplace=True)
#print(animal_data.isnull().sum())

#print(animal_data[animal_data.isnull().any(axis=1)])

animal_data = animal_data.dropna()

#print(animal_data)
#print(animal_data.isnull().sum())
