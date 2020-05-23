# from server import runServer
from flask import Flask
from server import Server
from task_controller import TaskController


app = Flask(__name__)
app.config["DEBUG"] = False

s = Server()

Server.register(app)
app.run(host='0.0.0.0', port=80)

