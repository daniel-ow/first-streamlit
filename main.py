import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Dynamic Pressure Profile')
st.sidebar.title('Inputs')

k = st.sidebar.slider('Perm(md)', min_value=10, max_value=200, value=100)
mu = st.sidebar.slider('Viscosity(cp)', min_value=10, max_value=50, value=15)
q = st.sidebar.slider('Flowrate(STB/Day)', min_value=100, max_value=2000, value=200)

re = st.sidebar.number_input('Outer radius of reservoir (ft)', min_value=100, max_value=10000, value=500)
rw = st.sidebar.number_input('Wellbore radius (ft)', min_value=1, max_value=10, value=1)
pe = st.sidebar.number_input('Pressure at the boundary reservoir (psi)', min_value=100, max_value=10000, value=4000)
b = st.sidebar.number_input('Formation volume factor (bbl/stb)', min_value=1, max_value=2, value=1)
h = st.sidebar.number_input('Net pay thickness of reservoir (ft', min_value=2, max_value=500, value=200)

r = np.linspace(rw, re, 500)
p = pe - (141.2*q*mu*b*(np.log(re/r))/k/h)
y_min = p[np.where (r == rw)]

btn = st.button('Show pressure profile')

if btn:
    plt.style.use('classic')
    plt.figure(figsize=(8,6))
    fig,ax = plt.subplots()
    ax.plot(r,p)
    ax.grid(True)
    ax.axhline(y_min, linewidth = 3, color='red')
    ax.set_xlabel('radius(ft)')
    ax.set_ylabel('Pressure at radius r, (PSI)')
    ax.set_title('Pressure profile')
    ax.set_ylim(0, 5000)
    
    ax.plot(r,p)
    st.pyplot(fig)

