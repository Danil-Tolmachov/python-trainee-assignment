import aiohttp


def prepare_matrix(matrix: str) -> list[list[int]]:
    result: list = []

    for line in matrix.split('\n'):
        if line and line[0] != '+':
            result.append([int(num) for num in line.split('|') if num.strip().isnumeric()])

    return result


def traverse_matrix(matrix: list[list[int]], result: list[int] = None) -> list[int]:

    if result is None:
        result = []

    if len(matrix) == 0:
        return result

    matrix = list(zip(*matrix[::-1]))
    result.extend(matrix[0][::-1])

    return traverse_matrix(matrix[1:], result)


async def get_matrix_string(url: str):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_matrix(url: str) -> list[int]:

    matrix = prepare_matrix(await get_matrix_string(url))

    return traverse_matrix(matrix)
