#Author C.M.H. Feb 2022 Core Pandas Data Analytics XLSX
import pandas as pd
import matplotlib.pyplot as plt
#Analytics
df = pd.read_excel(r'C:\Users\cowen\Desktop\VSC\Book1.XLSX')
df.head()
x = list(df['Country'])
y = list(df['Population'])
figure = plt.figure(figsize =(10,10))
plt.pie(y, labels = x,autopct='%1.2f%%')
plt.title('Countries by Population')
plt.show() 