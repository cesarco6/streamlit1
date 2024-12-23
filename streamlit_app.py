import streamlit as st

st.title("🎈 Mi nueva app en spanich")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
cantidad = st.slider('Selecciona la cantidad')
st.write(f'la cantidad es: {cantidad}')

for i in range(cantidad):
      st.button(f'{i}')