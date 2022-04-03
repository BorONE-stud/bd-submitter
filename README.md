# BD submitter
_Ирония порою может излечить даже то, что заражено пафосом._

## Before everything
- Clone homework repository from your mail. 
- Generate [ssh-key](https://gitlab2.atp-fivt.org/-/profile/keys)
- Check `bin/config` script and change `NAME`
- ... hope I have not forgot anything important

## Before every contest
- Clone homework repository to `bd-submitter` directory.

## If you are lost
- Lanch script without arguments or with flag `--help`. In both cases help will be printed.
- Write [me](https://t.me/BorONE)

## How push
### From stdin
Just type `./submit [--from-stdin] <task>...` in terminal.
End input with `ctrl+d`. Flag is optional.

### From file
Just type `./submit --from-file <task>...` in terminal.
Make sure you have corresponding files in `tasks` directory.

## How MR
In main directory create directory create homework directory named `hw<{1,2,3,4,5}>`.
Put all screenshots in created directory. Name them according to site number with `.png` format
(e.g. `hw3`: `7.png`, `9.png`, ...).
Launch `mr`-script with task site numbers (e.g. `7 9 ...`).
Check printed url to make sure that everything is ok.

## Useful tools
### Split
If you have file with tasks you can split it.
If you follow format, file for each task will be splitted.
You can check example with flag `--example`.
To erase example use flag `--erase-example`.

### Auto-comment
Check `commit` script in `bin/` and find `COMMENT_GENERATOR`.
You can make custom generator if you want.
