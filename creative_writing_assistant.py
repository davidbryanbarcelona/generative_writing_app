import streamlit as st
import openai


from openai import AsyncOpenAI
from openai import OpenAI

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=st.secrets["API_key"],
)

async def generate_response(question, genre, prompt, describe):
  model = "gpt-3.5-turbo"
  #model - "gpt-3.5-turbo"

  completion = await client.chat.completions.create(model=model, 
      messages=[{"role": "user", "content": question}, 
                {"role": "system", "content": genre},
                {"role": "user", "content": prompt},
                {"role": "user", "content": describe}])
  return completion.choices[0].message.content


async def app():
    
  text = """David Bryan S. Barcelona\n\n
  CCS 229 - Intelligent Systems
  College of Information and Communications Technology
  West Visayas State University"""
  st.text(text)
 

  st.title("Creative Writing Assistant App")
  st.image('write_ai.png', width=350)
    
  # Text input for initialization of the setting and plot keywords
  question = st.text_input("Hi, I'm your Creative Writing Assitant! How can I help your literary?")
   
  # User selects the type of literature to generate
  genre = st.selectbox(
      "Select the type of literature you want to generate:",
      ["Poetry", "Drama", "Fiction", "Non-Fiction", "Folklore"]
  )

  prompt = ""
  if genre == "Poetry":
      prompt = "Write a poetry about"
  elif genre == "Drama":
      prompt = "Write a drama story about"
  elif genre == "Fiction":
      prompt = "Write a fictional story about"
  elif genre == "Non-Fiction":
      prompt = "Write a non-fictional story about"
  elif genre == "Folklore":
      prompt = "Write a folklore story about"

  # Text area input for describing the literary
  describe = st.text_area("Describe the literary you want to write:")

  # Button to generate response
  if st.button("Generate Response"):
      if question and describe:
          response = await generate_response(question, genre, prompt, describe)
          st.write("Response:")
          st.write(response)
      else:
          st.error("Please input all the required fields")

#run the app
if __name__ == "__main__":
  import asyncio
  asyncio.run(app())
