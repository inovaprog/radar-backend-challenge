def SaidaTempo(tempo):
    
    horas = 0
    minutos = 0
    segundos = 0

    segundos = tempo%60
    minutos = tempo//60
    horas = minutos//60
    minutos = minutos%60

    result = {
        "horas": horas,
        "minutos": minutos,
        "segundos": segundos
    }
    return result


def SaidaLitros(quantidade):
    litros = quantidade//1000
    ml = quantidade%1000

    result={
        "litros": litros,
        "ml": ml
    }
    return result