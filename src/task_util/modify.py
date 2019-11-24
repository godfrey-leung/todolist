from . import task


def modify(task_list):
    """
    Function that modifies the attributes of an existing task in a task list.

    Parameters
    ----------
    task_list : list
        A list of to-do tasks

    Returns
    ---------
    task_list : list
        with the task's attribute modified if the task name exists.

    """
    # Ask user for the task name
    name = input("Please input the name of the task to be modified: ")

    # Check if the task name exist in task_list
    name_check = [task.name == name for task in task_list]

    if any(name_check):
        # The list index of the task to be modified
        task_index_to_modify = name_check.index(True)

        # Ask user the attribute to be modified
        ask_attr_str = "Please choose the attribute to be modified " + \
                     "(1: start_date; 2: deadline; 3: completed; " + \
                     "anything else: quit) :"
        attr = input(ask_attr_str)

        if attr == "1":
            new_value = input("Please enter the new start_date: ")
            task_list[task_index_to_modify].start_date = new_value
        elif attr == "2":
            new_value = input("Please enter the new deadline: ")
            task_list[task_index_to_modify].deadline = new_value
        elif attr == "3":
            new_value = input("Please enter the whether the task is completed",
                             " or not: ")
            task_list[task_index_to_modify].completed = new_value
        else:
            pass
    else:
        print("The input task name does not exist in the current to-do list.")

    return task_list
