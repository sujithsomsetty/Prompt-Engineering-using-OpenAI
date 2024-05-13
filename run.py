import os #to export the open API KEY
import openai


# Set the path to the 'key.txt' file
key_file_path = '/Volumes/Alfred/key.txt'  

# Set the API key path
openai.api_key_path = key_file_path


response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo', #model = to specify which gpt model we want to use
    messages=[
        {
            'role':'system', 'content': 'You have a nice day',
        },
        {
            'role':'user', 'content': 'How is the ICC world cup 2023 going?',
        }
    ],
    temperature = 0.5,
      # Temperature can take values from 0 to 2. closer to 0 will give responses more conversation concise and closer to
      #values closer to 2 will give more random answers
      max_tokens =  1024
      # to tokenize the length of our query  


)

print(response)
print()
print(response.choices[0].message.content)
