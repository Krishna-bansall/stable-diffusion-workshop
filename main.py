from decouple import config
import openai
import json

openai.api_key = config("API_KEY")
json_file = open("data.json", "a")

# user_prompt = input("Enter what would you like to Create Today? ")

user_prompt = input("topic of your spidey story: ")

fin_prompt = """
Generate comic book with 20 dialogues and keywords describing the enviroment with context for dalle-2
to generate accompanying images in format of json

Topic -""" + user_prompt + """
  { 
  "content": [
    {
      "spidey": "wow it was difficult day today",
      "prompt": "a close up of a comic book cover, comic book panel, spiderman in red relaxing reading a book, sitting on terrace, day, sleeping, wide, center marvel : 6 | ugly, disfigured hand : -2"
    },
    {
      "narrator": "loud noises",
      "prompt": "a close up of a comic book cover, comic book panel, full blue building, comic blast, debris, smoke, shattered glass, wide, center marvel : 6 | ugly, disfigured hand : -2"
    },
    {
      "spidey": "what was that?",
      "prompt": "a close up of  a comic book cover, comic book panel, spiderman alerted, close up face, spide sense, day, wide, center marvel : 6 | ugly, disfigured hand : -2"
    },
    {  
    """

output = openai.Completion.create(
  model="text-davinci-003",
  prompt = fin_prompt,
  max_tokens=4097-300,
  temperature=0.3
)
print('\n')
print((output.choices[0].text))
main_output = """
{ 
  "content": [
    {
      "spidey": "wow it was difficult day today",
      "prompt": "a close up of a comic book cover, comic book panel, spiderman in red relaxing reading a book, sitting on terrace, day, sleeping, wide, center marvel : 6 | ugly, disfigured hand : -2"
    },
    {
      "narrator": "loud noises",
      "prompt": "a close up of a comic book cover, comic book panel, full blue building, comic blast, debris, smoke, shattered glass, wide, center marvel : 6 | ugly, disfigured hand : -2"
    },
    {
      "spidey": "what was that?",
      "prompt": "a close up of  a comic book cover, comic book panel, spiderman alerted, close up face, spide sense, day, wide, center marvel : 6 | ugly, disfigured hand : -2"
    },
    {  
""" + output.choices[0].text
json_file.write((main_output))
print(json.load(main_output))