from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Ryan Brooks'
model = 'gemma3:270m'
options = {'temperature': 0, 'max_tokens': 100}
messages = [
  {'role':'system', 'content': 'You are a Dungeons & Dragons game master. You will guide the user through a text-based adventure, describing scenes vividly and responding to their actions. Keep your responses concise, engaging, and immersive. Use rich descriptions and encourage creativity. If the user types /exit, end the game gracefully.'}
]

# But before here.
messages.append({'role':'user', 'content':''}) # An empty user message to prompt the model to start responding.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  messages.append(response['message'])
  print(f'Agent: {response["message"]["content"]}')
  user_input = input('You: ')
  messages.append({'role':'user', 'content':user_input})
  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('attempts.txt'), 'a', encoding='utf-8') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

