import csv
import array as arr
import math
import random
import decimal


with open("Untitled-1.txt",newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter= ',')
    data_1 = []
    data_3 = []
    data_4 = []
    data_4_age = []
    data_5=[]
    data_5_heart=[]
    data_6 =[]
   
    for row in rows:
        data_1.append(float(row[0])) #row which represents the ID number
        data_3.append(float(row[1])) #row which represents the actual Oxygen number
        data_4.append(float(row[2])) #row which represents the age
        data_5.append(float(row[3])) #row whcih represents the heart rate
      
        data_2_ID=arr.array('d',data_1)
        oxygen=arr.array('d',data_3)
        data_4_age= arr.array('d',data_4)
        data_5_heart = arr.array('d',data_5)
       
        
    
x=data_2_ID[0] #ID number 1
y=data_2_ID[1] #ID number 2
z=data_2_ID[2] #ID number 3
a=data_2_ID[3] #ID number 4
b=data_2_ID[4] #ID number 5
c=data_2_ID[5] #ID number 6

d= oxygen[0] 
e=oxygen[1]
f=oxygen[2]
g=oxygen[3]
h=oxygen[4]
i=oxygen[5]

j=data_4_age[0]
k=data_4_age[1]
l=data_4_age[2]
m=data_4_age[3]
n=data_4_age[4]
o=data_4_age[5]

p=data_5_heart[0]
q=data_5_heart[1]
r=data_5_heart[2]
s=data_5_heart[3]
t=data_5_heart[4]
u=data_5_heart[5]

#w_0= float(decimal.Decimal(random.randrange(-200,200))/1000)
#print(w_0)
#w_1=float(decimal.Decimal(random.randrange(-200,200))/1000)
#print(w_1)
#ran the 4 lines above once to get an intial weight value for w_0 and w_1
trial =0
w_0 =0.197
w_1=-0.09
w_2=-0.054
#w_0 =-59.50
# w_1 = -0.15
# w_2 =0.60
trial =0
while trial <12:
    element=0
    prediction=[]
    prediction_array=[]

    while element <6:
        prediction= (w_0)+(w_1*data_4_age[element])+(w_2*data_5_heart[element])
    
        prediction_array.append(prediction)
        element +=1
    print('the prediction is '+str(prediction_array))   


    element=0
    error_array=[]
    
    while element <6:
        error=oxygen[element]-(prediction_array[element])
        
        error_array.append(error)
        element +=1
    element=0   
    print('THE ERROR RATE IS ' +str(error_array)) 
    error_sum=sum(error_array)
    
    w_1_error_array=[]
    while element <6:
        w_1_error= error_array[element] * data_4_age[element]
        w_1_error_array.append(w_1_error)
        element +=1
       #this is the error values for w_1 which relates to age
    w_1_error_sum =sum(w_1_error_array)
    element =0
    w_2_error_array=[]
    while element <6:
        w_2_error = error_array[element] * data_5_heart[element]
        w_2_error_array.append(w_2_error)
        element +=1
    
    w_2_error_sum=sum(w_2_error_array)

    learning_rate = 0.000002
    w_0= w_0 + (learning_rate *error_sum)
    
    w_1= w_1 + (learning_rate *w_1_error_sum)
    
    w_2= w_2 + (learning_rate*w_2_error_sum)
   



    element=0
    prediction=[]
    prediction_array=[]

    while element <6:
        prediction= (w_0)+(w_1*data_4_age[element])+(w_2*data_5_heart[element])
    
        prediction_array.append(prediction)
        element +=1
    print('the prediction is ' +str(prediction_array))    
    element=0
    error_array=[]
    
    while element <6:
        error=oxygen[element]-(prediction_array[element])
        
        error_array.append(error)
        element +=1
    element=0    
    trial +=1