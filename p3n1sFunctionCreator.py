CENTER_POSITION_X = 0
CENTER_POSITION_Y = 0
BALL_SIZE = 0
PEN_IS_LENGTH = 0
TRAJECTORY = False
TRAJECTORY_MAX_Y = 0
TRAJECTORY_MAX_SIZE = 0
left_circle_center_x = 0
right_circle_center_x = 0
circle_top_y = 0
top_circle_center_y = 0
square_of_size = 0
BALL_STYLE = 0
TRAJECTORY_STYLE = 0


def simplifier(text):
    return text.replace("-0.0 ", "").replace("+0.0 ", "").replace("--", "+").replace("(x)", "x").replace("(y)", "y").replace("+-", "-")


def ballStyleFullCircle():
    return f"""[].
            (x-{left_circle_center_x})^2+(y-{CENTER_POSITION_Y})^2={square_of_size}
            [].
            (x-{right_circle_center_x})^2+(y-{CENTER_POSITION_Y})^2={square_of_size}
            """


def ballStyleHalfCircle():
    return f"""[].
            (x-{left_circle_center_x})^2+(y-{CENTER_POSITION_Y})^2={square_of_size}+0*sqrt(-x+{left_circle_center_x})
            [].
            (x-{right_circle_center_x})^2+(y-{CENTER_POSITION_Y})^2={square_of_size}+0*sqrt(x-{right_circle_center_x})
            """


def main_part():
    return f"""[].
            x={left_circle_center_x}+0*sqrt(y-{circle_top_y})*sqrt({top_circle_center_y}-y)
            [].
            x={right_circle_center_x}+0*sqrt(y-{circle_top_y})*sqrt({top_circle_center_y}-y)
            [].
            0*sqrt(y-{top_circle_center_y})+(x-{CENTER_POSITION_X})^2+(y-{top_circle_center_y})^2={square_of_size}
            """


def trajectoryStyleQuadratic():
    return f"""[].
            {top_circle_center_y + BALL_SIZE + TRAJECTORY_MAX_Y}>y>{TRAJECTORY_MAX_SIZE}x^2-{2 * TRAJECTORY_MAX_SIZE * CENTER_POSITION_X}x+{top_circle_center_y + BALL_SIZE + TRAJECTORY_MAX_SIZE * CENTER_POSITION_X * CENTER_POSITION_X}
            """


def trajectoryStyleLine():
    return f"""[].
            {top_circle_center_y + BALL_SIZE + TRAJECTORY_MAX_Y}>y>{TRAJECTORY_MAX_SIZE}|x-{CENTER_POSITION_X}|+{top_circle_center_y + BALL_SIZE}
            """


if __name__ == '__main__':
    CENTER_POSITION_X = float(input("center x:"))
    CENTER_POSITION_Y = float(input("center y:"))
    BALL_STYLE = int(input("ball style(0->full,1->half):"))
    BALL_SIZE = float(input("size:"))
    PEN_IS_LENGTH = float(input("length:"))

    TRAJECTORY = bool(float(input("with trajectory?(1->yes,0->no):")))
    if TRAJECTORY:
        TRAJECTORY_STYLE = int(input("trajectory style(0->quadratic,1->line):"))
        TRAJECTORY_MAX_Y = float(input("trajectory max y:"))
        TRAJECTORY_MAX_SIZE = abs(float(input("trajectory max size:")))

    left_circle_center_x = CENTER_POSITION_X - BALL_SIZE
    right_circle_center_x = CENTER_POSITION_X + BALL_SIZE
    circle_top_y = CENTER_POSITION_Y + BALL_SIZE
    top_circle_center_y = CENTER_POSITION_Y + BALL_SIZE + PEN_IS_LENGTH
    square_of_size = BALL_SIZE * BALL_SIZE

    print(simplifier((ballStyleFullCircle() if BALL_STYLE == 0 else ballStyleHalfCircle()) + main_part() + (trajectoryStyleQuadratic() if TRAJECTORY_STYLE == 0 else trajectoryStyleLine())))
