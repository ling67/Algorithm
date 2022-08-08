# Maze-project

**Problem Define: Determine if we can find the route from the entrance to exit.**

**Maze Define: A maze is a path or collection of paths, typically from an entrance to a goal.**

<img width="200" alt="image" src="https://user-images.githubusercontent.com/93315926/179809703-0d5fb530-163c-49a9-8e10-f05d00b8ccee.png">

This project is an extension of Maze DFS, we use Breadth-First Traversal to solve Maze this problem
* Depth-First Traversal - does not find the Shortest Path
* Breadth-First Traversal - find the Shortest Path

## Idea

* A people starts at a position (source) and can move in four directions, the goal is to reach the destination:
  * Up
  * Down
  * Left
  * Right

* Direction Priority:  Right, Left, Up, Down <br>

In this case, we try to explore the search space on a level by level basis. i.e. We try to move in all the directions at every step. When all the directions have been explored and we still don't reach the destination, then only we proceed to the new set of traversals from the new positions obtained.

## Example: Unclear Route Maze

Find a route from 0 -> 1:  <br>
<img width="200" alt="image" src="https://user-images.githubusercontent.com/93315926/183321709-ac7c1325-16ac-4776-ad68-5bb99213153e.png">

* Solution: BFS in Matrix

## Related Theory

* Tree     [Tree Explaination](https://www.geeksforgeeks.org/binary-tree-data-structure/?ref=gcse)
* Graph    [Graph Explaination](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/?ref=gcse) 
* Depth-First-Search      [DFS Explaination](https://brilliant.org/wiki/depth-first-search-dfs/#complexity-of-depth-first-search)
* Breadth-First-Search      [BFS Explaination](https://www.youtube.com/watch?v=xlVX7dXLS64) 

## How to run project

```python
Step 1: download maze-BFS.py file
Step 2: python3 maze-BFS.py
```

## Detail Design Presentation
[MazeProject_Ling_Chen](https://docs.google.com/presentation/d/1a3wkcgDjNus_sKakGH45NjaS4lMpFmFIOKFqqprLHMc/edit#slide=id.g25f6af9dd6_0_0)
