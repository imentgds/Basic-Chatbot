import nltk
import random
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!"]
    ],
    [
        r"what's your name ?",
        ["You can call me Chatbot.", "I'm Chatbot!"]
    ],
    [
        r"(.*) your name ?",
        ["You can call me Chatbot.", "I'm Chatbot!"]
    ],
    [
        r"how old are you ?",
        ["I'm just a computer program, so I don't have an age."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual assistant, so I don't have a physical location."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
]

# Create a chatbot using the defined patterns and responses
def chatbot():
    print("Welcome! I'm a chatbot. You can start a conversation with me. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    chatbot()
