from flask import Flask
from flask_classful import FlaskView, route
from task_controller import TaskController
import logging
import log
from pages import MAIN_PAGE


logger = logging.getLogger('Whole')

class Server(FlaskView):
    route_base = ""
    default_methods = ['GET', 'POST']
    controller = TaskController()

    def __init__(self):
        logger.info('Server created')
        super().__init__()

    @route('/', methods=['GET'])
    def home(self):
        return MAIN_PAGE

    @route('/get-active-task-number', methods=['GET'])
    def active_threads_number(self):
        return f'<h1>Current threads count is: {Server.controller.get_tasks_number()}</p>'

    @route('/get-all-tasks', methods=['GET'])
    def all_tasks(self):
        res = []

        for task in Server.controller.get_all_tasks():
            res.append(f'<p>{task}</p>')

        if len(res) == 0:
            res = '<h1>There are no tasks :(</h1>'
        res = ''.join(res)
        return res
    

    @route('push-task-with-weight/<weight>', methods=['POST'])
    def push_task(self, weight) -> str:
        Server.controller.push_task_for(weight)

        return f'<h1>Your "task" has been pushed to computation with weight: {weight}</h1>'\
               f'<h2>Current tasks count: {Server.controller.get_tasks_number()} <h2>'
