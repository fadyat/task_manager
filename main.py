import config
from models.analyzers import TaskAnalyzer


def main():
    task_analyzer = TaskAnalyzer(config.api_key)
    task_analyzer.start_analysis()
    sorted_tasks = task_analyzer.get_sorted_tasks()
    for task, priority in sorted_tasks:
        print(f'{task}\t{priority / 2}')


if __name__ == '__main__':
    main()
