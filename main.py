import streamlit as st
import datetime
import numpy as np
import matplotlib.pyplot as plt

st.title('活性化関数の比較')

def sigmoid(x):
    return 1 /( 1 + np.exp(-x))

def swish(x):
    return x*sigmoid(x)

def relu(x):
    return x*(x>0.0)

x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
y2 = swish(x)
y3 = relu(x)

fig, ax = plt.subplots()

ax.plot(x, y, label='sigmoid') 
ax.plot(x, y2, label='swish')
ax.plot(x, y3, label="relu")
ax.legend()
st.pyplot(fig)

d = st.date_input("こどもの日：", datetime.date(2021,6,1))
st.write(d)
