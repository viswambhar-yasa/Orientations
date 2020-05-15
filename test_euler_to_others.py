import numpy as np
# import pytest as pt

from EULER_TO_OTHERS import eu2om
from EULER_TO_OTHERS import eu2ax
from EULER_TO_OTHERS import eu2ro
from EULER_TO_OTHERS import eu2ho
from EULER_TO_OTHERS import eu2qa


def test_eu2om():
    ACTUAL_RM = np.round(np.array([(0.0000000, 1.0000000, 0.0000000),
                                   (-0.0000000, 0.0000000, -1.0000000),
                                   (-1.0000000, 0.0000000, 0.0000000)]))
    angle = [270.0000000, 90.0000000, 180.0000000]
    FUN_RM = eu2om(angle)
    assert np.all(ACTUAL_RM == FUN_RM)


def test_eu2ax():
    ACTUAL_AX = np.round(np.array([(-0.7071068, -0.7071068, 0.0000000, 180.00)]), 6)
    angle = [270.0000000, 180.0000000, 180.0000000]
    FUNCTIONAL_AX = eu2ax(angle)
    assert np.all(ACTUAL_AX == FUNCTIONAL_AX)


def test_eu2ro():
    ACTUAL_RO = np.round(np.array([(0.5773503, -0.5773503, 0.5773503, 1.7320508)]), 6)
    angle = [360.0000000, 90.0000000, 90.0000000]
    FUNCTIONAL_RO = eu2ro(angle)
    assert np.all(ACTUAL_RO == FUNCTIONAL_RO)


def test_eu2ho():
    ACTUAL_HO = np.round(np.array([(1.3306700, 0.0000000, 0.0000000)]), 6)
    angle = [90.0000000, 180.0000000, 90.0000000]
    FUNCTIONAL_HO = eu2ho(angle)
    assert np.all(ACTUAL_HO == FUNCTIONAL_HO)


def test_eu2qa():
    ACTUAL_QO = np.round(np.array([(0.7071068, 0.0000000, 0.0000000, 0.7071068)]), 6)
    angle = [90.0000000, 0.0000000, 360.0000000]
    FUNCTIONAL_QO = eu2qa(angle)
    assert np.all(ACTUAL_QO == FUNCTIONAL_QO)

