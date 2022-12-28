import asyncio
import pytest

from matrix.matrix import get_matrix, prepare_matrix, untwisting_matrix, get_raw_matrix

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
SOURCE = """+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+
"""

PREPARED = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160],
]
UNTWISTED = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


@pytest.mark.asyncio
async def test_get_raw_matrix():
    assert await get_raw_matrix(SOURCE_URL) == SOURCE


def test_prepare_matrix():
    assert prepare_matrix(SOURCE) == PREPARED


def test_untwisting_matrix():
    assert untwisting_matrix(PREPARED) == UNTWISTED


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == UNTWISTED
