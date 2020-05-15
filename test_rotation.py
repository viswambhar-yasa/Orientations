import numpy as np
# import pytest as pt

from ROTATION_TO_OTHERS import om2eu
from ROTATION_TO_OTHERS import om2ax
from ROTATION_TO_OTHERS import om2qu


def test_om2eu():
    rotation_matrix = np.round(np.array([(0.0000000, 0.0000000, 1.0000000),
                                         (-1.0000000, 0.0000000, 0.0000000),
                                         (0.0000000, -1.0000000, 0.0000000)]))
    ACTUAL_EU = [0.0000000, 90.0000000, 90.0000000]
    FUN_EU = om2eu(rotation_matrix)
    assert np.all(ACTUAL_EU == FUN_EU)


def test_om2ax():
    rotation_matrix = np.round(np.array([(0.0000000, 0.0000000, 1.0000000),
                                         (-1.0000000, 0.0000000, 0.0000000),
                                         (0.0000000, -1.0000000, 0.0000000)]))
    ACTUAL_AX = np.round(np.array([(0.5773503, -0.5773503, 0.5773503, 120.000)]), 6)
    FUNCTIONAL_AX = om2ax(rotation_matrix)
    assert np.all(ACTUAL_AX == FUNCTIONAL_AX)


def test_om2qu():
    rotation_matrix = np.round(np.array([(0.0000000, -1.0000000, 0.0000000),
                                         (-1.0000000, 0.0000000, 0.0000000),
                                         (0.0000000, 0.0000000, -1.0000000)]))
    ACTUAL_QO = np.round(np.array([(0.0000000, -0.7071068, -0.7071068, -0.0000000)]), 6)
    FUNCTIONAL_QO = om2qu(rotation_matrix)
    assert np.all(ACTUAL_QO == FUNCTIONAL_QO)
