
# Basic Rule-Based Chatbot

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Welcome to ayush Python Chatbot."

    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"

    elif user_input == "what is your name":
        return "I am ayuPyBot, your friendly chatbot."

    elif user_input == "who created you":
        return "I was created by ayush sir using python programming ."

    elif user_input == "what can you do":
        return "I can answer basic questions and chat with you."

    elif user_input == "thank you":
        return "You're welcome! Happy to help."

    elif user_input == "bye" or user_input == "exit":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that. Please try something else."

# Main program
def start_chatbot():

    print("===================================")
    print("       WELCOME TO PYTHON CHATBOT")
    print("===================================")
    print("Type 'bye' or 'exit' to end the chat.\n")

    while True:

        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "exit"]:
            break

# Run chatbot
start_chatbot()