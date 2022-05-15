from asana import Client

import config


def select_option(message, options):
    options_lst = list(options)
    print(message)
    for i, option in enumerate(options_lst):
        print(i, ': ', option['name'])
    index = int(input("Enter your choice (default 0): ") or 0)
    return options_lst[index]


def get_tasks(api_key):
    client = Client.access_token(api_key)
    workspaces = client.workspaces.find_all()
    workspace = select_option('Please choice a workspace:', workspaces)
    projects = client.projects.find_all({'workspace': workspace['gid']})
    project = select_option('Please choice a project', projects)
    tasks = client.tasks.find_all({'project': project['gid']})
    return tasks


def main():
    tasks = get_tasks(config.api_key)
    print([t for t in tasks])


if __name__ == '__main__':
    main()
