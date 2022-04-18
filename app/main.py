from EntityTower import Tower

def print_towers(t1, t2, t3):
    print("           |                    |                    |           ")
    print("           |                    |                    |           ")
    print("           |                    |                    |           ")
    print("           |                    |                    |           ")
    print("           |                    |                    |           ")
    print("           |                    |                    |           ")
    print("           |                    |                    |           ")
    print("           |                    |                    |           ")
    print("          T-1                  T-2                  T-3          ")

if __name__ == '__main__':
    qnt_discs = 0

    is_disc_qnt_valid = False
    qnt_discs = input("Quantos discos serão utilizados? (Min. 1 e máx. 8): ")
    if 1 <= qnt_discs <= 8:
        is_disc_qnt_valid = True

    while not is_disc_qnt_valid:
        qnt_discs = input("Quantos discos serão utilizados?: ")
        if 1 <= qnt_discs <= 8:
            is_disc_qnt_valid = True

    t1 = Tower()
    t2 = Tower()
    t3 = Tower()
