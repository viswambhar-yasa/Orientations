import math as m
import numpy as np


def qu2eu(q):
    q03 = q[0] ** 2 + q[3] ** 2
    q12 = q[1] ** 2 + q[2] ** 2
    xi = np.sqrt(q03 * q12)
    P = -1
    if float(xi) == 0 & float(q12) == 0:
        A1 = np.rad2deg(m.atan2(-2 * P * q[0] * q[3], q[0] ** 2 - q[3] ** 2))
        A2 = 0
        A3 = 0
    elif float(xi) == 0 & float(q03) == 0:
        A1 = np.rad2deg(m.atan2(2 * P * q[0] * q[2], q[0] ** 2 - q[2] ** 2))
        A2 = np.rad2deg(m.pi)
        A3 = 0
    else:
        A1 = np.rad2deg(m.atan2(((q[1] * q[3] - P * q[0] * q[2]) / xi), ((-P * q[0] * q[1] - q[2] * q[3]) / xi)))
        A2 = np.rad2deg(m.atan2(2 * xi, q03 - q12))
        A3 = np.rad2deg(m.atan2(((P * q[0] * q[2] + q[1] * q[3]) / xi), ((q[2] * q[3] - P * q[0] * q[1]) / xi)))
    eu = [A1, A2, A3]
    return eu


quaternion = [0.0000000, 0.7071068, -0.7071068, 0.00000000]
print(quaternion)
euler_angles = qu2eu(quaternion)
print(euler_angles)


def qu2om(q):
    qt = q[0] ** 2 - (q[1] ** 2 + q[2] ** 2 + q[3] ** 2)
    P = -1
    om11 = qt + 2 * q[1] ** 2
    om12 = 2 * (q[1] * q[2] - P * q[0] * q[3])
    om13 = 2 * (q[1] * q[3] + P * q[0] * q[2])
    om22 = qt + 2 * q[2] ** 2
    om21 = 2 * (q[1] * q[2] + P * q[0] * q[3])
    om23 = 2 * (q[2] * q[3] - P * q[0] * q[1])
    om33 = qt + 2 * q[3] ** 2
    om31 = 2 * (q[1] * q[3] - P * q[0] * q[2])
    om32 = 2 * (q[2] * q[3] + P * q[0] * q[1])
    om = np.array([(om11, om12, om13),
                   (om21, om22, om23),
                   (om31, om32, om33)])
    return om


rotation_matrix = qu2om(quaternion)
print(rotation_matrix)
