import gitlab
from sys import argv

import access_token

class color:
  attention = "\033[033m"
  underline = "\033[4m"
  reset = "\033[0m"


def print_help():
  print("Usage: python3 mr.py NAME [task]...")
  print()
  print("Creates merge request and attaches screenshot.")
  print("Screenshot should be in a directory named after homework e.g. 'hw3'.")
  print("Screenshot should be named after task on site e.g. '7.png'.")


def get_access_token(access_token_path: str = 'access_token'):
  if not access_token.exists():
    print(f'access_token file \'{access_token.default_path}\' is not found!')
    print(access_token.how_to_get())
    set(input('Enter access_token: '))
  return access_token.get()


def map_task(task):
  tasks = {
    'hw1': [ 1,  2, 10, 17, 31,  33,  38,  44, 53, 62],
    'hw2': [11, 12, 15, 20, 22,  29,  30,  68, 74, 86],
    'hw3': [ 7,  9, 14, 16, 23,  32,  48,  84],
    'hw4': [37, 41, 47, 70, 73,  87, 102, 112],
    'hw5': [65, 82, 90, 96, 98, 100, 105, 109],
  }
  for hw, hw_tasks in tasks.items():
    try:
      ord_task = hw_tasks.index(task) + 1
      return {
        'hw': hw,
        'ord_task': f'task{ord_task}',
        'site_task': str(task)
      }
    except:
      pass
  raise ValueError(f'task {task} not found')


def create_mr(project, *, hw, ord_task, site_task):
  """
  Creates MR, attaches screenshot.
  Args:
    hw: string e.g. 'hw3'
    ord_task: string e.g. 'task2'
    site_task: string e.g. '9'
  Returns:
    created MR
  """
  uploaded = project.upload(site_task, filepath=f'{hw}/{site_task}.png')

  return project.mergerequests.create({
    'source_branch': f'{hw}{ord_task}',
    'target_branch': 'main',
    'title': f'{hw}{ord_task}',
    'description': f"!{uploaded['markdown']}"
  })


def get_project_by(*, name):
  # this is kinda naive, but whatever
  gl = gitlab.Gitlab('https://gitlab2.atp-fivt.org', private_token=get_access_token())
  return next(project for project in gl.projects.list() if project.name == name)


def main():
  if len(argv) == 1 or argv[1] == '--help':
    print_help()
    return

  NAME = argv[1]
  tasks = argv[2:]
  
  if NAME == 'user':
    print(color.attention, "NAME is not set!!!", color.reset, sep='')
    print('Check bin/config.')
    return

  for task in tasks:
    mapped = map_task(int(task))
    project = get_project_by(name=f"{NAME}-{mapped['hw']}")
    mr = create_mr(project, **mapped)
    print(f"{mapped['hw']}{mapped['ord_task']}:")
    print(" ", mr.web_url)


if __name__  == '__main__':
  main()
