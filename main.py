from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt
from google import genai

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from .env
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)

# now loading CSV data
df = pd.read_csv("data.csv")

#Here we convert dataframe to text so the model can read i
data_text = df.to_string(index=False)

#Ask the user for a question
user_question = input("Ask a question about the vehicle data: ")

#The 1.st Tool : Plotting
if "plot" in user_question or "graph" in user_question or "chart" in user_question:
   plt.plot(df["time"], df["battery_temp"])
   plt.xlabel("Time")
   plt.ylabel("Battery Temperature")
   plt.title("Battery Temprature over Time")
   plt.savefig("output.png")
   plt.show()
   print("Plot saved as output.png")
   

#Building the prompt/ 2nd Tool: LLM-based analyst
else:
  prompt = f"""
  You are a strict data analyst.
  
  DATASET:
  {data_text}
  TNSTRUCTION:
  Answer the user's question based ONLY on the dataset.

  -If the question asks about anomalies, identify unusual values.
  -Be specific (mention row and values).
  -If the question is unrelated to the data, respond politely and guide the user to ask relevant questions (e.g., about temperature, voltage, current, or anomalies). 
  -Do not ignore the question.
  -Do not give generic answers.
  -Do Not assume anomalies unless asked

  QUESTION:
  {user_question}

  ANSWER:
  """

   # Send a simple request
  response = client.models.generate_content( 
        model="gemini-3-flash-preview",
        contents=prompt
   )

  print("\nAnswer:")
  print(response.text)