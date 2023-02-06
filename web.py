import streamlit as st
import requests
from streamlit_lottie import st_lottie

# !pip install spello
from spello.model import SpellCorrectionModel
sp = SpellCorrectionModel(language='en')



def hangman_game():

    # title for page
    st.title('Masked letter prediction')

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    st_lottie(animation_data=load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_tfb3estd.json'),
              quality='high', width=300, )

    # taking discrpition
    masked_word = st.text_input(label='Enter Masked Word: ')
    discrip = st.text_input(label="Enter description: ")


    def predict_word(word):
        sp.load('D:\\trained_model.pkl\\model.pkl')
        return sp.spell_correct(word)


    # two columns for predict and try again
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Predict"):
            predicted = predict_word(masked_word.lower())
            st.text(predicted['spell_corrected_text'])

    with col2:
        st.button("Try again")

if __name__ == '__main__':
    hangman_game()