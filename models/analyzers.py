import time
from pynput.keyboard import Key, Listener
from asana_api import client_tasks


class KeyAnalyzer:
    pressed_key = None

    @classmethod
    def on_press(cls, key):
        cls.pressed_key = key
        return key not in [Key.left, Key.right, Key.up]

    @classmethod
    def listen(cls):
        with Listener(on_press=cls.on_press) as listener:
            listener.join()


class TaskAnalyzer:
    important_task_cost = 2
    equally_task_cost = 1

    def __init__(self, api_key):
        self._tasks = list(client_tasks.get_tasks(api_key))
        self._scores = dict.fromkeys([t['gid'] for t in self._tasks], 0)

    def _compare_tasks(self, left_task, right_task):
        self._display_choice(left_task, '|', right_task)
        KeyAnalyzer.listen()
        if KeyAnalyzer.pressed_key == Key.left:
            self.add_scores(left_task, self.important_task_cost)
            self._display_choice(left_task, '>', right_task)

        elif KeyAnalyzer.pressed_key == Key.right:
            self.add_scores(right_task, self.important_task_cost)
            self._display_choice(left_task, '<', right_task)

        elif KeyAnalyzer.pressed_key == Key.up:
            self.add_scores(left_task, self.equally_task_cost)
            self.add_scores(right_task, self.equally_task_cost)
            self._display_choice(left_task, '=', right_task)

        time.sleep(.3)

    def start_analysis(self):
        for i, left_task in enumerate(self._tasks):
            for right_task in self._tasks[i + 1:]:
                self._compare_tasks(left_task, right_task)

    def add_scores(self, task, number):
        self._scores[task['gid']] += number

    @staticmethod
    def _display_choice(first_task, option, second_task):
        print("{0} {1} {2}".format(first_task['name'], option, second_task['name']))

    def get_sorted_tasks(self):
        gid_sorted = sorted(self._scores.items(), key=lambda x: x[1], reverse=True)
        return [(self._find_task_name(gid), priority) for gid, priority in gid_sorted]

    def _find_task_name(self, task_gid):
        for task in self._tasks:
            if task['gid'] == task_gid:
                return task['name']
