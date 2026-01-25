import math


def rotate_image(matrix):
    """
    Leetcode 48
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    end = len(matrix)

    for front in range(0, end // 2):
        end = end - 1

        for offset in range(0, int(math.ceil(end + 1 / 2)) - front):
            if len(matrix[offset]) != len(matrix):
                raise ValueError("Matrix must be square.")

            (
                matrix[front][front + offset],
                matrix[end - offset][front],
                matrix[end][end - offset],
                matrix[front + offset][end],
            ) = (
                matrix[end - offset][front],
                matrix[end][end - offset],
                matrix[front + offset][end],
                matrix[front][front + offset],
            )

        front = front - 1
