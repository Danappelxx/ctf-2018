jam_initial_pos = (2,3)
you_initial_pos = (10,20)
exit_pos = (24,15)

def gen_path(point_from, point_to):
    steps = []
    while point_from != point_to:

        # randomly swap from moving up/down and left/right
        if bool(random.getrandbits(1)):

            # from-x -> to-x, then go left
            if point_from[0] - point_to[0] > 0:
                point_from = (point_from[0] - 1, point_from[1])
            elif point_from[0] - point_to[0] < 0:
                point_from = (point_from[0] + 1, point_from[1])
            else:
                continue

        else:
            # from-y -> to-y, then go down
            if point_from[1] - point_to[1] > 0:
                point_from = (point_from[0], point_from[1] - 1)
            elif point_from[1] - point_to[1] < 0:
                point_from = (point_from[0], point_from[1] + 1)
            else:
                continue

        steps.append(point_from)

    return steps

def is_valid(path):
    all_points = []
    previous = None

    for point in path:

        if point in all_points:
            return False
        else:
            all_points.append(point)

        if previous is None:
            previous = point
            continue
        dX = abs(previous[0] - point[0])
        dY = abs(previous[1] - point[1])

        if (dX == 1 and dY == 0) or (dX == 0 and dY == 1):
            pass
        else:
            print(previous, point, dX, dY)
            return False

        previous = point

    return True

def check_correct(j_path, y_path):
    # first make sure that the path is legal
    if not is_valid(y_path):
        return False

    # next check
    num_steps = len(y_path)
    return j_path[num_steps - 1] == y_path[-1]

def parse(input):
    # TODO: implement
    return []
