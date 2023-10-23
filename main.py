import ct
while True:

    f = input('Você deseja passar a temperatura de Fahrenheit para Celsius ou de Celsius para Fahrenheit: c/f ').lower()
    t = float(input('Digite a temperatura: '))

    if f == 'c':
        print('Passando a temperatura de {}°C para Fahrenheit passará a ser {}°F'.format(t, ct.c(t)))
    else:
        if f == 'f':
            print('Passando a temperatura de {}°F para Celsius passará a ser {:.2f}°C'.format(t, ct.f(t)))
        elif f != 'f' or f !='c':

            print('Diga se quer converter para Celsius ou para Fahrenheit c/f')
            print('Tente Novamente.')
    break