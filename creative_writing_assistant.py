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
    
  # Text input for initialization of the setting and plot keywords
  question = st.text_area("Hi, I'm your Creative Writing Assitant! How can I help your literary?")
   
  # User selects the type of literature to generate
    # Text input for user question
  context = st.text_input("Enter the genre of the literary you want to write:")
  
  # Button to generate response
  if st.button("Generate Response"):
      if question and context:
          response = await generate_response(question, context)
          st.write("Here is the generated literary:")
          st.write(response)
      else:
          st.error("Please enter both fields.")

#run the app
if __name__ == "__main__":
  import asyncio
  asyncio.run(app())
