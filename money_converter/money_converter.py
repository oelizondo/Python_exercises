def cambiar_peso_dolar(cantidad):
    return (cantidad * 17.5)

def cambiar_dolar_peso(cantidad):
    return (cantidad / 17.5)

def main():

    running = True

    while running:

        tipo_de_cambio = raw_input('Que quieres hacer?')

        if tipo_de_cambio == 'Cambiar dolares':
            dinero = raw_input('Especifica la cantidad')
            print(cambiar_peso_dolar(int(dinero)))

        elif tipo_de_cambio == 'Cambiar pesos':
            dinero = raw_input('Especifica la cantidad')
            print(cambiar_dolar_peso(int(dinero)))

        else:
            running = False

    return 'Bye'

if __name__ == '__main__':
    main()
