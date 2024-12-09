from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load the Langflow JSON configuration file
with open("Simple Agent.json", "r") as f:
    langflow_data = json.load(f)

# Define a route to interact with the Langflow flow
@app.route('/api/run', methods=['POST'])
def run_flow():
    user_input = request.json.get('input')
    # Here you would interact with the Langflow flow using the data from the JSON
    # This will likely involve some code that invokes Langflow components
    response = process_with_langflow(user_input)
    return jsonify({"response": response})

# Function to simulate interaction with Langflow (replace with actual code)
def process_with_langflow(input_data):
    # You will need to customize this based on your flow and logic
    return f"Processed input: {input_data}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
