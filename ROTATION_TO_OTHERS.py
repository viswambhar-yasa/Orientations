import math as m
import numpy as np
from numpy import linalg as LA


def om2eu(rm):
    if abs(rm[2, 2]) == 1:
        A1 = np.rad2deg(m.atan2(rm[0, 1], rm[0, 0]))
        A2 = 0
        A3 = 0
        eu = [A1, A2, A3]
    else:
        s = 1 / np.sqrt((1 - (rm[2, 2]) ** 2))
        A2 = abs(np.rad2deg(m.acos(rm[2, 2])))
        A1 = abs(np.rad2deg(m.atan2((rm[2, 0] * s), (-rm[2, 1] * s))))
        A3 = abs(np.rad2deg(m.atan2((rm[0, 2] * s), (rm[1, 2] * s))))
        # if A1 + A3 > np.rad2deg(m.pi):
        #    A3 = np.rad2deg(m.pi) - A1
        # else:
        #    A3
        eu = [A1, A2, A3]
    return eu


def om2ax(rm):
    trace = (rm[0, 0] + rm[1, 1] + rm[2, 2])
    omega = np.rad2deg(m.acos(0.5 * (trace - 1)))
    if omega == 0:
        ax = [0, 0, 1, 0]
    else:
        P = 1
        n = m.sqrt((rm[2, 1] - rm[1, 2]) ** 2 + (rm[0, 2] - rm[2, 0]) ** 2 + (rm[1, 0] - rm[0, 1]) ** 2)
        if n == 0:
            x = ((rm[1, 2]) - (rm[2, 1]))
            y = ((rm[2, 0]) - (rm[0, 2]))
            z = ((rm[0, 1]) - (rm[1, 0]))
            ax = [P * x, P * y, P * z, omega]
        else:
            x = ((rm[1, 2]) - (rm[2, 1])) / n
            y = ((rm[2, 0]) - (rm[0, 2])) / n
            z = ((rm[0, 1]) - (rm[1, 0])) / n
            ax = [P * x, P * y, P * z, omega]
    return np.round(ax, 5)


def om2qu(rm):
    qo = 0.5 * m.sqrt(1 + rm[0, 0] + rm[1, 1] + rm[2, 2])
    P = -1
    if rm[2, 1] < rm[1, 2]:
        q1 = -0.5 * P * m.sqrt(1 + rm[0, 0] - rm[1, 1] - rm[2, 2])
    else:
        q1 = 0.5 * P * m.sqrt(1 + rm[0, 0] - rm[1, 1] - rm[2, 2])
    if rm[0, 2] < rm[2, 0]:
        q2 = -0.5 * P * m.sqrt(1 - rm[0, 0] + rm[1, 1] - rm[2, 2])
    else:
        q2 = 0.5 * P * m.sqrt(1 - rm[0, 0] + rm[1, 1] - rm[2, 2])
    if rm[1, 0] < rm[0, 1]:
        q3 = -0.5 * P * m.sqrt(1 - rm[0, 0] - rm[1, 1] + rm[2, 2])
    else:
        q3 = 0.5 * P * m.sqrt(1 - rm[0, 0] - rm[1, 1] + rm[2, 2])
    q = [qo, q1, q2, q3]
    qn = np.linalg.norm(q)
    qu = q / qn
    return qu


rotation_matrix = np.array([(0, 0, 1),
                            (-1, 0, 0),
                            (0, -1, 0)])
print(rotation_matrix)
euler_angles = om2eu(rotation_matrix)
print(euler_angles)

axis_angle_pair = om2ax(rotation_matrix)
print(axis_angle_pair)

quaternion = om2qu(rotation_matrix)
print(quaternion)
