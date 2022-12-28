import aiohttp


def prepare_matrix(matrix: str) -> list[list[int]]:
    """
        Prepares source matrix to list format.

        :param matrix: str
        :return: list[list[int]]
    """

    result: list = []

    for line in matrix.split('\n'):
        if line and line[0] != '+':
            result.append([int(num) for num in line.split('|') if num.strip().isnumeric()])

    return result


def untwisting_matrix(matrix: list[list[int]], result: list[int] = None) -> list[int]:
    """
        Prepares source matrix to list format.

        :param result: list[int]
        :param matrix: str

        :return: list[list[int]]
    """

    if result is None:
        result = []

    if len(matrix) == 0:
        return result

    matrix = list(zip(*matrix[::-1]))
    result.extend(matrix[0][::-1])

    return untwisting_matrix(matrix[1:], result)


async def get_raw_matrix(url: str) -> str:
    """
        Gets source matrix from url

        :param url: str
        :return: untwisted matrix: list[int]
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_matrix(url: str) -> list[int]:
    """
    Gets untwisted matrix from source.

    :param url: str
    :return: untwisted matrix: list[int]
    """

    matrix = prepare_matrix(await get_raw_matrix(url))

    return untwisting_matrix(matrix)
