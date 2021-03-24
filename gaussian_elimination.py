import numpy as np


class Error(Exception):
    """Base class for other exceptions"""
    pass


class IncompatibleSizes(Error):
    def __init__(self, matrix_A, vector_b, message="Incompatible sizes between matrix A and vector b"):
        self.matrix_A_ = matrix_A
        self.vector_b_ = vector_b
        self.message_ = message
        super().__init__(self.message_)

    def __str__(self):
        return f'{self.message_} -> size of A = {len(self.matrix_A_)}, size of b = {self.vector_b_.size}'


class NotNonSingular(Error):
    def __init__(self, message="Matrix A is singular, no more calculations..."):
        self.message_ = message
        super().__init__(self.message_)

    def __str__(self):
        return f'{self.message_}'


def GE(A_, b_):
    """
    Gaussian elimination with pivoting strategy

    inputs: A_ - Matrix: np.array
            b_ - Absolute term in an expression: np.array

    outputs: x_ - Solution of Ax=b

    Comments: 1. If any of the elements on the diagonal is equal to 0, we rearrange the rows (if the matrix is
        non-singular), and:
        2. If any of the elements on the diagonal is small compared to other elements, we rearrange the rows and columns
        if it's necessary.

    Script with necessary knowledge (polish): https://rperlinski.pl/strona/files/mn/d03_UkladyRownanLiniowychI.pdf ,
        chapter: 4.3
    """

    if b_.size != len(A_):
        raise IncompatibleSizes(A_, b_)

    # First and second condition from above Comments
    for k in range(len(A_) - 1):  # k shows current pivot row
        if np.linalg.det(A_) != 0:  # checking if matrix is non-singular
            max_index = abs(A_[k:, k]).argmax() + k  # finding abs(max value) of index
            if max_index != k:
                # swap the rows in matrix A and vector b
                A_[[k, max_index]] = A_[[max_index, k]]
                b_[[k, max_index]] = b_[[max_index, k]]
        else:
            raise NotNonSingular

    # Elimination
    for k in range(len(A_) - 1):
        for t in range(k + 1, len(A_)):
            temp = -(A_[t, k] / A_[k, k])
            A_[t, k:] = A_[t, k:] + temp * A_[k, k:]
            b_[t] = b_[t] + temp * b_[k]

    # Back substitution (From x_n to x_1)
    x = np.zeros(len(A_))
    for k in range(len(A_) - 1, -1, -1):
        x[k] = (b_[k] - (A_[k, k + 1:] @ x[k + 1:])) / A_[k, k]

    return x


if __name__ == "__main__":
    pass

