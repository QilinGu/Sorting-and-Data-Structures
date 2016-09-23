# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    """
    Returns minimum list of points that fall at least once in each provided segment

    :param segments: list of namedtuple objects containing the start and stop points of each segment
    :return: list of points that fall in every segment
    """
    # Sort segments by endpoint
    segments = sorted(segments, key=attrgetter("end"))
    points = [segments[0].end]  # First safe point is last point in first segment

    point_idx = 0
    for line in segments[1:]:
        if line.start > points[point_idx]:
            points.append(line.end)
            point_idx += 1

    return points


def main():
    vals = sys.stdin.read()
    n, *data = map(int, vals.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

if __name__ == '__main__':
    main()
