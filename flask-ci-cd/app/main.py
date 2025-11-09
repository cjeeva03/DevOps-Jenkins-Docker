from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)
    
    @app.route("/health")
    def health():
        return jsonify(status="ok")
    @app.route("/hello/<name>")
    def hello(name: str):
        return jsonify(message=f"Hello, {name}!")
    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
