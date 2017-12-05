from flask import Flask, render_template, request
import datetime
import pytz

application = Flask(__name__)

@application.route("/")
def index():
    with open("static/messages.txt", "r") as f:
        text = f.read()
    f.closed
    text = text.replace("\n","<br/>")
    return text

@application.route("/log")
def log_msg():
    try:
        message = request.args.get("msg")
    except:
        return "no message"
    else:
        addr = request.remote_addr
        eastern = pytz.timezone("America/New_York")
        timestamp = datetime.datetime.now(eastern).strftime("%H:%M %m/%d/%y")
        with open("static/messages.txt", "a+") as f:
            f.write(addr + " - " + timestamp + "\n")
            f.write(message + "\n\n")
        f.closed
    
        return "message logged"
