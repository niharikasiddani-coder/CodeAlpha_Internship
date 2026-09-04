# Basic Chatbot

def chatbot():
    print("===== BASIC CHATBOT =====")
    print("Type 'bye' to exit the chatbot.")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Bot: My name is CodeAlpha Bot.")

        elif user_input == "what can you do":
            print("Bot: I can have a simple conversation with you.")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()