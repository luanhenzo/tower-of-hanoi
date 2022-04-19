from typing import List

from EntityTower import Tower
from EntityDisc import Disc

def new_print_towers(t1: Tower, t2: Tower, t3: Tower):
    max_discs_t1 = t1.max_discs
    discs_in_t1 = len(t1.discs)

    max_discs_t2 = t2.max_discs
    discs_in_t2 = len(t2.discs)

    max_discs_t3 = t3.max_discs
    discs_in_t3 = len(t3.discs)

    greater_max_disc = max([max_discs_t1, max_discs_t2, max_discs_t3])
    for mounting in range(0, greater_max_disc + 1):
        t1_mounting = " "
        t2_mounting = " "
        t3_mounting = " "

        if (max_discs_t1 - greater_max_disc + mounting) >= 0:
            if (discs_in_t1 - greater_max_disc + mounting) >= 0:
                last_item = -1 - (discs_in_t1 - greater_max_disc + mounting)
                disc_size = t1.discs[last_item].size
                t1_mounting = f"{' '*(10-(disc_size+1))}[{'-'*disc_size}|{'-'*disc_size}]{' '*(10-(disc_size+1))}"
            else:
                t1_mounting = "          |          "

        if (max_discs_t2 - greater_max_disc + mounting) >= 0:
            if (discs_in_t2 - greater_max_disc + mounting) >= 0:
                last_item = -1 - (discs_in_t2 - greater_max_disc + mounting)
                disc_size = t2.discs[last_item].size
                t2_mounting = f"{' '*(10-(disc_size+1))}[{'-' * disc_size}|{'-' * disc_size}]{' '*(10-(disc_size+1))}"
            else:
                t2_mounting = "          |          "

        if (max_discs_t3 - greater_max_disc + mounting) >= 0:
            if (discs_in_t3 - greater_max_disc + mounting) >= 0:
                last_item = -1 - (discs_in_t3 - greater_max_disc + mounting)
                disc_size = t3.discs[last_item].size
                t3_mounting = f"{' '*(10-(disc_size+1))}[{'-' * disc_size}|{'-' * disc_size}]{' '*(10-(disc_size+1))}"
            else:
                t3_mounting = "          |          "

        if mounting < greater_max_disc:
            print(f"{t1_mounting}{t2_mounting}{t3_mounting}   ")
        else:
            print(f"{' '*9}T-1{' '*18}T-2{' '*18}T-3{' '*9}")
    # print("        [-|-]                  |                    |          ")
    # print("       [--|--]                 |                    |          ")
    # print("      [---|---]                |                    |          ")
    # print("     [----|----]               |                    |          ")
    # print("    [-----|-----]              |                    |          ")
    # print("   [------|------]             |                    |          ")
    # print("  [-------|-------]            |                    |          ")
    # print(" [--------|--------]           |                    |          ")
    # print("         T-1                  T-2                  T-3         ")

def big_space():
    for prints in range(0, 30):
        print()

if __name__ == '__main__':
    def validate_discs_qnt(input_message: str) -> int:
        qnt_discs = -1
        while not 1 <= qnt_discs <= 8:
            try:
                qnt_discs = int(input(input_message))
                input_message = "Valor inválido. Insira um número entre 1 e 8: "
            except ValueError:
                qnt_discs = -1
                input_message = "Valor inválido. Somente número são permitidos: "
        else:
            big_space()
        return qnt_discs

    qnt_discs = validate_discs_qnt("Quantos discos serão utilizados? (Min. 1 e máx. 8): ")

    initial_discs = [Disc(qnt_discs - disc) for disc in range(0, qnt_discs)]
    t1 = Tower(6, initial_discs.copy())
    t2 = Tower(3)
    t3 = Tower(4)
    towers = [t1, t2, t3]

    def print_towers(towers: List[Tower]):
        for tower in range(0, len(towers)):
            print(f"{tower + 1} ->", towers[tower])
        else:
            print()

    def select_tower(input_message: str, towers_list: List[Tower]) -> Tower:
        tower_index = -1
        while not 1 <= tower_index <= len(towers_list):
            try:
                tower_index = int(input(input_message))
                input_message = "Valor inválido. Selecione umas torres acima: "
            except ValueError:
                input_message = "Valor inválido. Somente número são permitidos: "
                tower_index = -1
        else:
            print()
        tower = towers_list[tower_index-1]
        return tower

    while t3.discs != initial_discs:
        new_print_towers(t1, t2, t3)
        selected_tower = select_tower("Selecione a torre que você vai tirar o disco: ", towers)

        big_space()

        print(f"Torre selecionada: {selected_tower}\n")

        towers_less_selected = towers.copy()
        towers_less_selected.remove(selected_tower)
        print_towers(towers_less_selected)
        target_tower = select_tower("Selecine a torre que você colocará o disco: ", towers_less_selected)

        selected_tower.transfer_disc(target_tower)
        big_space()
    else:
        print_towers(towers)
        print("Você ganhou!")
