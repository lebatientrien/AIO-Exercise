# Demo để trả lời câu hỏi trắc nghiệm
import streamlit as st

with st.form('my_form'):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('First Name')
    l_name = col2.text_input('Last Name')
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First name:", f_name, " - Last Name:", l_name)
