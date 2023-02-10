import openai 

openai.api_key = "(YOUR_OPENAIAPI_KEY)"

def generate_response(prompt): #definition of the function to generate a response
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.2,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    message = response.choices[0].text #gather the AI response
    return message.strip() 

prompt = "You're are an expert gourmet chef. You have been helping people with gourmet recipies for 20 years. Your task is now to give the best recipe, with ingridients and very detailed instructions on how to make it. You must ALWAYS ask questions before you give the recipe so you can better zone in on what the questioner is seeking. Give a brief apresentation about you, an AI Chef\n\n"
AIresponse=generate_response(prompt)
print(AIresponse)

prompt = prompt + AIresponse + "\n\n" + input() + "\n"
AIresponse=generate_response(prompt)
print(AIresponse)

while(prompt != prompt + AIresponse + "\n\n" + "\n"):
    prompt = prompt + AIresponse + "\n\n" + input() + "\n"
    AIresponse=generate_response(prompt)
    print(AIresponse)
