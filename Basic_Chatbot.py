def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hi! How can I help you?"
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."
    elif "bye" in user_input:
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that."

print("Welcome to Chatbot! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)
    if "bye" in user_input.lower():
        break
