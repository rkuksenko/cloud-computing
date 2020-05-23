from task import Task
import logging
import log
import time
from task import TaskState

logger = logging.getLogger('Whole')

class TaskController:
    tasks_count = 0

    def __init__(self):
        logger.info('TaskController created!')
        self.tasks = []

    def push_task_for(self, duration: int):
        new_task = Task(duration)
        new_task.start()

        self.tasks.append(new_task)
        logger.info('New task pushed!')
        logger.info(f'Current task count: {Task.get_current_task_count()}')

    # def _need_remove_task(self, task):
    #     print(task.get_current_state())
    #     return task.get_current_state() == TaskState.FINISHED

    # def _update_tasks(self):
    #     for task in self.tasks:
    #         if self._need_remove_task(task):
    #             self.tasks.remove(task)

    def get_tasks_number(self):
        return Task.get_current_task_count()

    def get_all_tasks(self):
        for i in self.tasks:
            logger.info(f'Task {i} returned')
            yield str(i)
