CENTER_POSITION_X = 0
CENTER_POSITION_Y = 0
BALL_SIZE = 0
PEN_IS_LENGTH = 0
TRAJECTORY = False
TRAJECTORY_MAX_Y = 0
TRAJECTORY_MAX_SIZE = 0


def replaceText(text):
    return text.replace("-0.0 ", "").replace("+0.0 ", "").replace("--", "+").replace(" )", ")").replace("(x)",
                                                                                                        "x").replace(
        "(y)", "y")


def final_result_0():
    return replaceText(f"""
            1.
            (x-{CENTER_POSITION_X - BALL_SIZE} )^2+(y-{CENTER_POSITION_Y} )^2={BALL_SIZE * BALL_SIZE}
            2.
            (x-{CENTER_POSITION_X + BALL_SIZE} )^2+(y-{CENTER_POSITION_Y} )^2={BALL_SIZE * BALL_SIZE}
            3.
            x={CENTER_POSITION_X - BALL_SIZE}+0*sqrt((y-{CENTER_POSITION_Y + BALL_SIZE} )*({CENTER_POSITION_Y + BALL_SIZE + PEN_IS_LENGTH}-y ))
            4.
            x={CENTER_POSITION_X + BALL_SIZE}+0*sqrt((y-{CENTER_POSITION_Y + BALL_SIZE} )*({CENTER_POSITION_Y + BALL_SIZE + PEN_IS_LENGTH}-y ))
            5.
            0*sqrt(y-{CENTER_POSITION_Y + BALL_SIZE + PEN_IS_LENGTH} )+(x-{CENTER_POSITION_X} )^2+(y-{CENTER_POSITION_Y + BALL_SIZE + PEN_IS_LENGTH} )^2={BALL_SIZE * BALL_SIZE}
            """)


def final_result_1():
    return replaceText(f"""6.
            {CENTER_POSITION_Y + PEN_IS_LENGTH + BALL_SIZE * 2 + TRAJECTORY_MAX_Y}>y>{TRAJECTORY_MAX_SIZE}x^2-{2 * TRAJECTORY_MAX_SIZE * CENTER_POSITION_X}x+{CENTER_POSITION_Y + PEN_IS_LENGTH + BALL_SIZE * 2 + TRAJECTORY_MAX_SIZE * CENTER_POSITION_X * CENTER_POSITION_X}
            """)


if __name__ == '__main__':
    CENTER_POSITION_X = float(input("center x:"))
    CENTER_POSITION_Y = float(input("center y:"))
    BALL_SIZE = float(input("size:"))
    PEN_IS_LENGTH = float(input("length:"))

    TRAJECTORY = bool(float(input("with trajectory?(1->yes,0->no):")))
    TRAJECTORY_MAX_Y = float(input("trajectory max y:"))
    TRAJECTORY_MAX_SIZE = abs(float(input("trajectory max size:")))

    print(final_result_0() + ("" if not TRAJECTORY else final_result_1()))
