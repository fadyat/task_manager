import os
import time
import keyboard

from asana_api import client_tasks


class TaskManager:
    def __init__(self):
        self.tasks = client_tasks.get_tasks()
        self.tasks_list = list(self.tasks)
        self.scores = dict.fromkeys([t['gid'] for t in self.tasks_list], 0)

    def analyze(self):
        for i in range(len(self.tasks_list)):
            first_task = self.tasks_list[i]
            for j in range(i + 1, len(self.tasks_list)):
                second_task = self.tasks_list[j]
                self.compare_tasks(first_task, second_task)

        sorted_gids = sorted(self.scores.items(),
                             key=lambda x: x[1],
                             reverse=True)

        sorted_tasks = [(self.find_task(task_gid), priority)
                        for task_gid, priority in sorted_gids]

        return sorted_tasks

    def compare_tasks(self, first_task, second_task):
        print(f'{first_task["name"]} | {second_task["name"]}?')
        os.system("stty -echo")
        while True:
            if keyboard.is_pressed('left'):
                self.scores[first_task['gid']] += 2
                break

            elif keyboard.is_pressed('right'):
                self.scores[second_task['gid']] += 2
                break

            elif keyboard.is_pressed('up'):
                self.scores[first_task['gid']] += 1
                self.scores[second_task['gid']] += 1
                break

        time.sleep(.3)

    def find_task(self, task_gid):
        for task in self.tasks_list:
            if task['gid'] == task_gid:
                return task

        return None
