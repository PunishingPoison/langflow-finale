from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS to allow requests from other origins (for frontend)
CORS(app)

# Dummy AI processing function (replace with actual AI model integration)
def process_with_ai(user_input):
    """
    This function simulates the AI processing.
    Replace this with your actual AI model's logic.
    For example, you can use Hugging Face, GPT, or any other AI framework.
    """
    # Here, we're just simulating the response.
    # Replace this with the real processing logic for your AI.
    return f"Processed response for: {user_input}"

@app.route('/api/run', methods=['POST'])
def run():
    # Parse incoming JSON data from the request
    data = request.get_json()
    
    # Get user input from the request
    user_input = data.get('input')

    # Check if the user input is valid
    if not user_input:
        return jsonify({'error': 'No input provided'}), 400

    # Process the input with the AI model
    ai_response = process_with_ai(user_input)

    # Return the AI's response as JSON
    return jsonify({'response': ai_response})

# Run the Flask app
if __name__ == '__main__':
    # Run the app on the specified host and port (you can set host='0.0.0.0' for production)
    app.run(debug=True, host='0.0.0.0', port=5000)
