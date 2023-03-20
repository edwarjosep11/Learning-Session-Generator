import pandas as pd
import streamlit as st
import openai

openai.api_key = "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"

def generate_learning_plan(grade_level, subject_area, topic):
    # Use ChatGPT to generate the learning plan based on user inputs
    
    prompts = [f"Eres un profesor de educación primaria de {grade_level}. Diseñarás una sesión de aprendizaje detallada del curso {subject_area} sobre el tema {topic}. Debes detallar incorporar estos componentes: Propósitos de aprendizaje, Preparación de la actividad, Desarrollo de la estrategia, Estrategia de Evaluación (Rúbrica) y Cierre (Reflexión).",    "En cuanto al propósito de aprendizaje, deberás incluir como subtítulos y explicar: competencias y capacidades que trabajarás, los desempeños esperados, los criterios de evaluación, las evidencias e instrumentos de evaluación que utilizarás para medir el éxito de la sesión.",    "En cuanto a la preparación de la actividad, debes incluir como subtítulos y explicar: las tareas y actividades que los estudiantes realizarán antes, durante y después de la sesión, y cómo estas se alinean con los objetivos de aprendizaje. Además, brindarás una lista de recursos y materiales que se utilizarán en esta sesión.",    "En cuanto al desarrollo de la estrategia, debes incluir como subtítulos y explicar: cómo motivarás a tus estudiantes, cómo integrarás sus saberes previos, cómo presentarás la situación problemática y cómo desarrollarás el tema. Es importante en esta sección detallar la situación problemática, la cual deberá formularse en forma de pregunta.",    "Por último, en cuanto al cierre, deberás describir cómo ayudarás a tus estudiantes a reflexionar sobre lo que han aprendido y cómo fomentarás la metacognición. Como consideraciones finales, incluye las rúbricas de evaluación y tablas donde consideres relevante. Todos los componentes y subcomponentes deben estar escritos y fundamentados detalladamente y debe cumplir con los requisitos. El resultado que me darás debe ser mayor a 2500 palabras."]

    responses = []
    for p in prompts:
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=p, max_tokens=3900, n=1, stop=None, temperature=0.5,
        )
        learning_plan = response.choices[0].text
        responses.append(learning_plan)

    learning_plan = "".join(responses)
    
    return learning_plan
    

# Create the Streamlit user interface
st.title("Generar una Nueva Sesión de Aprendizaje")
grade_level = st.selectbox("Seleccione el grado: ", ["1er grado", "2do grado", "3er grado", "4to grado", "5to grado", "6to grado"])
subject_area = st.selectbox("Seleccione el curso: ", ['Comunicación', 'Matemática', 'Personal Social', 'Ciencia y Tecnología', 'Arte', 'Educación Religiosa', 'Educación Física', 'Tutoría'])
duration = st.slider("Seleccione la duración de la sesión (en minutos)", min_value=30, max_value=120, value=60)
topic = st.text_input("Ingrese el tema de la sesión de aprendizaje:")

# Generate the learning plan based on user inputs
if st.button("Generar Sesión de Aprendizaje"):
    progress_bar = st.progress(0)
    learning_plan = generate_learning_plan(grade_level, subject_area, topic)
    progress_bar.progress(50)
    st.write(learning_plan)
    progress_bar.progress(100)