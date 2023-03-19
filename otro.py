import openai

openai.api_key = "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"

while True:
    engine_model_gpt3 = 'text_davinci_003'
    
    prompt = input('Introduzca el tema: ')
    
    if prompt in ['exit', 'salir', 'quit', 'terminar']:
        break
        
    completion = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5,
    )
    
    response = completion.choices[0].text
    
    print(response)
