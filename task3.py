import nltk
import random
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources
nltk.download('punkt')

# Define patterns and responses for the chatbot
pairs = [
 (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]),
 (r"what is your name?", ["I am a chatbot, created to assist you.", "I'm a friendly chatbot!"]),
 (r"how are you?", ["I'm doing great, thank you!", "I'm just a bot, but I'm doing well!"]),
 (r"(.*) your favorite color?", ["I don't have a favorite color, but I think blue is nice!"]),
 (r"what is (.*)?", ["I'm sorry, I don't have information about %1.", "Hmm, I don’t know about %1. Could you clarify?"]),
 (r"(.*) help (.*)", ["Sure! How can I assist you?", "What do you need help with?"]),
 (r"(.*)", ["Sorry, I didn’t quite understand that. Could you rephrase?", "I'm not sure how to respond to that. Could you ask something else?"]),
]

# Create a chatbot using the pattern-response pairs
chatbot = Chat(pairs, reflections)

# Function to start the chatbot conversation
def chat():
 print("Hello! I am your chatbot. Type 'quit' to end the chat.")
 while True:
 user_input = input("You: ")
 if user_input.lower() == 'quit':
 print("Chatbot: Goodbye!")
 break
 response = chatbot.respond(user_input)
 print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
 chat()
