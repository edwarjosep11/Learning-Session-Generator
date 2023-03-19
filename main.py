import pandas as pd
import streamlit as st
import openai

openai.api_key = "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"

def generate_learning_plan(grade_level, subject_area, duration, topic):
    # Use ChatGPT to generate the learning plan based on user inputs
    prompt = f"Generate a learning session plan for {grade_level} grade {subject_area} for {duration} minutes on the topic of {topic}."
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5,
    )
    learning_plan = response.choices[0].text
    return learning_plan

# Create the Streamlit user interface
st.title("Generar una nueva Sesión de Aprendizaje")
grade_level = st.selectbox("Seleccione el grado: ", ["1er grado", "2do grado", "3er grado", "4to grado", "5to grado", "6to grado"])
subject_area = st.selectbox("Seleccione el curso: ", ['Comunicación', 'Matemática', 'Personal Social', 'Ciencia y Tecnología', 'Arte', 'Educación Religiosa', 'Educación Física', 'Tutoría'])
duration = st.slider("Seleccione la duración de la sesión (en minutos)", min_value=30, max_value=120, value=60)
topic = st.text_input("Ingrese el tema de la sesión de aprendizaje:")

# Generate the learning plan based on user inputs
if st.button("Generar Sesión de Aprendizaje"):
    learning_plan = generate_learning_plan(grade_level, subject_area, duration, topic)
    st.write(learning_plan)
