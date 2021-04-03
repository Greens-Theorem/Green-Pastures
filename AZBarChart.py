#@author Cowen M. Hames
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel("Arizona Spreadsheet.xlsx")
sns.barplot(data = df, x = "Med Age", y = "County")
plt.show()