from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Basic chatbot logic
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! What about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "your name" in user_input:
        return "I'm a simple chatbot built with Python!"
    elif "help" in user_input:
        return "Sure! You can say hello, ask how I am, or say bye."
    else:
        return "I'm not sure I understand. Can you try rephrasing?"

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Chat route to handle messages
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    print("User said:", user_message)  # Debug print

    bot_response = get_response(user_message)
    print("Bot replied:", bot_response)  # Debug print

    return jsonify({"response": bot_response})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
