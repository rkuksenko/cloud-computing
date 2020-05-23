from threading import Thread
from time import sleep
from datetime import datetime
import logging
import log
from enum import Enum

logger = logging.getLogger('Whole')


class TaskState(Enum):
    PROCESSING = 1
    FINISHED = 2
    READY_TO_PROCESS = 3

class Task(Thread):
    global_id = 0
    task_count = 0

    def __init__(self, duration: int):
        Thread.__init__(self)
        self.id = Task.global_id
        self.state = TaskState.READY_TO_PROCESS

        Task.global_id += 1
        Task.task_count += 1

        logger.info(f'Task [{self.id}] started for: {duration} seconds')
        self.task_duration = int(duration)
        self.started_at = datetime.now()
        self.finished_at = ""

    def run(self):
        self.state = TaskState.PROCESSING

        while True:
            now = datetime.now()
            if (now - self.started_at).seconds >= self.task_duration:
                logger.info(f'Task [{self.id}] finished')
                self.state = TaskState.FINISHED
                self.finished_at = now
                Task.task_count -= 1
                break
    
    def __str__(self):
        finished = ''

        if self.state == TaskState.FINISHED:
            finished = f', Finished at: {self.finished_at}'
        else:
            finished = ', Not finished yet'

        return f'Id: {self.id}, Posted: {self.started_at}, Set duration: {self.task_duration}, Status: {self.state}{finished}'

    def get_current_state(self):
        return self.state

    @staticmethod
    def get_current_task_count():
        return Task.task_count

