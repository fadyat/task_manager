import os
import sys
import time
import keyboard


def task_analyzer(tasks):
    correct_tasks = [correct_name(task) for task in tasks]
    task_scores = dict.fromkeys(correct_tasks, 0)
    for i in range(len(correct_tasks)):
        first_task = correct_tasks[i]
        for j in range(i + 1, len(tasks)):
            second_task = correct_tasks[j]
            compare_tasks(task_scores, first_task, second_task)

    sorted_tasks = sorted(task_scores.items(),
                          key=lambda x: x[1],
                          reverse=True)

    for task, priority in sorted_tasks:
        print(f'{task}\t{priority}')


def correct_name(task_name):
    return task_name.replace('\n', '')


def compare_tasks(task_scores, first_task, second_task):
    print(f'{first_task} | {second_task}?')
    while True:
        if keyboard.read_key() == 'left':
            task_scores[first_task] += 1
            break

        elif keyboard.read_key() == 'right':
            task_scores[second_task] += 1
            break

    time.sleep(.3)


if __name__ == '__main__':
    os.system("stty -echo")
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        lines = file.readlines()
        task_analyzer(lines)
