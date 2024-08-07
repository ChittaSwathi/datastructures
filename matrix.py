def set_matrix_zeroes_73(matrix):
    """Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
    You must do it in place.

    Example 1:
    ------------
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Example 2:
    --------------
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    Constraints:
    ----------------
    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

    Follow up:
    -------------
    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?"""
    rows = len(matrix)
    cols = len(matrix[0])
    rows_index = set()
    cols_index = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rows_index.add(i)
                cols_index.add(j)

    for i in rows_index:
        matrix[i] = [0] * cols

    for j in cols_index:
        for i in range(rows):
            matrix[i][j] = 0




