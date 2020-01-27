import tensorflow as tf
from tensorflow import keras
import numpy as np
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense,Activation,Dropout
#from tensorflow.keras.optimizers import Adam
#from tensorflow.keras.callbacks import Callback,EarlyStopping
import random
import sys
inFile = sys.argv[1]


input=[]
with open(inFile, 'r') as filehandle:
	for line in filehandle:
		line = line[:-1]
		input.append(line)

def fizzbuzz2(i):
  
  if i % 15 == 0:
    return [0,0,0,1]
  elif i % 3 == 0:
    return [0,1,0,0]
  elif i % 5 == 0:
    return [0,0,1,0]
  else: 
    return [1,0,0,0]
    
def fizzbuzz1(i):
if i % 15 == 0:
    return("fizzbuzz")
elif i % 5 == 0:
    return("buzz")
elif i % 3 == 0:
    return("fizz")
else:
    return(str(i))
    

def binary_encode(i, num_digits):
    return np.array([i >> d & 1 for d in range(num_digits)])

def fizz_buzz_pred(i, pred):
    return [str(i), "fizz", "buzz", "fizzbuzz"][pred.argmax()]

input = np.array(list(map(int, input)))
m=len(input)
f1=open('Software1.txt','w')
f2=open('Software2.txt','w')
model = tf.keras.models.load_model('./model/fizzbuzz_model.h5')
errors=0;
correct=0;
for i in range(m):
    f1.write(fizzbuzz1(input[i]))
    f1.write('\n')
    x = binary_encode(input[i])
    y = model.predict(x.reshape(-1,10))
    f2.write(fizz_buzz_pred(input[i],y))
    f2.write('\n')
    
    
f1.close()
f2.close()
