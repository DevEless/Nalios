def sum(nombres):
    if not nombres:
        return 0
    return nombres[0] + sum(nombres[1:])