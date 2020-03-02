import numpy as np


def ex_1():
    return np.arange(3 * 4 * 5).reshape(3, 4, 5)


def ex_2(arr):
    return np.where(arr%2 == 0)


def ex_3(n):
    result = np.eye(n+1)
    for i in range(1, n+1):
        result[i, :] = result[i-1, :] + np.concatenate((np.array([0]), result[i-1, :-1]))
    return result


def ex_4(A, B):
    return np.dot(np.linalg.inv(A), B)


def ex_5():
    arr = np.load('../data/data.npy')
    arr = arr ** 2
    np.save('../data/data_squared.npy', arr)

