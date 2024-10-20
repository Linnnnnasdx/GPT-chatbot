import openai

# openai.api_key = 'fake-api'
# openai.base_url = "http://localhost:3040/v1/"
openai.api_key = "YOUR_API_KEY"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()

while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit" , "exit" , "bye" ]:
            break

        response = chat_with_gpt(user_input)
        print("GPT:",response)
