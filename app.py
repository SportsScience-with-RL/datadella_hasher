import streamlit as st
import streamlit_authenticator as stauth


st.set_page_config(layout='centered', page_icon='Logo2b.png', page_title='Datadella | Password Hasher')
hashed_pwd = None

_, c = st.columns([.2, .8])
with c:
    st.header(':hash: Hashing Password App')
st.write('')

with st.form('entry form'):
    st.write('Entrez votre mot de passe ci-dessous')
    pwd = st.text_input('')
    st.write('')
    _, c = st.columns([.7, .3])
    with c:
        if st.form_submit_button('Encrypter le mot de passe'):
            hashed_pwd = stauth.Hasher([pwd]).generate()

if hashed_pwd is not None:
    st.caption('Mot de passe encrypté')
    st.success(''.join(i if i!='$' else '\$' for i in hashed_pwd[0]))