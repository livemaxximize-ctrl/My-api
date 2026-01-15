from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    num = request.args.get("num")
    return jsonify({
        "number": num,
        "status": "ok"
    })

app.run(host="0.0.0.0", port=10000)
