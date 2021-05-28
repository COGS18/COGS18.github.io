### Module Import

from twentiethx import ducklings_race

bark = ducklings_race()
bark.add_duckling('Donald', 5, 'aka Mr. Duck')
bark.add_duckling('Daisy', 7, 'aka Mrs. Duck')
bark.add_duckling('Mickey', 2, 'not a duck, but it is fine')
print(bark.roster)
bark.winner()

### Script Execution

!python twentiethx_script.py