from django.shortcuts import render
import pandas as pd
import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer



def home(request):
    return render(request,"home.html")

def result(request):
    
    # Loading the model
    cls = pk.load(open("RF_model.pkl",'rb'))
    
    vec = pk.load(open("vecotrizer.pkl",'rb'))
    txt=request.GET['text']
    
    # Vectorizer
    
    X = vec.transform([txt])
    
    # predicting the output using the model
    ans=cls.predict(X)
    
    print(ans)
    
    if ans == 0:
        ans="Benign"
    elif ans == 1:
        ans="Defacement"
        
    elif ans == 2:
        ans="Malware"
    
    elif ans == 3:
        ans="Phishing"
        
    return render(request,"result.html",{'ans':ans})