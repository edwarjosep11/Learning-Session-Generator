import os
import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set page title
st.set_page_config(page_title="OpenAI Chatbot")

# Add text input field to the sidebar
with st.sidebar:
    st.subheader('¿Necesitas ideas para tu sesión?')
    st.write('Aquí puedes preguntar lo que quieras. Ej: Dame 5 ejercicios de sumas y restas para 2do de primaria, ejemplo de texto del día del agua para 5to de primaria')
    user_input = st.sidebar.text_input("En qué te puedo ayudar:")

    # Add button to the sidebar
    if st.sidebar.button("Preguntar"):
            # Call the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.3,
        )

        # Display the response
        bot_response = response.choices[0].text
        st.sidebar.text(bot_response)
