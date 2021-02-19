# Problema 1
def time_converter(time_AMPM) -> str:
    """Converte um horário no formato 12h (hh:mm:ssAM/PM) para o formato 24h (hh:mm:ss). 

    Args:
        time_AMPM (str): horário no formato 12h (hh:mm:ssAM/PM)

    Returns:
        str: horário no formato 24h (hh:mm:ss)
    """
    hh, mm, ss = time_AMPM.split(":")
    hh = int(hh)
    mm = int(mm)
    ss = int(ss[:-2])
    am_pm = time_AMPM[-2:]
    
    if am_pm == "PM":
        hh = int(hh)+12
    if hh == 24 or hh == 12:  #corrige se meia noite ou meio dia
        hh -= 12

    return f'{str(hh).rjust(2, "0")}:{str(mm).rjust(2, "0")}:{str(ss).rjust(2, "0")}'


# Problema 2
def diagonals_diff(matrix):
    """Calcula a diferença absoluta entre a diagonal principal e a secundária de uma matriz quadrada

    Args:
        matrix ([[int]]): matriz quadrada de números inteiros

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


# Problema 3
def div_sum(arr, k):
    """ Dada uma lista de n inteiros, ar = [ar[0], ar[1], ..., ar[n-1]], e um inteiro positivo, k, 
        retorna o número de pares (i,j) onde i < j e ar[i] + ar[j] é divisível por k.
        
        Após a lista "arr" ser ordenada, é preciso verificar a divisibilidade por "k" de cada elemento apenas com os seus sucessores.

    Args:
        arr (int): lista não ordenada de inteiros
        k (int): inteiro para qual será verificada a divisibilidade

    Returns:
        [type]: [description]
    """
    result = 0
    arr.sort()
    for index, element1 in enumerate(arr):
        for element2 in (arr[index+1:]):
            if (element1+element2) % k==0:
                result += 1
    return result


if __name__ == '__main__':
    a = 1
    print(f'''
    Problema 1:
        12:00:00AM -> {time_converter("12:00:00AM")}
    
    Problema 2:
        1 2 3
        4 5 6 -> {diagonals_diff([[1,2,3],[4,5,6],[9,8,9]])}
        9 8 9

    Problema 3:
        (ar=[1, 2, 3, 4, 5, 6], k=5) -> {div_sum([1, 2, 3, 4, 5, 6], 5)}
    ''')