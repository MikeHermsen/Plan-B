from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return 'Hello world'


@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    print("Data Received:", data)
    return jsonify(status="success", data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
