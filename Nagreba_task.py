import numpy as np
import matplotlib.pyplot as plt
import keras
from keras import Sequential
from keras.layers import Dense
from tensorflow import keras

c=np.array([[1,1,1,1],
[1,1,1,0],
[1,1,0,1],
[1,0,1,1],
[0,1,1,1],
[0,0,0,0],
[0,0,0,1],
[1,0,1,0],
[1,0,0,0],
[1,0,1,0]])
f=np.array([1,1,0,0,1,0,0,0,0,0])

model = keras.Sequential()
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))

history = model.fit(c, f, epochs=600, verbose=0)

print(model.summary())

def input_data():
  print("Ввод 1 или 0 !!!")
  a=int(input("Мощное давление в шинах?"))
  b=int(input("Покрышки покрышки в рабочем состоянии?"))
  c=int(input("Достаточно топлива для дальнейшего участия?"))
  d=int(input("Возможна потеря места из-за потраченного времени?"))
  array=[a,b,c,d]
  return array

def answer(array):
  ii=array[0][0]
  if ii>0.5:
    return "\n\nПит стоп не обязателен, не теряй время!"
  elif ii<0.5:
    return "\n\nПит стоп обязателен, иначе будет дисквалификация!"
  else:
    return "\n\nХочу циферки 0 или 1, иначе БАН"

    
reshenie=model.predict([input_data()])
print(answer(reshenie))