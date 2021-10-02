# 12)

def get_perfect_squares(start, end):
    for idx in range(start, end + 1):
        found = False
        nr = 1
        while (not found) and (nr <= idx // 2 + 1):
            if nr * nr == idx:
                found = True
                print(idx)
            nr += 1




def main():
    while True:
        print('1. Afiseaza toti anii bisecti intre 2 ani dati,inclusiv anii dati')
        print('2. Afiseaza toate patratele perfecte dintr-un interval inchis dat')
        print('3. Iesi')
        optiune = input('Alege o optiune: ')
        if optiune == '2':
            print('Scrie interval')
            st = int(input('Limita stanga:'))
            dr = int(input('Limita dreapta:'))
            get_perfect_squares(st, dr)
        elif optiune == '3':
            break

main()
