from markupsafe import escape
from flask import Flask
from fluent import sender
from fluent import event

app = Flask(__name__)

sender.setup('fluentd.test', host='fluentd', port=24224)

@app.route("/")
def hello_world():
    event.Event('follow', {'from': 'userA', 'to': 'userB'})
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def hello(name):
    event.Event('follow', {'route': name})
    return f"Hello, {escape(name)}!"
