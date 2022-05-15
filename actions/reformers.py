def reformat_tasks(tasks):
    """ make iterable tasks to dict() mapped by 'gid'"""
    tasks_mapped_by_gid = dict()
    try:
        for task in tasks:
            gid = task.pop('gid')
            tasks_mapped_by_gid[gid] = task

        return tasks_mapped_by_gid
    except KeyError as e:
        print(e)
