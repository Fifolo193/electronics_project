from flask import Flask, request, jsonify
import pickle
import pandas as pd   # or whatever you use

app = Flask(__name__)

def process_data(raw_bytes):
    data = pickle.loads(raw_bytes)
    
    # ←←← PUT YOUR REAL PROCESSING CODE HERE ←←←
    # Example:
    #df = pd.DataFrame(data)
    #df['processed'] = df['value'] * 2
    #result = df.to_dict('records')
    result = {"result" : [1,2,3,4]}
    # ←←← end of your code
    
    return result

@app.route('/process', methods=['POST'])
def process():
    raw = request.data
    if not raw:
        return "No data", 400
    
    try:
        result = process_data(raw)
        # Return as pickle again (or use jsonify(result) if it's JSON-able)
        return pickle.dumps(result), 200, {'Content-Type': 'application/octet-stream'}
    except Exception as e:
        return str(e), 500

@app.route('/')
def home():
    return "Send pickled data to /process"

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8080)
