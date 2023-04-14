from time import perf_counter

import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def convex_bucket(points: NDArray) -> NDArray:
    """Complexity: O(n log n)"""
    clockwise_sorted_ch = []
    points = sorted(points, key=lambda p: (p[0], p[1]))

    clockwise_sorted_ch.append(points[0])
    clockwise_sorted_ch.append(points[1])

    for point in points[2:]:
        while len(clockwise_sorted_ch) > 1 and not is_clockwise(clockwise_sorted_ch[-2], clockwise_sorted_ch[-1], point):
            del clockwise_sorted_ch[-1]
        clockwise_sorted_ch.append(point)

    return np.array(clockwise_sorted_ch)


def is_clockwise(p1: NDArray, p2: NDArray, p3: NDArray) -> bool:
    area = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    return area > 0


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"practicum_5/homework/points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_points(points, convex_hull=ch, markersize=20)
        print()
