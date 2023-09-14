import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np



cwd=__file__[0:-12]
datadirectory=cwd + "cleanednau.csv"
naulek=pd.read_csv(datadirectory)
y=naulek.iloc[:,7]
x=naulek.iloc[:,1:7]


X_train,X_test,y_train,y_test =train_test_split(x,y,random_state=6,train_size=0.9)


LR=LinearRegression()
LR.fit(X_train,y_train)


predicted=LR.predict(X_test)
score=LR.score(X_test,y_test)

tested=y_test.tolist()


# for user input values 
relative_humidity=float(input("Relative Humidity :"))
air_temprature=float(input("Air Temperature (C): "))
wind_speed=float(input("Wind Speed (m/s): "))
shortwave_net=float(input("Net Shortwave energy (w/m2): "))
longwave_net=float(input("Net Longwave energy (w/m2): "))
previous_snowdepth=float(input("Previous Snow Depth (cm):"))

# inputdata_array=np.array([relative_humidity,air_temprature,wind_speed,shortwave_net,longwave_net,previous_snowdepth]).reshape((6,1))
# indexes=np.array(["RH.high","Tair.high","u","Net S","Net L","Previous Snow"]).reshape((6,1))
data_dict={
    "RH.high":[relative_humidity],
    "Tair.high":[air_temprature],
    "u":[wind_speed],
    "Net S":[shortwave_net],
    "Net L":[longwave_net],
    "Previous Snow":[previous_snowdepth]
}
input_dataframe=pd.DataFrame(data_dict)


input_predicted=LR.predict(input_dataframe)
print("Snow depth after half an hour wil be: "+ str(input_predicted[0]) +" Cm")

