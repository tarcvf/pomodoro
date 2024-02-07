def formatar(segundos):
    minutos,segundos = divmod(segundos,60)
    return "{:02d}:{:02d}".format(int(minutos), int(segundos))
