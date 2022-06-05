import pandas as pd
import statistics as st
df=pd.read_csv('C:/Users/khada/Downloads/python/c104/SOCR-HeightWeight.csv')
height=df['Height(Inches)'].tolist()
sum=0
for h in height:
    sum=sum+h
mean=sum/len(height)
print(mean)
mean=st.mean(height)
print(mean)