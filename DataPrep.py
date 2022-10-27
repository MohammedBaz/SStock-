import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from datetime import date

df = pd.read_csv('Tadawul_stcks_23_4.csv')
#for col in df.columns: #This for loop to  print the column names of the dataframe
#    print(col)
#df['name'].unique() # just to print the unique names of the companies  
#print(df.dtypes) # print datatype of each column 
df["date1"] = pd.to_datetime(df["date"]) # convert date from object to datetime and store it in new column named date1 
df =df.sort_values(by='date1') #sort dataframe by the date. 
df['dayOfWeek'] = df['date1'].dt.day_name() # get the dayname of each date and store it in new column named dayOfWeek
df['GMonth']=df.date1.dt.month # add the gregorian month to new column 
df['GDay']=df.date1.dt.day # add the gregorian day to new column 
df['GYear']=df.date1.dt.year # add the gregorian year to new column 
!pip install hijri-converter # to convert to hijri date 
from hijri_converter import Hijri, Gregorian
AMonth=np.zeros(shape=(len(df))) # Just to manage SettingWithCopyWarning error create new array as temporay 
ADay=np.zeros(shape=(len(df)))# Just to manage SettingWithCopyWarning error create new array as temporay 
AYear=np.zeros(shape=(len(df)))# Just to manage SettingWithCopyWarning error create new array as temporay 

for i in range(len(df)):
  temp=Gregorian(int(df.iloc[i]['GYear']),int(df.iloc[i]['GMonth']),int(df.iloc[i]['GDay'])).to_hijri() # Not the best way  
  ADay[i]=temp.day
  AMonth[i]=temp.month
  AYear[i]=temp.year

df['AMonth'] = AMonth.tolist() # append the temporary array to df 
df['ADay'] = ADay.tolist()# append the temporary array to df 
df['AYear'] = AYear.tolist()# append the temporary array to df 
