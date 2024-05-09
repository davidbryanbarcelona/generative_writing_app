import streamlit as st
import openai


from openai import AsyncOpenAI
from openai import OpenAI

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=st.secrets["API_key"],
)

async def generate_response(question, context):
  model = "gpt-3.5-turbo"
  #model - "gpt-3.5-turbo"

  completion = await client.chat.completions.create(model=model, 
      messages=[{"role": "user", "content": question}, 
                {"role": "system", "content": context}])
  return completion.choices[0].message.content


async def app():
    
  text = """David Bryan S. Barcelona\n\n
  CCS 229 - Intelligent Systems
  College of Information and Communications Technology
  West Visayas State University"""
  st.text(text)
 

  st.title("Creative Writing Assistant App")
  st.image('write_ai.png', width=350)
    
  # Text area input for describing the literary
  desccribe = st.text_area("Describe the literary you want to write:")
    
   # User selects the type of literature to generate
  genre = st.selectbox(
      "Select the type of literature you want to generate:",
      ["Poetry", "Drama", "Fiction", "Non-Fiction", "Folklore"]
  )

  prompt = ""
        if genre == "Science Fiction":
            prompt = "Write a science fiction story about"
        elif genre == "Fantasy":
            prompt = "Write a fantasy story about"
        elif genre == "Mystery":
            prompt = "Write a mystery story about"

  # Text input for user question
  question = st.text_input("Enter your question:")
  
  # Button to generate response
  if st.button("Generate Response"):
      if question and context:
          response = await generate_response(question, context)
          st.write("Response:")
          st.write(response)
      else:
          st.error("Please enter both question and context.")

#run the app
if __name__ == "__main__":
  import asyncio
  asyncio.run(app())
