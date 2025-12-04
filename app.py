from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color: green;'>Flask CI/CD Deployment Successful 🎉</h1><p>Deployed via Jenkins to EC2</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
