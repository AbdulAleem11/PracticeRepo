from flask import Flask, render_template, request, jsonify
import time
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    if request.method == 'POST':
        url = request.form['url']
        server_url = "http://184.105.6.10:8280/process_url"
        payload = {"url": url}

        # Make a POST request with JSON payload
        response = requests.post(server_url, json=payload)

        if response.status_code == 200:
            res=response.json()
            res=res['result']
            print(res)
        else:
            res='MALWARE Failed'
        return jsonify({'result': f"Prediction: {res}"})
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)