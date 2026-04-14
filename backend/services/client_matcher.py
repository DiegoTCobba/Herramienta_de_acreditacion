def adivinar_cliente(texto, cuentas):
    texto = texto.upper()

    for cliente in cuentas:
        if cliente.upper() in texto:
            return cliente

    return None
