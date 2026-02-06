from mouth import speak
from openai import OpenAI
from personality import build_system_prompt
SYSTEM_PROMPT = build_system_prompt()
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)



def classify_intent(spoken_text: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a STRICT intent classifier for a voice assistant.\n\n"

                    "Definitions:\n"
                    "- command: The user is directly telling the assistant to DO something now.\n"
                    "  Examples: 'open spotify', 'turn off wifi', 'play music'\n\n"

                    "- question: The user is asking HOW, WHY, or WHAT about something.\n"
                    "  This includes questions about actions.\n"
                    "  Examples: 'how do I open a python file', 'can you tell me how to open spotify'\n\n"

                    "- conversation: Storytelling, opinions, or casual speech.\n\n"

                    "CRITICAL RULES:\n"
                    "- If the sentence contains words like 'how', 'why', 'what', 'can you tell me',\n"
                    "  'explain', or ends like a question → it is NOT a command.\n"
                    "- Questions about actions are ALWAYS 'question', never 'command'.\n\n"

                    "Reply with ONLY one word: command, question, or conversation."
                )
            },
            {"role": "user", "content": spoken_text}
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip().lower()


def ask_ai(prompt):  

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        temperature=0.65,
        max_output_tokens=600,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    try:
        return response.output_text
        #ai will speak you through its thought process 
        #text=response.output[0].content[0].text
        #speak(text)
    except:
        return "Error"