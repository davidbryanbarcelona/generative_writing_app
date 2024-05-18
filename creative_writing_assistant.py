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
  genre = st.selectbox(
      "Select the type of literature you want to generate:",
      ["Poetry", "Drama", "Fiction", "Non-Fiction", "Folklore"]
  )

  # User inputs what plot is in its mind right now
  plot = st.text_input("Enter the plot of the literary work on your mind right now:")
  
  # User inputs neccessary keywords of the literary they want to generate
  context = st.text_input("Enter the keywords of the literary work you want to write:")
  
  # Button to generate response
  if st.button("Generate Response"):
      if question and context:
          response = await generate_response(question, context)
          st.write("It's always a pleasure to help! Here is the answer to your request:")
          st.write(response)
      else:
          st.error("Please input all the required fields.")

#run the app
if __name__ == "__main__":
  import asyncio
  asyncio.run(app())
