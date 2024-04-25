import openia

def get_preco_celular(marca, modelo, ano):
    prompt = '''
            Me mostre o preço de mercado para o celular da marca {} do modelo {} do ano {} utilizando o modelo float em 5 casas decimais.

            '''
    openia.api_key = "sk-proj-Nh0ZJj6BWAvGKbG7Uiq8T3BlbkFJ5T8NJyCcT4WgfGgQ2ClQ"
    prompt = prompt.format(marca, modelo, ano)
    response = openia.Completion.create(
        model = 'text-davinci-003',
        prompt = prompt,
        max_tokens = 5
    )
    return response['choices'][0]['text']
