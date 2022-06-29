def cripto(frase):
    tradutor = ''
    for letra in frase:
        if letra in 'Aa':
            tradutor += 'f'
        elif letra in 'Bb':
            tradutor += 'j'
        elif letra in 'Cc':
            tradutor += 'l'
        elif letra in 'Dd':
            tradutor += '%'
        elif letra in 'Ee':
            tradutor += 'k'
        elif letra in 'Ff':
            tradutor += 'y'
        elif letra in 'Gg':
            tradutor += '6'
        elif letra in 'Hh':
            tradutor += '8'
        elif letra in 'Ii':
            tradutor += 'x'
        elif letra in 'Jj':
            tradutor += '$'
        elif letra in 'Kk':
            tradutor += '3'
        elif letra in 'Ll':
            tradutor += 'm'
        elif letra in 'Mm':
            tradutor += 'z'
        elif letra in 'Oo':
            tradutor += '&'
        elif letra in 'Uu':
            tradutor += 'w'
        elif letra in ' ':
            tradutor += 'h'
        else:
            tradutor += letra
    return tradutor.lower()

def descripto(frase):
    tradutor = ''
    for letra in frase:
        if letra in 'f':
            tradutor += 'a'
        elif letra in 'j':
            tradutor += 'b'
        elif letra in 'l':
            tradutor += 'c'
        elif letra in '%':
            tradutor += 'd'
        elif letra in 'k':
            tradutor += 'e'
        elif letra in 'y':
            tradutor += 'f'
        elif letra in '6':
            tradutor += 'g'
        elif letra in '8':
            tradutor += 'h'
        elif letra in 'x':
            tradutor += 'i'
        elif letra in '$':
            tradutor += 'j'
        elif letra in '3':
            tradutor += 'k'
        elif letra in 'm':
            tradutor += 'l'
        elif letra in 'z':
            tradutor += 'm'
        elif letra in '&':
            tradutor += 'o'
        elif letra in 'w':
            tradutor += 'u'
        elif letra in 'h':
            tradutor += ' '
        else:
            tradutor += letra
    return tradutor.lower()

