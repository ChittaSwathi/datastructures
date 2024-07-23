from collections import deque


def keys_and_rooms_841_bfs(rooms):
    """There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
    Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
    
    When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, 
    denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
    
    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
    return true if you can visit all the rooms, or false otherwise.
    
    Example 1:
    -----------
    Input: rooms = [[1],[2],[3],[]]
    Output: true
    Explanation: 
    We visit room 0 and pick up key 1.
    We then visit room 1 and pick up key 2.
    We then visit room 2 and pick up key 3.
    We then visit room 3.
    Since we were able to visit every room, we return true.
    
    Example 2:
    -----------
    Input: rooms = [[1,3],[3,0,1],[2],[0]]
    Output: false
    Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
     
    Constraints:
    ------------
    n == rooms.length
    2 <= n <= 1000
    0 <= rooms[i].length <= 1000
    1 <= sum(rooms[i].length) <= 3000
    0 <= rooms[i][j] < n
    All the values of rooms[i] are unique.
    """
    visited = {0}
    q = deque([0])
    while q:
        curr = q.popleft()

        for i in rooms[curr]:
            if i not in visited:
                q.append(i)
                visited.add(i)
    return len(visited) == len(rooms)

def keys_and_rooms_841_dfs(rooms):
    visited = set()
    def dfs(source, visited):
        if source in visited: return
        visited.add(source)
        for i in rooms[source]:
            dfs(i, visited)

    dfs(source=0, visited=visited)
    return len(rooms) == len(visited)


def rotting_oranges_504_bfs(grid):
    """
    You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.
    If this is impossible, return -1.


    Example 1:
    ----------
    Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4

    Example 2:
    ---------
    Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

    Example 3:
    ---------
    Input: grid = [[0,2]]
    Output: 0
    Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


    Constraints:
    ------------
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.
    """

    minutes = 0
    fresh = 0
    q = deque()
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                q.append((i, j))  # indices of rotten

    while q and fresh:
        for each in range(len(q)): #to cover all corresponding rotten ones
            cr, cc = q.popleft()
            for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dr, dc = cr + r, cc + c
                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1: #range check
                    grid[dr][dc] = 2
                    fresh -= 1
                    q.append((dr, dc))
        minutes += 1
    return minutes if not fresh else -1


def nearest_exit_from_entrance_in_maze_1926(maze, entrance):
    """
    You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and
    walls (represented as '+'). You are also given the entrance of the maze,
    where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

    In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall,
    and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance.
    An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

    Return the number of steps in the shortest path from the entrance to the nearest exit,
    or -1 if no such path exists.

    Example 1:
    ----------
    Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
    Output: 1
    Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
    Initially, you are at the entrance cell [1,2].
    - You can reach [1,0] by moving 2 steps left.
    - You can reach [0,2] by moving 1 step up.
    It is impossible to reach [2,3] from the entrance.
    Thus, the nearest exit is [0,2], which is 1 step away.

    Example 2:
    ----------
    Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
    Output: 2
    Explanation: There is 1 exit in this maze at [1,2].
    [1,0] does not count as an exit since it is the entrance cell.
    Initially, you are at the entrance cell [1,0].
    - You can reach [1,2] by moving 2 steps right.
    Thus, the nearest exit is [1,2], which is 2 steps away.

    Example 3:
    ----------
    Input: maze = [[".","+"]], entrance = [0,0]
    Output: -1
    Explanation: There are no exits in this maze.

    Constraints:
    ------------
    maze.length == m
    maze[i].length == n
    1 <= m, n <= 100
    maze[i][j] is either '.' or '+'.
    entrance.length == 2
    0 <= entrancerow < m
    0 <= entrancecol < n
    entrance will always be an empty cell.
    """
    rows, cols = len(maze), len(maze[0])
    q = deque()
    q.append(entrance)
    maze[entrance[0]][entrance[1]] = '+'
    level = 1

    while q:
        for i in range(len(q)):
            cr, cc = q.popleft()
            for r, c in [(0,1), (0,-1), (1,0), (-1,0)]:
                dr, dc = r+cr, c+cc

                # maze edges
                if dr==0 or dr==rows-1 or dc==0 or dc==cols-1:
                    return level

                # outbound or wall(+)
                elif maze[dr][dc]=='+' or dr<0 or dr>=rows or dc<0 or dc>=cols:
                    continue

                q.append((dr,dc))
                maze[dr][dc] = '+'
        level += 1

    return -1


def number_of_islands_200(grid):
    """
    Given an m x n 2D binary grid, which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Example 1:
    ------------
    Input: grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    Output: 1

    Example 2:
    ------------
    Input: grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    Output: 3

    Constraints:
    --------------
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
    """
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def dfs(r, c):
        nonlocal islands, rows, cols, grid
        if r >= rows or r < 0 or c < 0 or c >= cols or grid[r][c] != '1':
            return

        grid[r][c] = '*'
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            dfs(r + dr, c + dc)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                islands += 1
                dfs(row, col)
    return islands
