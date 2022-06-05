import statistics as st
import pandas as pd
df=pd.read_csv('C:/Users/khada/Downloads/python/c104/SOCR-HeightWeight.csv')
weight=df['Weight(Pounds)'].tolist()
mean=st.mean(weight)
print(mean)
median=st.median(weight)
print(median)
mode=st.mode(weight)
print(mode)