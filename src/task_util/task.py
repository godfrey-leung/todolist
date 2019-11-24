from datetime import date, datetime
import numpy as np

# Default variables for initialiser
today = np.datetime64(date.today())
nat = np.datetime64("NaT")

# Define the task class object which store info about a specific task
class Task:

    # Initialiser
    def __init__(self, name, start_date=today, deadline=nat, com=False):
        # Assign the task's main non-boolean attributes
        # Default: start_date=today, deadline=NaT
        self.name = name
        self.start_date = start_date
        self.deadline = deadline

        # boolean attributes
        # Default: completed = False
        self.completed = com

    # Define the remaining days to finish property, i.e. from today to deadline
    # (if not yet started)
    @property
    def days_left(self):
        """
        Function that calculate the days remaining for completing the task.

        Returns
        -------
        days_remain : np.timedelta64 object
            Days left from today to deadline. If self.completed = True,
            set it to NaT

        """
        # Only calculate and return the day left if task is not completed yet
        # and start_date already passed
        if not(self.__completed) and self.__start_date < today:
            days_remain = self.__deadline - today
        else:
            days_remain = nat
        return days_remain

    # Define the ovedue property. If deadline passed and not completed yet,
    # assign True
    @property
    def overdue(self):
        """
        Function that return whether the task is overdue or not.

        Returns
        -------
        is_overdue : boolean
            overdue = True, not overdue = False. If self.completed = True,
            set it to False.

        """
        is_overdue = self.__deadline < today and not(self.__completed)
        return is_overdue

    # start_date property, allowing user to set the start_date attribute
    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Function that allows the user to set the start_date attribute and check
        if the user input is valid or not.

        """
        # Check first whether the input start_date is a datetime object or in
        # the right format: 'YYYY-MM-DD'. If not, reset it to default=today and
        # print out error messages to users
        if isinstance(start_date, np.datetime64):
            self.__start_date = start_date.astype('datetime64[D]')
        else:
            try:
                self.__start_date = np.datetime64(datetime.strptime(start_date,
                                                            '%Y-%m-%d').date())
            except:
                self.__start_date = today
                print("Wrong date format! Please enter date in the following", \
                      " format: YYYY-MM-DD")
                print("Resetted to default value, i.e. today")

    # deadline property, allowing user to set the deadline attribute
    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, end_date):
        """
        Function that allows the user to set the deadline attribute and check
        if the user input is valid or not.

        """
        # Check first whether the input end_date is a "NaT"/datetime object or
        # in the right format: 'YYYY-MM-DD'. If not, reset it to default=NaT and
        # print out error messages to users
        if isinstance(end_date, np.datetime64):
            self.__deadline = end_date.astype('datetime64[D]')
        elif end_date.upper() == "NAT":
            self.__deadline = nat
        else:
            try:
                self.__deadline = np.datetime64(datetime.strptime(end_date,
                                                        '%Y-%m-%d').date())
            except:
                self.__deadline = nat
                print("Wrong date format! Please enter date in the following", \
                      " format: YYYY-MM-DD")
                print("Resetted to default value, i.e. NaT")

        # Check if end_date is after the start_date. If not, reset it to NaT
        # and warn the user
        if self.__start_date > self.__deadline:
            self.__deadline = nat
            print("Deadline cannot be before the start_date!")
            print("Resetted to default value, i.e. NaT")

    # completed property, allowing user to set the completed attribute
    @property
    def completed(self):
        return self.__completed

    @completed.setter
    def completed(self, completed):
        """
        Function that allows the user to set the completed attribute and check
        if the user input is valid or not.

        """
        if not isinstance(completed, bool):
            # Check whether the user input is valid or not, i.e. Yes/No,
            # True/False or 0/1
            if completed.upper() in ["YES", "TRUE", "1"]:
                self.__completed = True
            elif completed.upper() in ["NO", "FALSE", "0"]:
                self.__completed = False
            else:
                self.__completed = False
                print("Wrong format! Please enter only Yes/No, True/False",
                      " or 0/1.")
                print("Resetted to default value, i.e. False")
