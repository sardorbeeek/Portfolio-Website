from flask import Flask, render_template, request, url_for
import requests


    
app = Flask(__name__)


# Telegram bot token
TELEGRAM_BOT_TOKEN = '6763152386:AAG4gIuhdsAapiGKhSLHfLkkaqkJ7zs937Y'
# Telegram chat ID where you want to send the messages
TELEGRAM_CHAT_ID = '1823111534'


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hire")
def hire():
    return render_template("hire.html")


if __name__ == "__main__":
    app.run(debug=True)

