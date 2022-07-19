from typing import List

class Solution:
    EMPTY = 0
    WALL = 1

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def dfs(curr_i, curr_j):
            if [curr_i, curr_j] == destination:
                return True

            for delta_i, delta_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_i, next_j = curr_i, curr_j
                while 0 <= next_i + delta_i < m and 0 <= next_j + delta_j < n and maze[next_i + delta_i][next_j + delta_j] == self.EMPTY:
                    next_i += delta_i
                    next_j += delta_j

                if (next_i, next_j) not in visited:
                    visited.add((next_i, next_j))
                    if dfs(next_i, next_j):
                        return True
            return False

        m, n = len(maze), len(maze[0])
        visited = set()
        return dfs(start[0], start[1])


def main():
    solution = Solution()

    # Test case 0:
    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [2, 2]
    print("Test case 0 output:", solution.hasPath(maze, start, destination))

    # Test case 1:
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    print("Test case 1 output:", solution.hasPath(maze, start, destination))

    # Test case 2:
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [3, 2]
    print("Test case 2 output:", solution.hasPath(maze, start, destination))

    # Test case 3:
    maze = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
    start = [4, 3]
    destination = [0, 1]
    print("Test case 3 output:", solution.hasPath(maze, start, destination))

if __name__ == "__main__":
    main()
