# BD submitter
_Ирония порою может излечить даже то, что заражено пафосом._

## Before everything
- `pip install python-gitlab` or your personal variation.
- [Generate ssh-key](https://gitlab2.atp-fivt.org/-/profile/keys). 
Leave passphrase empty if you do not want to enter it for every task.
- [Generate access token](https://gitlab2.atp-fivt.org/-/profile/personal_access_tokens). Tick `api` in __Select scopes__. Save it to file named `token` in `bd-submitter` directory.
- ... hope I have not forgot anything important

## Before every contest
- Clone homework repository to `bd-submitter` directory. [Projects](https://gitlab2.atp-fivt.org/dashboard/projects)

## How to use submitter
- Create directory named after homework (e.g. `hw3`).
- Save code to file in the directory. Follow pattern:
  - Commment starting with `--`, space, task number (the one on [sql-ex](https://www.sql-ex.ru)).
  - Code related to task with the nubmer.
  - Repeat for every task.
- Save screenshots to the directory. Every screenshot must be named after task number (the one on [sql-ex](https://www.sql-ex.ru)) with `.png` format.
- Run `submitter`-script with argument wich stands for homework (e.g. `hw3`).

### If you already have splitted into files
- Make sure your tasks named according ot rules: `task-N.sql`, where `N` is a task number (the one on [sql-ex](https://www.sql-ex.ru)).
- Copy all of your task files to directory `tasks` in `bd-submitter` directory.
- Leave 'file to split' empty. (It appears while running `submitter` script).

### What do you mean by 'Are you *?'
- Name before dash and `hwX` on each repository. Propably your @username on (gitlab)[https://gitlab2.atp-fivt.org]
