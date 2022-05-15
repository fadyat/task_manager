import time
from pynput.keyboard import Key, Listener
from asana_api import client_tasks
from actions import reformers


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
        self._tasks = reformers.reformat_tasks(client_tasks.get_tasks(api_key))
        self._scores = dict.fromkeys(self._tasks.keys(), 0)

    def _compare_tasks(self, gid_left, gid_right):
        self._display_choice(gid_left, '|', gid_right)
        KeyAnalyzer.listen()
        if KeyAnalyzer.pressed_key == Key.left:
            self.add_scores(gid_left, self.important_task_cost)
            self._display_choice(gid_left, '>', gid_right)

        elif KeyAnalyzer.pressed_key == Key.right:
            self.add_scores(gid_right, self.important_task_cost)
            self._display_choice(gid_left, '<', gid_right)

        elif KeyAnalyzer.pressed_key == Key.up:
            self.add_scores(gid_left, self.equally_task_cost)
            self.add_scores(gid_right, self.equally_task_cost)
            self._display_choice(gid_left, '=', gid_right)

        time.sleep(.3)

    def start_analysis(self):
        for i, left_task_gid in enumerate(self._tasks.keys()):
            for right_task_gid in list(self._tasks.keys())[i + 1:]:
                self._compare_tasks(left_task_gid, right_task_gid)

    def add_scores(self, task_gid, number):
        self._scores[task_gid] += number

    def _display_choice(self, gid_left, option, gid_right):
        print(f'{self.get_task_name(gid_left)} {option} {self.get_task_name(gid_right)}')

    def get_task_name(self, gid):
        return self._tasks[gid]['name']

    def get_sorted_tasks(self):
        gid_sorted = sorted(self._scores.items(), key=lambda x: x[1], reverse=True)
        return [(self.get_task_name(gid), priority) for gid, priority in gid_sorted]
