from . import task

def new_task(task_list):
    """
    Function that creates a new instance of Task.

    Parameters
    ----------
    task_list : list
        A list of to-do tasks

    Returns
    ---------
    task_new : Task object
        A new task object with attributes inputted by user (or using default
        values if invalid inputs)

    """
    conflict = False

    # Ask user for the task name
    name = input("Please input task name: ")

    # Check if the task name exist in task_list
    name_check = [task.name == name for task in task_list]

    # If there is name conflict, rename the new task name
    while any(name_check):
        name += '_2'
        name_check = [task.name == name for task in task_list]
        conflict = True

    if conflict:
        print("Name conflicts found. Suffi(ces) '_2' added to the task name.")

    task_new = task.Task(name=name)

    start_date = input("Please input the start date of the task " +
                       "(default=today): ")
    task_new.start_date = start_date
    end_date = input("Please input the deadline (default=NaT): ")
    task_new.deadline = end_date
    completed = input("Please input if the task is completed or not " +
                      "(default=False): ")
    task_new.completed = completed

    return task_new

def add_new(task_list):
    """
    Function that adds a new task to a task list.

    Parameters
    ----------
    task_list : list
        A list of to-do tasks

    Returns
    ---------
    task_list : list
        with the a new task added

    """
    # create a new task
    task = new_task(task_list)
    return task_list.append(task)
