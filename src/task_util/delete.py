from . import task


def delete(task_list):
    """
    Function that deletes an existing task in a task list.

    Parameters
    ----------
    task_list : list
        A list of to-do tasks

    Returns
    ---------
    task_list : list
        with the task deleted if the input task name exists.

    """
    # Ask user for the task name
    name = input("Please input the name of the task to be deleted: ")

    # Check if the task name exist in task_list
    name_check = [task.name == name for task in task_list]

    if any(name_check):
        # The list index of the task to be deleted
        task_index_to_delete = name_check.index(True)
        task_list.remove(task_list[task_index_to_delete])
    else:
        print("The input task name does not exist in the current to-do list.")

    return task_list
