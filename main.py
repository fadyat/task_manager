import sys

from models.analyzers import TaskAnalyzer


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
