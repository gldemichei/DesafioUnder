# Problema 1
def time_converter(time_AMPM) -> str:
    """Converte um horário no formato 12h (hh:mm:ssAM/PM) para o formato 24h (hh:mm:ss). 

    Args:
        time_AMPM (str): Horário no formato 12h (hh:mm:ssAM/PM)

    Returns:
        str: Horário no formato 24h (hh:mm:ss)
    """
    hh = time_AMPM[:2]
    mm_ss = time_AMPM[2:-2]
    if time_AMPM[-2:] == "PM":
        hh = int(hh)+12
    return str(hh) + mm_ss

def diagonals_diff(matrix):
    """Calcula a diferença absoluta entre a diagonal principal e a secundária de uma matriz quadrada

    Args:
        matrix ([[int]]): Matriz quadrada de números inteiros

    Returns:
        int: diferença absoluta entre diagonal principal e secundária da matriz
    """
    diag1 = []
    diag2 = []
    for i, line in enumerate(matrix):
        for j, element in enumerate(line):
            if i==j:
                diag1.append(element)
            if (i+j) == (len(line)-1):
                diag2.append(element)
    return abs(sum(diag1) - sum(diag2))

print(diagonals_diff([[1,2,3],[4,5,6],[9,8,9]]))