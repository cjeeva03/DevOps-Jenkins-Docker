from flask import Flask, jsonify

app = Flask(__name__)
app.debug = True
app.secret_key = 'development'

@app.route("/health")
def health():
    return jsonify(status="ok")
@app.route("/hello/<name>")
def hello(name: str):
    return jsonify(message=f"Hello, {name}!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
