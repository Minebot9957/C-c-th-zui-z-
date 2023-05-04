import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = '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'
completion = openai.Completion()

def Reply(text) :
  prompt = text
  response = completion.create(prompt = prompt,engine = "text-davinci-003",temperature=0.7,max_tokens=256)
  answer = response.choices[0].text.strip()
  return answer

ans = Reply("Iphone là gì")
print (ans)
  







