# ============================================================
# PRACTICAL 8: BUILD A SIMPLE RULE-BASED CHATBOT
# ============================================================


# Function to generate chatbot responses
def chatbot_response(user_message):

    # Convert user input into lowercase
    # This helps us compare text easily
    user_message = user_message.lower()


    # --------------------------------------------------------
    # GREETING
    # --------------------------------------------------------

    if "hello" in user_message or "hi" in user_message or "hey" in user_message:

        return "Hello! How can I help you?"


    # --------------------------------------------------------
    # HOW ARE YOU
    # --------------------------------------------------------

    elif "how are you" in user_message:

        return "I am fine! Thank you for asking."


    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    elif "your name" in user_message or "who are you" in user_message:

        return "I am a simple rule-based chatbot created using Python."


    # --------------------------------------------------------
    # COLLEGE / STUDY
    # --------------------------------------------------------

    elif "college" in user_message:

        return "College is a great place to learn new skills and technologies."


    elif "study" in user_message or "studying" in user_message:

        return "Keep studying regularly and practice every day!"


    # --------------------------------------------------------
    # NLP
    # --------------------------------------------------------

    elif "nlp" in user_message:

        return "NLP stands for Natural Language Processing. It helps computers understand human language."


    # --------------------------------------------------------
    # MACHINE LEARNING
    # --------------------------------------------------------

    elif "machine learning" in user_message:

        return "Machine Learning is a branch of Artificial Intelligence where computers learn patterns from data."


    # --------------------------------------------------------
    # PYTHON
    # --------------------------------------------------------

    elif "python" in user_message:

        return "Python is a popular programming language used in AI, Machine Learning and Data Science."


    # --------------------------------------------------------
    # THANK YOU
    # --------------------------------------------------------

    elif "thank" in user_message:

        return "You are welcome!"


    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    elif "bye" in user_message or "exit" in user_message or "quit" in user_message:

        return "Goodbye! Have a nice day!"


    # --------------------------------------------------------
    # DEFAULT RESPONSE
    # --------------------------------------------------------

    else:

        return "Sorry, I do not understand your question."


# ============================================================
# CHATBOT START
# ============================================================

print("========================================")

print("RULE-BASED CHATBOT")

print("Type 'bye' to exit the chatbot.")

print("========================================")


# Run chatbot continuously
while True:

    # Take input from user
    user_input = input("\nYou: ")


    # Get response from chatbot
    response = chatbot_response(user_input)


    # Display chatbot response
    print("Chatbot:", response)


    # Stop chatbot when user enters bye, exit or quit
    if user_input.lower() in ["bye", "exit", "quit"]:

        break
    