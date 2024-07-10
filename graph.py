from collections import deque

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