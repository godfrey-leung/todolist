import os
from datetime import date
from task_util import add, delete, modify
from output import print_task

if __name__ == '__main__':
    # initialiser
    to_do_list = []
    action = True

    # Path for output files
    current_path = os.getcwd()
    output_path = os.path.join(current_path,r'outputfiles')

    # ask user for actions
    while action:
        # output the current to-do list to screen and save it as dataframe
        df_task = print_task.output_task(to_do_list)

        try:
            action_num = int(input("""What action would you like to do? (1: add task;
                            2: modify; 3: delete task; anything else=quit) """))
        except:
            action_num = 0

        # take the appropriate action
        if action_num == 1:
            add.add_new(to_do_list)
        elif action_num == 2:
            modify.modify(to_do_list)
        elif action_num == 3:
            delete.delete(to_do_list)
        else:
            action = False

    # output the to-do list dataframe to a csv file
    df_task.to_csv(os.path.join(output_path,r'to_do_list.csv'), index=False)
