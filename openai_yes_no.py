import openai

client = openai.Client(api_key="[YOUR_API_KEY_HERE]")
print(client.chat.completions.create(
    model="gpt-4-1106-preview",
    functions=[
        {
            "name": "yes_no",
            "parameters": {
                "type": "object",
                "properties": {"answer": {"type": "string", "enum": ["yes", "no"]}},
            },
            "description": "Answer the question that was asked to you with either 'yes' or 'no'"
        }
    ],
    function_call={
        "name": "yes_no",
    },
    messages=[
        {
            "role": "user",
            "content": "Is this a test?"
        }
    ],
))

