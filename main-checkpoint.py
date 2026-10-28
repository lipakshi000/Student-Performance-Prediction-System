import streamlit as st
import pickle
st.title('Student Marks Predictor')
sh=st.number_input("Enter study hours")
btn=st.button("Predict")
if btn:
    if sh<=12:
        model=pickle.load(open("smp.pkl","rb"))
        res=model.predict([[sh]])[0][0].round(2)
        st.markdown(f"Predicted marks={res}")
    else:
        st.markdown("Galt Baat hai ye to.... Itna kon padhta hai")  