#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the GPT-3.5 engine
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,  # Control response length
        stop=None  # Let the model finish its response
    )
    return response.choices[0].text.strip()

# Example interaction
while True:
    player_input = input("You: ")
    prompt = f"Player: {player_input}\nDM:"
    dm_response = generate_response(prompt)
    print("DM:", dm_response)

