from src.mcqGen.utils import read_file
import streamlit as st
st.title("this is steamlit app deployed")
with st.form("user_inputs"):
    file=st.file_uploader("upload file")
    submit=st.form_submit_button("show data")
    
    if submit and file is not None:
        st.spinner("loading ....")
        st.write("file opened")
    
        try:
            text=read_file(file)
            st.write(text)
        except Exception as e:
            st.error("file not support")
    else:
        st.write("file open error")    
