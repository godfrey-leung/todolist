# todolist

Todolist is a simple Python library for creating a to-do list by asking user
inputs from terminal. User can add, modify and delete any tasks in the list.
When quit, the to-do list is returned as a csv file.

## Output

./src/outputfiles/to_do_list.csv

## An example of output to-do list
```
        name  start_date    deadline days_left completed overdue
0     study  2019-10-31         NaN       NaN     False   False
1   study_2  2019-11-24  2019-12-31       NaN      True   False
2  pay bill  2019-11-21  2019-11-23       NaN      True   False
```
## Note

The default task attributes are
```
start_date = today
deadline = NaT
completed = False
```
For simplicity, start_date and deadline must be inputted in YYYY-MM-DD format,
and completed in [Yes/No, True/False, 0/1]. Attributes are resetted to default
if not in valid format. 

## Version

1.0.0

## Author

Godfrey Leung, godfrey.leung.cosmo@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
