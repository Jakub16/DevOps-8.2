from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "HALTHY"}), 200

@app.route('/default', methods=['GET'])
def hello():
    return jsonify({"message": "test"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
