from decouple import config
import openai
openai.api_key = config("API_KEY")


user_prompt = input("Enter what would you like to Create Today? ")

output = openai.Completion.create(
  model="text-curie-001",
  prompt = user_prompt,
  max_tokens=1000,
  temperature=0.3
)
print('\n')
print(output.choices[0].text)