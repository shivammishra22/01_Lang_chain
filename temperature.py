from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm=ChatGroq(model_name="Gemma2-9b-It",temperature=0.5)
result = llm.invoke("Write a 5 line poem on cricket")

print(result.content)