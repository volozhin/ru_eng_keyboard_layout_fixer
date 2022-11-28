from pyfiglet import Figlet

def translate(string='NTCN'):
    eng = 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~qwertyuiop[]asdfghjkl;\'zxcvbnm,./`!@#$%^&*()?'
    rus = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ёйцукенгшщзхъфывапролджэячсмитьбю.ё!"№;%:?*(),'
    print(string.translate(string.maketrans(rus, eng)) if any(i >= 'А' for i in string) else string.translate(string.maketrans(eng, rus)))

def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('REVERSE RU<=>ENG'))
    print(preview_text.renderText('keyboard layout'))
    cont = input('Press "c" to continue or other key to exit: ')
    while cont=='c':

        string = input('INSERT TEXT YOU WANT TO CHANGE: ')
        translate(string=string)
        cont = input('Press "c" to continue or other key to exit: ')

if __name__ == '__main__':
    main()
