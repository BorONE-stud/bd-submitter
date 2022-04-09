import os.path

default_path = 'token'

def exists(*, path=default_path):
  return os.path.isfile(path)

def get(*, path=default_path):
  with open(path, 'r') as file:
    return file.readline().strip()

def set(token, /, *, path=default_path):
  with open(path, 'w') as file:
    file.write(f'{token}\n')

def how_to_get():
  return '\n'.join([
    'You can create token on gitlab:',
    '  Edit profile > Access token',
    'Or just visit:',
    '  https://gitlab2.atp-fivt.org/-/profile/personal_access_tokens',
    'It is required to tick \'api\'!',
  ])
