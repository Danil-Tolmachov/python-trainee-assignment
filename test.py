import asyncio

from matrix.transverse_matrix import get_matrix, prepare_matrix, transverse_matrix

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
SOURCE = """+-----+-----+-----+-----+
            |  10 |  20 |  30 |  40 |
            +-----+-----+-----+-----+
            |  50 |  60 |  70 |  80 |
            +-----+-----+-----+-----+
            |  90 | 100 | 110 | 120 |
            +-----+-----+-----+-----+
            | 130 | 140 | 150 | 160 |
            +-----+-----+-----+-----+"""

PREPARED = [
    10, 20, 30, 40,
    50, 60, 70, 80,
    90, 100, 110, 120,
    130, 140, 150, 160,
]
TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


def test_prepare_matrix():
    assert asyncio.run(prepare_matrix(SOURCE)) == PREPARED


def test_transverse_matrix():
    assert asyncio.run(transverse_matrix(PREPARED)) == TRAVERSAL


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL
