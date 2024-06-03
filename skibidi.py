from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hey, I'm Ben"

if __name__ == '__main__':
    # Run the app on the local development server
    app.run(host='0.0.0.0', port=5000)
