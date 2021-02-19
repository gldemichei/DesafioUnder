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

def 