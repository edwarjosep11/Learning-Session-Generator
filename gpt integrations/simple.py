import openai

openai.api_key = "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"

grado = ["1er grado", "2do grado", "3er grado", "4to grado", "5to grado", "6to grado"]
curso = ['Comunicación', 'Matemática', 'Personal Social', 'Ciencia y Tecnología', 'Arte', 'Educación Religiosa', 'Educación Física', 'Tutoría']
grado_input = input('Introduce tu grado (1-6): ')
curso_input = input('Introduce tu curso: ')

if grado_input.isnumeric() and 1 <= int(grado_input) <= 6 and curso_input in curso:
    grado_selected = grado[int(grado_input) - 1]
    tema = input('Introduce el tema: ')

    prompt = f"""Imagina que eres un profesor de educación primaria de {grado_selected} experimentado. 
    Diseñarás una sesión de aprendizaje detallada para el curso de {curso_input}. En la respuesta, deberás detallar los siguientes componentes de la sesión: Propósitos de aprendizaje, Preparación de la actividad, Desarrollo de la estrategia, Estrategia de Evaluación (Rúbrica) y Cierre (Reflexión). 
    En cuanto al propósito de aprendizaje, deberás incluir como subtítulos y explicar: competencias y capacidades que trabajarás, los desempeños esperados, los criterios de evaluación, las evidencias e instrumentos de evaluación que utilizarás para medir el éxito de la sesión. 
    En cuanto a la preparación de la actividad, debes incluir como subtítulos y explicar:  las tareas y actividades que los estudiantes realizarán antes, durante y después de la sesión, y cómo estas se alinean con los objetivos de aprendizaje. Además, brindarás una lista de recursos y materiales que se utilizarán en esta sesión.
    En cuanto al desarrollo de la estrategia, debes incluir como subtítulos y explicar:  cómo motivarás a tus estudiantes, cómo integrarás sus saberes previos, cómo presentarás la situación problemática y cómo desarrollarás el tema. Es importante en esta sección detallar la situación problemática, la cual deberá formularse en forma de pregunta.
    Por último, en cuanto al cierre, deberás describir cómo ayudarás a tus estudiantes a reflexionar sobre lo que han aprendido y cómo fomentarás la metacognición. 
    Como consideraciones finales, incluye las rúbricas de evaluación y tablas donde consideres relevante. Todos los componentes y subcomponentes deben estar escritos y fundamentados detalladamente y debe cumplir con los requisitos. El resultado que me darás debe ser mayor a 2500 palabras."""

    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    print(completion.choices[0].text)
else:
    print("Introduce un grado válido (1-6) y un curso válido.") 
