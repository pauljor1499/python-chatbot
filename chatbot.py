import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'what is your name\??', ['I am a simple chatbot.', 'You can call me Chatbot.']),
    (r'ok', ['Ask me anything.']),
    (r'how are you\??', ['I am fine, thank you!', 'Doing well, and you?']),
    (r'(.*) your (.*)\??', ['Why do you want to know about my %2?', 'You are curious about my %2!']),
    (r'quit', ['Bye! Take care!', 'See you later!']),
    (r'what can you do\??', ['I can chat with you and answer your questions.', 'I can help you with various queries!']),
    (r'help', ['Sure! I can assist you with your questions. Just ask me anything.']),
    (r'what is your favorite color\??', ['I don’t have a favorite color, but I like all colors!', 'Colors are fascinating, aren’t they?']),
    (r'tell me a joke\??', ['Why don’t scientists trust atoms? Because they make up everything!']),
    (r'(.*) (your|you) (.*)\??', ['I am just a bot, but I appreciate your interest in my %3!']),
    (r'what is the weather like\??', ['I’m not sure about the weather, but I can chat about anything else!']),
]

def chatbot():
    print("Hi, I'm a simple chatbot! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')  # Download NLTK resources
    chatbot()
