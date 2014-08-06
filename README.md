Bubble Blast 3D Solver
======================

Solves levels for Bubble Blast 3D (com.magmamobile.game.BubbleBlast3D) game on Android.

Usage:
------
```python
>>> solveboard('4444413243341432.42.34.12.2324', 5, 3)
ROW COL BOARD
        |44444|13243|34143|2.42.|34.12|.2324|
2   1   |44444|23243|34143|2.42.|34.12|.2324|   ::4444423243341432.42.34.12.2324
3   5   |44444|23243|34144|2.42.|34.12|.2324|   ::4444423243341442.42.34.12.2324
3   4   |.....|.....|.....|.....|.....|.....|   ::..............................
```
Enter board as a string, top to bottom, left to right. Use period (`.`) for empty space, numbers for bubble sizes. Use numbers `1` (smallest, blue), `2` (yellow), `3` (green) and `4` (largest, red) for bubble state.


See also:
---------

My [Flow game solver](https://github.com/lacop/FlowSolver) source on GitHub. That one uses SAT solver (this one is just plain bruteforce since the state space is small enough).

