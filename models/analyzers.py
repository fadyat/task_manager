import time

from pynput.keyboard import Key, Listener


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

    def __init__(self, tasks):
        self._tasks = tasks
        self._task_scores = dict.fromkeys(tasks, 0)

    def _compare_tasks(self, left_task, right_task):
        print(f'{left_task} | {right_task}')
        KeyAnalyzer.listen()
        if KeyAnalyzer.pressed_key == Key.left:
            self._task_scores[left_task] += self.important_task_cost
            print(f'{left_task} > {right_task}')

        elif KeyAnalyzer.pressed_key == Key.right:
            self._task_scores[right_task] += self.important_task_cost
            print(f'{left_task} < {right_task}')

        elif KeyAnalyzer.pressed_key == Key.up:
            self._task_scores[left_task] += self.equally_task_cost
            self._task_scores[right_task] += self.equally_task_cost
            print(f'{left_task} = {right_task}')

        time.sleep(.3)

    def start_analysis(self):
        for i, left_task in enumerate(self._tasks):
            for right_task in self._tasks[i + 1:]:
                self._compare_tasks(left_task, right_task)

    def get_sorted_tasks(self):
        return sorted(self._task_scores.items(), key=lambda x: x[1], reverse=True)
