import math as m
import numpy as np


def ax2om(apv):
    omega = np.deg2rad(apv[3])
    c = m.cos(omega)
    s = m.sin(omega)
    om11 = c + ((1 - c) * ((apv[0]) ** 2))
    om12 = ((1 - c) * ((apv[0]) * (apv[1]))) + s * (apv[2])
    om13 = ((1 - c) * ((apv[0]) * (apv[2]))) - s * (apv[1])
    om22 = c + ((1 - c) * ((apv[1]) ** 2))
    om21 = ((1 - c) * ((apv[0]) * (apv[1]))) - s * (apv[2])
    om23 = ((1 - c) * ((apv[1]) * (apv[2]))) + s * (apv[0])
    om33 = c + ((1 - c) * ((apv[2]) ** 2))
    om31 = ((1 - c) * ((apv[0]) * (apv[1]))) + s * (apv[2])
    om32 = ((1 - c) * ((apv[1]) * (apv[2]))) - s * (apv[0])

    om = np.array([(om11, om12, om13), (om21, om22, om23), (om31, om32, om33)])
    return np.round(om, 5)


axis_angle_pair = [0.5773503, -0.5773503, 0.5773503, 120.000]
print(axis_angle_pair)
rotation_matrix = ax2om(axis_angle_pair)
print(rotation_matrix)


def ax2ro(apv):
    omega = m.tan(np.deg2rad(apv[3]) * 0.5)
    n = np.sqrt((apv[0] ** 2) + (apv[1] ** 2) + (apv[2] ** 2))
    x = apv[0] * m.tan(np.deg2rad(apv[3]) * 0.5) / n  # error
    y = apv[1] * m.tan(np.deg2rad(apv[3]) * 0.5) / n
    z = apv[2] * m.tan(np.deg2rad(apv[3]) * 0.5) / n

    ro = [x, y, z, omega]
    return ro


rodriguez_frank = ax2ro(axis_angle_pair)
print(rodriguez_frank)


def ax2qu(apv):
    qo = m.cos(np.deg2rad(apv[3]) * 0.5)
    n = np.sqrt((apv[0] ** 2) + (apv[1] ** 2) + (apv[2] ** 2))
    q1 = apv[0] * m.sin(np.deg2rad(apv[3]) * 0.5) / n
    q2 = apv[1] * m.sin(np.deg2rad(apv[3]) * 0.5) / n
    q3 = apv[2] * m.sin(np.deg2rad(apv[3]) * 0.5) / n

    q = [qo, q1, q2, q3]
    return np.round(q, 5)


quaternion = ax2qu(axis_angle_pair)
print(quaternion)


def ax2ho(apv):
    t = (3 / 4) * (np.deg2rad(apv[3]) - m.sin(np.deg2rad(apv[3])))
    f = np.power(t, (1 / 3))
    x = apv[0] * f
    y = apv[1] * f
    z = apv[2] * f

    ho = [x, y, z]
    return ho


homochoric = ax2ho(axis_angle_pair)
print(homochoric)
