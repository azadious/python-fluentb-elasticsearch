from markupsafe import escape
from flask import Flask
from fluent import sender
from fluent import event

app = Flask(__name__)

logger = sender.FluentSender('app', host='fluentd', port=24224)

@app.route("/")
def hello_world():
    logger.emit('follow', {'from': 'userA', 'to': 'userB'})
    logger.close()

    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    logger.emit('follow', {'from': 'userA', 'to': 'userB'})
    logger.close()
    return f"Hello, {escape(name)}!"
