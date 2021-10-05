# 11)
def get_leap_years(start: int, end: int) -> list[int]:
    """
    Input: Doi ani --> start, end
    Output: O lista cu anii bisecti dintre anii introdusi
    """
    lst = []
    if (start > end) or ((start == 0) and (end == 0)):
        return lst
    for idx in range(start, end + 1):
        if ((idx % 4 == 0) and (idx % 100 != 0)) or (idx % 400 == 0):
            lst.append(idx)
    return lst


# 12)
def get_perfect_squares(start: int, end: int) -> list[int]:
    """
    Input: Doua capete de interval inchis --> start, int
    Output: O lista cu patratele perfecte din acel interval inchis
    """
    lst = []
    for idx in range(start, end + 1):
        found = False
        nr = 1
        while (not found) and (nr <= idx // 2 + 1):
            if nr * nr == idx:
                found = True
                lst.append(idx)
            nr += 1
    return lst


def test_get_leap_years():
    assert get_leap_years(2000, 2021) == [2000, 2004, 2008, 2012, 2016, 2020]
    assert get_leap_years(0, 0) == []
    assert get_leap_years(2000, 1900) == []


def test_get_perfect_squares():
    assert get_perfect_squares(0, 1) == [1]
    assert get_perfect_squares(0, 30) == [1, 4, 9, 16, 25]
    assert get_perfect_squares(36, 36) == [36]
    assert get_perfect_squares(7, 1) == []


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
            result = get_leap_years(an1, an2)
            if result == []:
                print('Nu exista rezultate pt datele introduse')
            else:
                print(result)

        elif optiune == '2':
            print('Scrie interval')
            st = int(input('Limita stanga:'))
            dr = int(input('Limita dreapta:'))
            result = get_perfect_squares(st, dr)
            if result == []:
                print('Nu exista rezultate pt datele introduse')
            else:
                print(result)

        elif optiune == '3':
            break


test_get_leap_years()
test_get_perfect_squares()
main()
