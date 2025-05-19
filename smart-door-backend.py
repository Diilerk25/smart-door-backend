from flask import Flask, request, jsonify, send_from_directory
import os
import base64
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def serve_index():
    return send_from_directory('frontend', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        data = request.get_json()
        image_data = data['image'].split(',')[1]
        image_bytes = base64.b64decode(image_data)

        # Use timestamp to generate unique filename
        filename = datetime.now().strftime('%Y%m%d_%H%M%S') + '.png'
        filepath = os.path.join(UPLOAD_FOLDER, filename)

        with open(filepath, 'wb') as f:
            f.write(image_bytes)

        return jsonify({"message": f"Image saved as {filename}."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    print("🚀 Starting Flask app version 2...")
    app.run(debug=True)
