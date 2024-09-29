from flask import Flask, request, jsonify, render_template
import json
import os
from flask_cors import CORS, cross_origin


app = Flask(__name__, template_folder='./')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Path to your JSON file
JSON_FILE = 'data.json'

# Helper function to read data from JSON file
def read_json_file():
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

# Helper function to write data to JSON file
def write_json_file(data):
    with open(JSON_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/update-json', methods=['POST'])
def update_json():
    # Get the incoming JSON data
    new_data = request.get_json()

    if not new_data or not isinstance(new_data, dict):
        return jsonify({'error': 'Invalid data format, must be JSON object.'}), 400

    # Read existing data from the JSON file
    data = read_json_file()

    # Append the new data
    data.append(new_data)

    # Write updated data back to the JSON file
    write_json_file(data)

    # Return success response
    return jsonify({'message': 'Data appended successfully!', 'data': new_data}), 200

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/all_recalls')
# def recalls():
#     return render_template('all_recalls.html')

if __name__ == '__main__':
    app.run(debug=True, port=8001)
