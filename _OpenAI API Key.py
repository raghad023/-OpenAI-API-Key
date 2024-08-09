#!/usr/bin/env python
# coding: utf-8

# In[7]:


pip install openai==0.28


# In[2]:


import openai

# Set your OpenAI API key here
openai.api_key = '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'

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    user_input = input("Please enter your prompt: ")
    response = get_openai_response(user_input)
    print("OpenAI Response:", response)


# In[ ]:





# In[ ]:




