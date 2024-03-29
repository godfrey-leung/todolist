import unittest
import numpy as np
from datetime import date, datetime
from task import Task

class TestTaskMethods(unittest.TestCase):

    def test_task_example1(self):
        """
        Function that test whether an instance of Task returns the expected
        default values. In this example, only the name of the task is inputted.

        """
        task1 = Task(name="pay the bill")

        task_attr = [task1.name, task1.start_date, task1.completed,
                     task1.overdue]
        task_attr_expected = ['pay the bill', np.datetime64(date.today()),
                               False, False]
        self.assertEqual(task_attr, task_attr_expected)
        self.assertTrue(np.isnat(task1.deadline))
        self.assertTrue(np.isnat(task1.days_left))

    def test_task_example2(self):
        """
        Function that test whether an instance of Task returns the expected
        input values. Some of the inputs are not in the correct format and
        default values should be returned.

        """
        task2 = Task(name="study", start_date="2019-01-01",
                    deadline="01/01/2019")
        task2.completed = "n"
        task_attr = [task2.name, task2.start_date, task2.completed,
                     task2.overdue]
        task_attr_expected = ['study',
                              datetime.strptime("2019-01-01",'%Y-%m-%d').date(),
                              False, False]
        self.assertEqual(task_attr, task_attr_expected)
        self.assertTrue(np.isnat(task2.deadline))
        self.assertTrue(np.isnat(task2.days_left))


if __name__ == '__main__':
    unittest.main()
