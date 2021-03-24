import unittest
from gaussian_elimination import *
import psutil
import os
import time
import csv


def write_to_file(num, memory_usage_, speed_, logic='FAILED'):
    myFile = 'Results.csv'
    with open(myFile, "r") as f:
        reader = csv.reader(f)
        for header in reader:
            break

    with open(myFile, "a", newline='\n') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writerow({header[0]: num, header[1]: memory_usage_, header[2]: speed_, header[3]: logic})


class GECase(unittest.TestCase):
    def test_1(self):
        A_ = np.array([[0.003, 59.14], [5.291, -6.13]])
        b_ = np.array([[59.17], [46.78]])

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = round((py.memory_info()[0] / 2. ** 30), 8)  # memory use in GB

        start = time.time()
        solution = GE(A_, b_)
        end = time.time()
        speed = round(end - start, 6)  # operating time

        write_to_file(num=1, memory_usage_=memory_usage, speed_=speed, logic='PASSED')
        for pair in zip(solution, [10, 1]):  # [10, 1] is exact solution
            self.assertEqual(pair[0], pair[1])

    def test_2(self):
        A_ = np.array([[1, 4], [2, 0]])
        b_ = np.array([[12], [2]])

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = round((py.memory_info()[0] / 2. ** 30), 8)  # memory use in GB

        start = time.time()
        solution = GE(A_, b_)
        end = time.time()
        speed = round(end - start, 6)  # operating time

        write_to_file(num=2, memory_usage_=memory_usage, speed_=speed, logic='PASSED')
        for pair in zip(solution, [1, 11 / 4]):  # [1, 11/4] is exact solution
            self.assertEqual(round(pair[0], 2), round(pair[1], 2))

    def test_3(self):
        A_ = np.array([[1, 4, 8], [2, 0, 3], [1, 4, 4]])
        b_ = np.array([[15], [2], [5]])

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = round((py.memory_info()[0] / 2. ** 30), 8)  # memory use in GB

        start = time.time()
        solution = GE(A_, b_)
        end = time.time()
        speed = round(end - start, 6)  # operating time

        write_to_file(num=3, memory_usage_=memory_usage, speed_=speed)
        for pair in zip(solution, [-11 / 4, -9 / 16, 5 / 2]):  # [-11/4, -9/16, 5/2] is exact solution
            self.assertEqual(round(pair[0], 2), round(pair[1], 2))

    def test_4(self):
        A_ = np.array([[1, 4, 8, 16], [2, 2, 3, 3], [1, 4, 4, 4], [2, 2, 6, 6]])
        b_ = np.array([[15], [2], [5], [6]])

        pid = os.getpid()
        py = psutil.Process(pid)
        memory_usage = round((py.memory_info()[0] / 2. ** 30), 8)  # memory use in GB

        start = time.time()
        solution = GE(A_, b_)
        end = time.time()
        speed = round(end - start, 6)  # operating time

        write_to_file(num=4, memory_usage_=memory_usage, speed_=speed)
        for pair in zip(solution, [-11 / 9, 2 / 9, 3 / 4, 7 / 12]):  # [-11/9, 2/9, 3/4, 7/12] is exact solution
            self.assertEqual(round(pair[0], 2), round(pair[1], 2))


if __name__ == '__main__':
    unittest.main()
