import os
import sys
import time
import keyboard


def correct_lines(lines):
    return [line.replace('\n', '') for line in lines]


def task_analyzer(tasks):
    task_scores = dict.fromkeys(tasks, 0)
    for i in range(len(tasks)):
        first_task = tasks[i]
        for j in range(i + 1, len(tasks)):
            second_task = tasks[j]
            compare_tasks(task_scores, first_task, second_task)

    sorted_tasks = sorted(task_scores.items(),
                          key=lambda x: x[1],
                          reverse=True)

    return sorted_tasks


def compare_tasks(task_scores, first_task, second_task):
    print(f'{first_task} | {second_task}?')
    while True:
        key = keyboard.read_key()
        if key == 'left':
            task_scores[first_task] += 2
            break

        elif key == 'right':
            task_scores[second_task] += 2
            break

        elif key == 'up':
            task_scores[first_task] += 1
            task_scores[second_task] += 1
            break

    time.sleep(.3)


if __name__ == '__main__':
    os.system("stty -echo")
    file_name = sys.argv[1]
    with open(file_name, 'r') as file:
        lines = file.readlines()
        tasks = correct_lines(lines)
        sorted_tasks = task_analyzer(tasks)

        for task, priority in sorted_tasks:
            print(f'{task}\t{priority / 2}')
