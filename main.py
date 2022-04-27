import os
import time
import keyboard
from asana_api import client_tasks


def find_task(tasks, task_id):
    for task in tasks:
        if task['gid'] == task_id:
            return task

    return None


def task_analyzer(tasks):
    task_scores = dict.fromkeys([t['gid'] for t in tasks], 0)
    for i in range(len(tasks)):
        first_task = tasks[i]
        for j in range(i + 1, len(tasks)):
            second_task = tasks[j]
            compare_tasks(task_scores, first_task, second_task)

    sorted_tasks_gid = sorted(task_scores.items(),
                              key=lambda x: x[1],
                              reverse=True)

    sorted_tasks = [(find_task(tasks, task_gid), priority)
                    for task_gid, priority in sorted_tasks_gid]

    return sorted_tasks


def compare_tasks(task_scores, first_task, second_task):
    print(f'{first_task["name"]} | {second_task["name"]}?')
    os.system("stty -echo")
    while True:
        if keyboard.is_pressed('left'):
            task_scores[first_task['gid']] += 2
            break

        elif keyboard.is_pressed('right'):
            task_scores[second_task['gid']] += 2
            break

        elif keyboard.is_pressed('up'):
            task_scores[first_task['gid']] += 1
            task_scores[second_task['gid']] += 1
            break

    time.sleep(.3)


def main():
    tasks = list(client_tasks.get_tasks())
    sorted_tasks = task_analyzer(tasks)

    for task, priority in sorted_tasks:
        print(f'{task}\t{priority / 2}')


if __name__ == '__main__':
    main()
