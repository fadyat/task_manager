from task_manager import TaskManager


def main():
    task_manager = TaskManager()
    sorted_tasks = task_manager.analyze()

    for task, priority in sorted_tasks:
        print(f'{task}\t{priority / 2}')


if __name__ == '__main__':
    main()
