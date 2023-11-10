# de_duplication (Using Or without using ML- Concepts)
from django.shortcuts import render
from django.http import HttpResponse
# from django.http import JsonResponse, response
from rest_framework.decorators import api_view
# import json

# Create your views here.


#4** Data De_duplicate Feature 
# De-duplication (Using or With-out using Machine Learning)
import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/Sofikul Mullick/Desktop/MDM/employees.csv.")

@api_view(["GET"])

def dupe_remove(n):

    my_df = pd.DataFrame()
    k = []
# print(df)

    m=df.duplicated()
# print(a.head(15))
    b = list(m)
#print(a)
#print(a)
    for i in range(len(b)):
        if b[i]==True:
            s=i
            k.append(s)
    print(k)       
    for i in k: 
        d=df.iloc[i:i+1]
        my_df =pd.concat([d, my_df], ignore_index = False)
    print(my_df)
#--------------------------------- drop duplicate data from database -----------------------
    newdf = df.drop_duplicates()
# print(newdf)
    newdf.to_csv('C:/Users/Sofikul Mullick/desktop/MDM/employees_100.csv')
#print()
#print()
    return HttpResponse('Saved Data as Excel File......')
#newdf.to_excel("C:/Users/Sofikul Mullick/Desktop/MDM/newdf005.xlsx")


# df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)