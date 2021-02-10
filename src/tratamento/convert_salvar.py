def ConverterTempo(tempo, unidade):
    if unidade == "h":
        return tempo*60*60
    if unidade == "m":
        return tempo*60
    if unidade == "s":
        return tempo

def ConverteLitros(quantidade, unidade):
    if unidade == "l":
        return quantidade*1000
    if unidade == "ml":
        return quantidade