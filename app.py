#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2025/03/24 09:06:32
@Author  :   wang.wei@baidaodata.com 
@Version :   1.0
'''
# 配置使用本地代理来访问Google Cloud SDK
import os
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"


from flask import Flask, render_template, request, jsonify
import base64
import os
from google.cloud import aiplatform
from google.cloud.aiplatform.gapic.schema import predict

app = Flask(__name__)

# Configure Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-service-account-key.json"
PROJECT_ID = "your-project-id"
LOCATION = "us-central1"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Get the uploaded image or text query
    if 'image' in request.files:
        image_file = request.files['image']
        image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    else:
        query = request.form.get('query', '')
        # Handle text query if needed
        return jsonify({'results': []})
    
    # Prepare the request for Vertex AI
    aiplatform.init(project=PROJECT_ID, location=LOCATION)
    
    # Replace with your deployed model endpoint ID
    endpoint = aiplatform.Endpoint("your-endpoint-id")
    
    # Prepare the instance for prediction
    instance = {
        "image": {
            "bytesBase64Encoded": image_base64
        }
    }
    
    # Make the prediction request
    prediction_response = endpoint.predict(instances=[instance])
    
    # Process the response
    results = []
    if prediction_response.predictions:
        # Assuming the response contains a list of similar items
        # This will depend on your specific Vertex AI model response format
        for item in prediction_response.predictions:
            results.append({
                "title": item.get("title", "No title"),
                "description": item.get("description", "No description"),
                "image_url": item.get("image_url", "")
            })
    
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
