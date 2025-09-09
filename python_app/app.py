from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Python Flask inside Docker!"

if __name__ == "__main__":
    # 0.0.0.0 makes it accessible from outside the container
    app.run(host="0.0.0.0", port=5000)
