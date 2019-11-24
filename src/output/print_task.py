import pandas as pd


def output_task(task_list):
    """
    Function that returns and print the input to-do list in the Pandas
    Dataframe format.

    Parameters
    ----------
    task_list : list
        A list of class Task objects

    Returns
    -------
    df_task : Pandas DataFrame
        A to-do task list built from the input task_list

    """
    task_headers = ['name', 'start_date', 'deadline', 'days_left',
                   'completed', 'overdue']
    df_task = pd.DataFrame(columns=task_headers)

    for task in task_list:
        task_attr_dict = {'name': task.name, 'start_date': task.start_date,
                          'deadline': task.deadline, 'days_left': task.days_left,
                          'completed': task.completed, 'overdue': task.overdue}

        task_to_add = pd.Series(task_attr_dict)
        df_task_to_add = task_to_add.to_frame().transpose()
        df_task = df_task.append(df_task_to_add, ignore_index=True)

    # Print the resulting dataframe to screen
    print( "\n", df_task, "\n")

    return df_task
