# 11)
def get_leap_years(start, end):
    """
    Input: Doi ani --> start, end
    Output: Afisarea anilor bisecti dintre cei doi ani inclusiv
    """
    if start > end:
        return None
    for idx in range(start, end + 1):
        if ((idx % 4 == 0) and (idx % 100 != 0)) or (idx % 400 == 0):
            print(idx, end=' ')


# 12)
def get_perfect_squares(start, end):
    """
    Input: Doua capete de interval inchis
    Output: Afisarea patratelor perfecte din acel interval inchis
    """
    for idx in range(start, end + 1):
        found = False
        nr = 1
        while (not found) and (nr <= idx // 2 + 1):
            if nr * nr == idx:
                found = True
                print(idx, end=' ')
            nr += 1


""" 
    get test_get_leap_years():
    assert get_leap_years((1, 0)) ==

Cum fac testele la functii de acest fel?
"""


def main():
    while True:
        print(' ')
        print('1. Afiseaza toti anii bisecti intre 2 ani dati,inclusiv anii dati')
        print('2. Afiseaza toate patratele perfecte dintr-un interval inchis dat')
        print('3. Iesi')
        optiune = input('Alege o optiune: ')
        if optiune == '1':
            print('Alege ani')
            an1 = int(input('Anul de inceput:'))
            an2 = int(input('Anul de sfarsit:'))
            get_leap_years(an1, an2)
        elif optiune == '2':
            print('Scrie interval')
            st = int(input('Limita stanga:'))
            dr = int(input('Limita dreapta:'))
            get_perfect_squares(st, dr)
        elif optiune == '3':
            break


main()
