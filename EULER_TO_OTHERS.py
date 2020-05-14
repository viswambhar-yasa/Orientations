import math as m
import numpy as np


# main function which return the transformation matrix
def eu2om(angle):  # axis):
    A = np.zeros((3, 3))
    c1 = np.cos(angle[0])
    s1 = np.sin(angle[0])
    c2 = np.cos(angle[2])
    s2 = np.sin(angle[2])
    c = np.cos(angle[1])
    s = np.sin(angle[1])

    A[0][0] = (c1 * c2) - (s1 * c * s2)
    A[0][1] = (s1 * c2) + (c1 * c * s2)
    A[0][2] = s * s2
    A[1][0] = (-c1 * s2) - (s1 * c * c2)
    A[1][1] = (-s1 * s2) + (c1 * c * c2)
    A[1][2] = s * c2
    A[2][0] = s1 * s
    A[2][1] = -c1 * s
    A[2][2] = c
    return A


def eu2ax(angle):
    t = m.tan(angle[1] * 0.5)
    sigma = 0.5 * (angle[0] + angle[2])
    delta = 0.5 * (angle[0] - angle[2])
    tow = np.sqrt((t ** 2) + (m.sin(sigma) ** 2))
    alpha = np.rad2deg(2 * m.atan(tow / np.cos(sigma)))
    C = np.rad2deg(m.pi)
    if angle[0] < m.pi:
        P = -1
    else:
        P = 1
    if tow == 0:
        axis_angle_pair = [(-P * (t * m.cos(delta))),
                           (-P * (t * m.sin(delta))),
                           (-P * (m.sin(m.pi * 0.5 + sigma))),
                           alpha]
    else:
        if alpha <= C:
            axis_angle_pair = [((-P / tow) * (t * m.cos(delta))),
                               ((-P / tow) * (t * m.sin(delta))),
                               ((-P / tow) * (m.sin(sigma))),
                               abs(alpha)]
        else:
            axis_angle_pair = [((P / tow) * (t * m.cos(delta))),
                               ((P / tow) * (t * m.sin(delta))),
                               ((P / tow) * (m.sin(sigma))),
                               abs(2 * C - alpha)]

    return axis_angle_pair


def eu2ro(angle):
    ax_pa = np.round(eu2ax(np.deg2rad(angle)), 5)
    omega = m.tan(np.deg2rad(ax_pa[3]) * 0.5)
    ro = [ax_pa[0], ax_pa[1], ax_pa[2], omega]
    return ro


def eu2ho(angle):
    ax_pair = np.round(eu2ax(np.deg2rad(angle)), 5)
    t = (3 / 4) * (np.deg2rad(ax_pair[3]) - m.sin(np.deg2rad(ax_pair[3])))
    omega = np.power(t, (1 / 3))
    ho = ax_pair[0:3] * omega
    return ho


def eu2qa(angle):
    sigma = 0.5 * (angle[0] + angle[2])
    delta = 0.5 * (angle[0] - angle[2])
    s = m.sin(angle[1] * 0.5)
    c = m.cos(angle[1] * 0.5)
    P=-1
    if c * m.cos(sigma) > 0:
        qa = [c * m.cos(sigma), -P * s * m.cos(delta), -P * s * m.sin(delta), -P * c * m.sin(sigma)]
    else:
        qa = [P*c * m.cos(sigma), P * s * m.cos(delta), P * s * m.sin(delta), P * c * m.sin(sigma)]
    return qa


Ang = [0.0000000, 180.0000000, 0.0000000]


# initializing of rotation matrix
rotation_matrix = np.zeros((3, 3))
rotation_matrix = np.round(eu2om(np.deg2rad(Ang)), 6)
print(rotation_matrix)

axis_angle_pair = np.round(eu2ax(np.deg2rad(Ang)), 5)
print(axis_angle_pair)

rodriguez_frank = np.round(eu2ro(Ang), 5)
print(rodriguez_frank)

homochoric = np.round(eu2ho(Ang), 5)
print(homochoric)

quaternion = np.round(eu2qa(np.deg2rad(Ang)), 5)
print(quaternion)

