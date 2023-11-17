import nltk
from nltk.chat.util import Chat, reflections
from flask import Flask, render_template, request

# Define pairs of patterns and responses
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you', ['I am good, thank you!', 'I am doing well. How about you?']],
    ['what is your name', ['I am a chatbot. You can call me ChatGPT.']],
    ['bye|goodbye', ['Goodbye!', 'See you later!']],
]

# Create a chat object
chatbot = Chat(pairs, reflections)

# Create a Flask web app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle chat interactions
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = chatbot.respond(user_input)
    return {'response': response}

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
