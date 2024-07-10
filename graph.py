from collections import deque
import math

def number_of_provinces_547_dfs(isConnected):
    """There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

    A province is a group of directly or indirectly connected cities and no other cities outside of the group.

    You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

    Example 1:
    ----------
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2

    Example 2:
    -----------
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3

    Constraints:
    ------------
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
    """

    n = len(isConnected)
    visited = set()
    provinces = 0

    def dfs(i):
        visited.add(i)
        for j in range(n):  # j cols
            if j not in visited and isConnected[i][j]:
                dfs(j)

    for i in range(n):
        if i not in visited:  # i rows
            dfs(i)
            provinces += 1

    return provinces


def number_of_provinces_547_bfs(isConnected):

    n = len(isConnected)
    visited = set()
    provinces = 0

    def bfs(i):
        visited.add(i)
        q = deque()
        q.append(i)
        while q:
            j = q.popleft()
            for i in range(n):
                if i not in visited and isConnected[i][j]:
                    q.append(i)
                    visited.add(i)

    for i in range(n):
        if i not in visited:  # i rows
            provinces += 1
            bfs(i)

    return provinces


def reorder_routes_to_make_all_paths_lead_to_the_city_zero_1466(n, connections):
    """There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

    Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

    This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

    Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

    It's guaranteed that each city can reach city 0 after reorder.

    Example 1:
    -----------
    Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    Output: 3
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

    Example 2:
    -------------
    Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
    Output: 2
    Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).

    Example 3:
    ------------
    Input: n = 3, connections = [[1,0],[2,0]]
    Output: 0

    Constraints:
    -------------
    2 <= n <= 5 * 104
    connections.length == n - 1
    connections[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi
    """

    edges = {(a, b) for a, b in connections}
    neighbors = {city: [] for city in range(n)}
    visited = set()
    count = 0

    for a, b in connections:
        neighbors[a].append(b)
        neighbors[b].append(a)

    def dfs(city):
        nonlocal edges, neighbors, visited, count

        for neighbor in neighbors[city]:
            if neighbor in visited:
                continue

            if (neighbor, city) not in edges:
                count += 1

            visited.add(neighbor)
            dfs(neighbor)

    visited.add(0)
    dfs(0)
    return count



def evaluate_division_399(equations, values, queries):
    """
    You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

    You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

    Return the answers to all queries. If a single answer cannot be determined, return -1.0.

    Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

    Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

    Example 1:
    ------------
    Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    Explanation:
    Given: a / b = 2.0, b / c = 3.0
    queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
    return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
    note: x is undefined => -1.0

    Example 2:
    -------------
    Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    Output: [3.75000,0.40000,5.00000,0.20000]

    Example 3:
    --------------
    Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
    Output: [0.50000,2.00000,-1.00000,-1.00000]

    Constraints:
    -----------------
    1 <= equations.length <= 20
    equations[i].length == 2
    1 <= Ai.length, Bi.length <= 5
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
    queries[i].length == 2
    1 <= Cj.length, Dj.length <= 5
    Ai, Bi, Cj, Dj consist of lower case English letters and digits.
    """

    def dfs(edges, source, target, visited):
        if (source not in edges) or (source in visited): return math.inf
        visited.add(source)
        if source == target: return 1  # edge case

        for node in edges[source]:
            print('node', node)
            d = dfs(edges, node[0], target, visited)
            if d != math.inf: return d * node[1]  # multiply with old distance to get new distance
        return math.inf

    edges = {}
    res = []

    for index, eqn in enumerate(equations):
        if eqn[0] not in edges: edges[eqn[0]] = []
        if eqn[1] not in edges: edges[eqn[1]] = []

        edges[eqn[0]].append([eqn[1], values[index]]) #add one -way : ex: a->b
        edges[eqn[1]].append([eqn[0], 1 / values[index]]) #add reverse: ex: b->a and value wll be 1/value

    for q in queries:
        d = dfs(edges, q[0], q[1], set())
        if d == math.inf:
            res.append(-1)
        else:
            res.append(d)

    return res