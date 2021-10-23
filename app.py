import streamlit as st
import pandas as pd

def isPrime(x): #checks if number is prime
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def isTwin(x): #checks if number is twin prime
    if isPrime(x-2): 
        return True
    else:
        return False

def getNum(x): #returns numbers which are twin prime
    if isPrime(x) and isTwin(x):
        return x
    else: #0 otherwise
        return 0


st.write("""
# Twin Prime Conjecture Visualiser
Graph showing a number of twin primes.
""")

numChoice = st.sidebar.slider('Max Number', 100, 100000, 10) #user selects maximum number for the chart

x= list(range(numChoice)) #every non-negative integer up to chosen number
y = map(getNum, x) #prime number


chart_data = pd.DataFrame( #draws a chart from the values
     y,
     x
     )

st.line_chart(chart_data) #plots chart

st.write("""
Developed by MJM Apps.
""")