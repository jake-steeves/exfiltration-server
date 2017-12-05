from flask import Flask, render_template, request
import datetime

application = Flask(__name__)

@application.route("/")
def index():
    with open("static/messages.txt", "r") as f:
        text = f.read()
    f.closed
    return text

@application.route("/log"):
    try:
        message = request.args.get("msg")
    except:
        return "no message"
    else:
        addr = request.remote_addr
        timestamp = datetime.datetime.now().strftime("%H:%M %m/%d/%y")
        with open("static/messages.txt", "a+") as f:
            f.write(addr + " - " + timestamp + "\n")
            f.write(msg + "\n\n")
        f.closed
    
        return "message logged"
        
    
