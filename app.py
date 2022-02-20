import streamlit as st
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def lottie(url: str):
    content = load_lottieurl(url)
    st_lottie(content)


st.write('Dear Santa,')
'This year for Christmas I would like a puppy!'
':dog::santa:'
st.balloons()
lottie("https://assets5.lottiefiles.com/packages/lf20_2oW79h.json")