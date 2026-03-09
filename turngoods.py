import streamlit as st

def app():
    
    st.tittle("TurnGoods")

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
    if choice=='Login':

        username=st.text_input('Username')
        password = st.text_input('Password', type='Password')

        st. button('login')





    else:

        username=st.text_input('Username')
        password = st.text_input('Password', type='Password')

        username = st.text_input('Enter your username')

        st.button('Create my account')
