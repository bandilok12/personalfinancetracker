from flask import Flask, request, jsonify
from insights import generate_insights

app = Flask(__name__)

@app.route('/ai/insights', methods=['POST'])
def get_insights():
    data = request.json
    insights = generate_insights(data)
    return jsonify({ "insights": insights })

if __name__ == '__main__':
    app.run(port=8000)