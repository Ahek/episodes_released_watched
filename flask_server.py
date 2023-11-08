from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.logger.info("Starting the Flask application.")
    app.run(port=5000)
