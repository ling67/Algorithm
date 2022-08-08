import collections
from typing import List

class Solution(object):
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q = collections.deque([start])
        visited = set()
        visited.add((start[0], start[1]))
        while q:
            i, j = q.popleft()
            if i == destination[0] and j == destination[1]:
                return True
            for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                ni, nj = i + di, j + dj
                while 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and not maze[ni][nj]:
                    ni, nj = ni + di, nj + dj
                ni, nj = ni - di, nj - dj
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    q.append((ni, nj))
        return False

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
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [4, 4]
    print("Test case 1 output:", solution.hasPath(maze, start, destination))

    # Test case 2:
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
        0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    start = [0, 4]
    destination = [3, 2]
    print("Test case 2 output:", solution.hasPath(maze, start, destination))

    # Test case 3:
    maze = [[0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 0, 0]]
    start = [4, 3]
    destination = [0, 1]
    print("Test case 3 output:", solution.hasPath(maze, start, destination))


if __name__ == "__main__":
    main()
