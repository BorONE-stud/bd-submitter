# BD submitter
_Ирония порою может излечить даже то, что заражено пафосом._

## Before everything
- Clone homework repository from your mail. 
- Generate [ssh-key](https://gitlab2.atp-fivt.org/-/profile/keys)
- Check `bin/config` script and change `NAME`
- ... hope I have not forgot anything important

## Before every contest
- Clone homework repository to `bd-submitter` directory.

## How to use
### From stdin
Just type `./submit [--from-stdin] <task>...` in terminal.
End input with `ctrl+d`. Flag is optional.

### From file
Just type `./submit --from-file <task>...` in terminal.
Make sure you have corresponding files in `tasks` directory.

## Useful tools
### Split
If you have file with tasks you can split it.
If you follow format, file for each task will be splitted.
You can check example with flag `--example`.
To erase example use flag `--erase-example`.

### Auto-comment
Check `commit` script in `bin/` and find `COMMENT_GENERATOR`.
You can make custom generator if you want.
