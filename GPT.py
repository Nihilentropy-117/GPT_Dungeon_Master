import openai

openai.api_key = ''

def call(prompt, maxLength=500):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=.5,
        max_tokens=maxLength,
        n=1,
        stop=None
    )
    return response.choices[0].message.content

