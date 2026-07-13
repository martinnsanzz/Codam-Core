# A-Maze-ing: Research

## Maze generation alghorithms

[Visual and extended explanation](https://professor-l.github.io/mazes/)

**DFS** (Depth First Search / Back tracking maze):

- Generates a maze by treating the grid as a graph: each cell is a node, walls between cells are edges.
- Uses randomized depth-first search (recursive backtracker) to carve a spanning tree over the grid.
- **Result**: exactly one path between any two cells (perfect maze, no loops, no isolated areas).

<ins>Steps</ins>

1. Pick start cell, mark visited, push onto stack.
2. Loop while stack not empty:
    - Look at current cell (top of stack).
    - Get unvisited neighbors (2 cells away if using wall-grid, 1 cell away if using logical grid + wall bitmask).
    - If unvisited neighbor exists:
        - Pick one at random.
        - Remove wall between current and neighbor.
        - Mark neighbor visited, push onto stack (becomes new current).
    - Else:
        - Pop stack (backtrack).
3. Terminates when stack empties → all reachable cells visited.


**Randomized Kruskal's Alghorithm**:

- Generates a maze by building a minimum spanning tree over the grid graph using randomized edge selection, not DFS traversal.
- Treats each cell as a separate set; repeatedly merges sets by removing walls between cells in different sets, chosen at random.
- Uses Union-Find (Disjoint Set Union) to track connectivity — core difference from DFS approach.

<ins>Steps</ins>

1. Init: each cell is its own set (parent[i] = i).
2. Build list of all walls (edges) between adjacent cells.
3. Shuffle edge list randomly.
4. For each edge (a, b) in shuffled order:
    - If find(a) != find(b): cells are in different sets → remove wall, union_sets(a, b).
    - Else: same set already connected → skip (removing would create a loop).

5. Terminates after processing all edges → single connected set = perfect maze.


## Path finding alghoritms