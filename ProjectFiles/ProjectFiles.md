### This folder contains the following:

CMPSC_455_Training.ipynb: 
- Notebook for training the three models.

CMPSC_455_Trained_Demo.ipynb: 
- Notebook showing how to use the models and retireve information.

Company_Data.xls: 
- 1,000 house entries to use for demonstration (Global active power not included due to it being predicted by the linear regression model during demo).

ActiveEnergy_LinearRegression.joblib: 
- Linear regression model used to predict global active power per household.

SVM_typical_to_high.joblib: 
- SVM model used to determine if the houses' global active power is high or typical.

SVM_typical_to_low.joblib: 
- SVM model used to determine if the houses' global active power is low or typical.

___
Dataset provided from the following source: https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption
___
### User must supply a CSV file containing values for the following:

![image](https://github.com/justyden/Forecasting-Energy-Consumption-Machine-Learning/assets/118846876/e25a8c69-ab2d-4336-ab8d-682083896836)

 #### Where variables are defined as the following:

 #### **1.datetime:** 
- DateTime in format dd/mm/yyyy hh : mm : ss
___

 #### **2.global_reactive_power:** 
- household global hour-averaged reactive power(in kilowatt)
___

 #### **3.voltage:** 
- minute-averaged voltage(in volt)
___

 #### **4.global_intensity:** 
- household global hour-averaged current intensity(in ampere)
___

 #### **5.sub_metering_1:** 
- energy sub-metering No. 1 (in watt-hour of active energy). It corresponds to the kitchen, containing mainly a dishwasher, an oven and a microwave (hot plates are not electric but gas powered).
___

 #### **6.sub_metering_2:** 
- energy sub-metering No. 2 (in watt-hour of active energy). It corresponds to the laundry room, containing a washing-machine, a tumble-drier, a refrigerator and a light.
___

 #### **7.sub_metering_3:** 
- energy sub-metering No. 3 (in watt-hour of active energy). It corresponds to an electric water-heater and an air-conditioner.

