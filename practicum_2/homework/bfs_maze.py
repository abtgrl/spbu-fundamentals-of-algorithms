from time import perf_counter
from queue import Queue


class Maze:
    def __init__(self, list_view: list[list[str]]) -> None:
        self.list_view = list_view
        self.start_j = None
        for j, sym in enumerate(self.list_view[0]):
            if sym == "O":
                self.start_j = j

    @classmethod
    def from_file(cls, filename):
        list_view = []
        with open(filename, "r") as f:
            for l in f.readlines():
                list_view.append(list(l.strip()))
        obj = cls(list_view)
        return obj

    def valid(self, i: int, j: int, move: str) -> bool:
        i, j = _shift_coordinate(i, j, move)
        if not (0 <= i <= len(self.list_view)) or not (0 <= j <= len(self.list_view[0])):
            return False
        elif self.list_view[i][j] == "#":
            return False
        return True

    def print(self, path="") -> None:
        # Find the path coordinates
        i = 0  # in the (i, j) pair, i is usually reserved for rows and j is reserved for columns
        j = self.start_j
        path_coords = set()
        for move in path:
            i, j = _shift_coordinate(i, j, move)
            path_coords.add((i, j))
        # Print maze + path
        for i, row in enumerate(self.list_view):
            for j, sym in enumerate(row):
                if (i, j) in path_coords:
                    print("+ ", end="")  # NOTE: end is used to avoid linebreaking
                else:
                    print(f"{sym} ", end="")
            print()  # linebreak


def solve(maze: Maze) -> None:
    path = ""  # solution as a string made of "L", "R", "U", "D"
    start_i, start_j = 0, maze.start_j
    q = Queue()
    q.put(path)
    visited = set()
    while not q.empty():
        path = q.get()
        i, j = start_i, start_j
        for move in path:
            i, j = _shift_coordinate(i, j, move)
        if maze.list_view[i][j] == "X":
            break
        if (i, j) not in visited:
            visited.add((i, j))
            for move in ["U", "D", "L", "R"]:
                if maze.valid(i, j, move):
                    q.put(path + move)

    print(f"Found: {path}")
    maze.print(path)


def _shift_coordinate(i: int, j: int, move: str) -> tuple[int, int]:
    if move == "L":
        j -= 1
    elif move == "R":
        j += 1
    elif move == "U":
        i -= 1
    elif move == "D":
        i += 1
    return i, j


if __name__ == "__main__":
    maze = Maze.from_file("practicum_2/homework/maze_2.txt")
    t_start = perf_counter()
    solve(maze)
    t_end = perf_counter()
    print(f"Elapsed time: {t_end - t_start} sec")
