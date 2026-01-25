import copy
import pytest
from rotate_image import rotate_image

def is_rotated_90_clockwise(original, rotated):
    """Check if rotated is original rotated 90° clockwise."""
    n = len(original)
    return all(rotated[j][n - 1 - i] == original[i][j] for i in range(n) for j in range(n))

@pytest.mark.parametrize(
    "matrix",
    [
        [[1]],

        [[1, 2],
         [3, 4]],

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],

        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]],

        [[-1, -2, -3],
         [-4, -5, -6],
         [-7, -8, -9]],

        [[1, 1, 1],
         [1, 2, 1],
         [1, 1, 1]],

        [[5, 1, 9],
         [2, 4, 8],
         [13, 3, 6]],

        [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]],
    ]
)
def test_rotate_image(matrix):
    original = copy.deepcopy(matrix)
    result = rotate_image(matrix)

    # Check that function modifies in-place
    assert result is None

    # Check that the matrix is correctly rotated 90° clockwise
    assert is_rotated_90_clockwise(original, matrix)
