import sys
import time

from pynput.keyboard import Key

from KeyAnalyzer import KeyAnalyzer


class TaskAnalyzer(object):
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


def correct_lines(lines):
    return [line.replace('\n', '') for line in lines]


if __name__ == '__main__':
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        lines = file.readlines()
        tasks = correct_lines(lines)
        task_analyzer = TaskAnalyzer(tasks)
        task_analyzer.start_analysis()
        sorted_tasks = task_analyzer.get_sorted_tasks()
        for task, priority in sorted_tasks:
            print(f'{task}\t{priority / 2}')
