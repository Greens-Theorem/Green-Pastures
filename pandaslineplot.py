#Author C.M.H. Feb 2022 Core Pandas Data Analytics XLSX
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Analytics
df = pd.read_excel(r'C:\Users\cowen\Desktop\VSC\MasterTranscript.XLSX')
df.head()
y = list(df['Term'])
x = list(df['GPA'])
plt.plot(y,x)
plt.xlabel('Term')
plt.ylabel('GPA')
plt.title('GPA by Term')
plt.show()