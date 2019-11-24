import unittest
import numpy as np
from datetime import date
from task import Task

class TestTaskMethods(unittest.TestCase):

    def test_task_example1(self):
        """
        Function that test whether an instance of Task returns the expected
        default values. In this example, only the name of the task is inputted.

        """
        task = Task(name="pay the bill")
        task_attr = [task.name, task.start_date, task.completed, task.overdue]
        task_attr_expected = ['pay the bill', np.datetime64(date.today()),
                               False, False]
        self.assertEqual(task_attr, task_attr_expected)
        self.assertTrue(np.isnat(task.deadline))
        self.assertTrue(np.isnat(task.days_left))

    def test_task_example2(self):
        """
        Function that test whether an instance of Task returns the expected
        default values if

        """
        task = Task(name="pay the bill")
        task_attr = [task.name, task.start_date, task.completed, task.overdue]
        task_attr_expected = ['pay the bill', np.datetime64(date.today()),
                               False, False]
        self.assertEqual(task_attr, task_attr_expected)
        self.assertTrue(np.isnat(task.deadline))
        self.assertTrue(np.isnat(task.days_left))


if __name__ == '__main__':
    unittest.main()
