import streamlit as st
import pickle
st.title ("IRIS FLOWER CLASSIFICATION")
SepalLengthCm=st.number_input("Sepal Length",value=0.0,step=0.1)
SepalWidthCm=st.number_input("Sepal Width",value=0.0,step=0.1)
PetalLengthCm=st.number_input("Petal Length",value=0.0,step=0.1)
PetalWidthCm=st.number_input("Petal Width",value=0.0,step=0.1)
if st.button("Submit"):
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    st.success(pickled_model.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])[0])
