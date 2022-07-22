# Maze-project

## Description

#### Definition

* A maze is a path or collection of paths, typically from an entrance to a goal. 
<img width="300" alt="image" src="https://user-images.githubusercontent.com/93315926/179809703-0d5fb530-163c-49a9-8e10-f05d00b8ccee.png">

#### [Maze Type]()

There are four type of maze:
1. Clear Route(Street, Highway): there are clear route in graph and there are less empty space in graph.
   * without wheel
   * with wheel
   
2. Unclear Route(Hotel, Hospital) : there are no clear route in graph and there are more empty space in graph.
   * without wheel
   * with wheel

**we only fucus on Clear Route without wheel and Unclear Route with with wheel. It more normal in real word.**

#### [Maze Direction]()
* A people starts at a position (source) and can move in four directions, the goal is to reach the destination:
  * Up
  * Down
  * Left
  * Right

* Direction Priority:  Right, Left, Up, Down <br>

* Graph Theory - Solve a Maze (vedio): [Graph Theory](https://www.youtube.com/watch?v=DDPdnywfxuM)

## Design

#### [Clear Route Maze]()

> Key point: thinking find the path between two point in a graph.

* Step 1: Study the picture below until you understand how a maze can be converted into a graph.
* Step 2: Use DFS to find the path between two position.

<img width="800" alt="image" src="https://user-images.githubusercontent.com/93315926/179808769-9a305917-e1c9-4a9a-baad-cdb129e2a7f9.png">

#### [Unclear Route Maze]()

Find a route from 0 -> 1:  <br>

<img width="200" alt="image" src="https://user-images.githubusercontent.com/93315926/180577497-e72e98bd-bbd4-43ad-87c9-e96c86a0845a.png">

* Solution: DFS in Matrix

## Related Theory

* Tree     [Tree Explaination](https://www.geeksforgeeks.org/binary-tree-data-structure/?ref=gcse)
* Graph    [Graph Explaination](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/?ref=gcse) 
* Depth-First-Search      [DFS Explaination](https://brilliant.org/wiki/depth-first-search-dfs/#complexity-of-depth-first-search)
* Breadth-First-Search      [BFS Explaination](https://www.youtube.com/watch?v=xlVX7dXLS64) 

## How to run project

```python
Step 1: download maze-DFS.py file
Step 2: python3 maze-DFS.py
```

## Detail Design Presentation
[CS501_19632_MazeProject_Ling_Chen](https://docs.google.com/presentation/d/1v43LjrhdWu0MIY3CdU9H1Uvo751W0iz4zujG_3AcO-s/edit?usp=sharing)
