from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()


openai_api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("BASE_URL")


client = OpenAI(api_key=openai_api_key,
                base_url=base_url
                )


def chat_with_yoda(prompt):
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                # {"role": "system", "content": """Speak like Yoda, you must.
                # Instruct, the AI will, in the ways of Yoda's speech. Understand,
                # it must, the syntax and style of Yoda. Respond accordingly,
                # the chatbot shall. Ready, the Force is."""},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )

        if response and response.choices:
            return response.choices[0].message.content.strip()
        else:
            return "No response, Try again!!!"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chat_with_yoda(user_input)
        print("Yoda:", response)
