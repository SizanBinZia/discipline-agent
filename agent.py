from openai import OpenAI

# Load system prompt from system.md
def load_system_prompt():
    with open("system.md", "r", encoding="utf-8") as f:
        return f.read()

SYSTEM_PROMPT = load_system_prompt()

client = OpenAI()

def agent_response(user_message):
    """Generate response from the Discipline Agent."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ]
    )
    return response.choices[0].message["content"]


# For Kaggle testing (optional)
if __name__ == "__main__":
    print("Discipline Agent is running...\n")
    while True:
        user_input = input("You: ")
        reply = agent_response(user_input)
        print("\nDiscipline Agent:", reply, "\n")
