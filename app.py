from flask import Flask, request, jsonify
from google.generativeai import client

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    # Call Google Gemini API and get response (pseudo code)
    response = client.generate_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)