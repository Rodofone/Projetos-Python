def cripto(frase):
    tradutor = ''
    contador = 0
    for letra in frase:
        if letra in 'Aa':
            tradutor += 'd'
        elif letra in 'Bb':
            tradutor += 'e'
        elif letra in 'Cc':
            tradutor += 'f'
        elif letra in 'Dd':
            tradutor += 'g'
        elif letra in 'Ee':
            tradutor += 'h'
        elif letra in 'Ff':
            tradutor += 'i'
        elif letra in 'Gg':
            tradutor += 'j'
        elif letra in 'Hh':
            tradutor += 'k'
        elif letra in 'Ii':
            tradutor += 'l'
        elif letra in 'Jj':
            tradutor += 'm'
        elif letra in 'Kk':
            tradutor += 'n'
        elif letra in 'Ll':
            tradutor += 'o'
        elif letra in 'Mm':
            tradutor += 'p'
        elif letra in 'Nn':
            tradutor += 'q'
        elif letra in 'Oo':
            tradutor += 'r'
        elif letra in 'Pp':
            tradutor += 's'
        elif letra in 'Qq':
            tradutor += 't'
        elif letra in 'Rr':
            tradutor += 'u'
        elif letra in 'Ss':
            tradutor += 'v'
        elif letra in 'Tt':
            tradutor += 'w'
        elif letra in 'Uu':
            tradutor += 'x'
        elif letra in 'Vv':
            tradutor += 'y'
        elif letra in 'Ww':
            tradutor += 'z'
        elif letra in 'Xx':
            tradutor += 'a'
        elif letra in 'Yy':
            tradutor += 'b'
        elif letra in 'Zz':
            tradutor += 'c'
        elif letra in ' ':
            contador += 1
            if contador == 1:
                tradutor += '!'
            elif contador == 2:
                tradutor += '@'
            elif contador == 3:
                tradutor += '#'
            elif contador == 4:
                tradutor += '$'
            elif contador == 5:
                tradutor += '%'
            elif contador == 6:
                tradutor += '&'
                contador = 0
        else:
            tradutor += letra
    return tradutor.lower()

def descripto(frase):
    tradutor = ''
    for letra in frase:
        if letra in 'd':
            tradutor += 'a'
        elif letra in 'e':
            tradutor += 'b'
        elif letra in 'f':
            tradutor += 'c'
        elif letra in 'g':
            tradutor += 'd'
        elif letra in 'h':
            tradutor += 'e'
        elif letra in 'i':
            tradutor += 'f'
        elif letra in 'j':
            tradutor += 'g'
        elif letra in 'k':
            tradutor += 'h'
        elif letra in 'l':
            tradutor += 'i'
        elif letra in 'm':
            tradutor += 'j'
        elif letra in 'n':
            tradutor += 'k'
        elif letra in 'o':
            tradutor += 'l'
        elif letra in 'p':
            tradutor += 'm'
        elif letra in 'q':
            tradutor += 'n'
        elif letra in 'r':
            tradutor += 'o'
        elif letra in 's':
            tradutor += 'p'
        elif letra in 't':
            tradutor += 'q'
        elif letra in 'u':
            tradutor += 'r'
        elif letra in 'v':
            tradutor += 's'
        elif letra in 'w':
            tradutor += 't'
        elif letra in 'x':
            tradutor += 'u'
        elif letra in 'y':
            tradutor += 'v'
        elif letra in 'z':
            tradutor += 'w'
        elif letra in 'a':
            tradutor += 'x'
        elif letra in 'b':
            tradutor += 'y'
        elif letra in 'c':
            tradutor += 'z'
        elif letra in '!@#$%&':
            tradutor += ' '
        else:
            tradutor += letra
    return tradutor.lower()

