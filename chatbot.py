import openai

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=2000,
                temperature=0.5,
        ).choices[0].text
        return response

chatbot = Chatbot()
response = chatbot.get_response("Tell me a joke")
print(response)