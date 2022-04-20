from typing import List

from EntityTower import Tower
from EntityDisc import Disc

def new_print_towers(t1: Tower, t2: Tower, t3: Tower, selected_tower: Tower = None):
    greater_max_disc = max([t1.max_discs, t2.max_discs, t3.max_discs])
    for mounting in range(0, greater_max_disc):
        def print_tower(tower: Tower) -> str:
            tower_mounting = "                     "
            max_discs = tower.max_discs
            discs_in = len(tower.discs)

            if (max_discs - greater_max_disc + mounting) >= 0:
                if (discs_in - greater_max_disc + mounting) >= 0:
                    last_item = -1 - (discs_in - greater_max_disc + mounting)
                    disc_size = tower.discs[last_item].size
                    tower_mounting = f"{' ' * (10 - (disc_size + 1))}[{'-' * disc_size}|{'-' * disc_size}]{' ' * (10 - (disc_size + 1))}"
                else:
                    tower_mounting = "          |          "
            return tower_mounting

        t1_mounting = print_tower(t1)
        t2_mounting = print_tower(t2)
        t3_mounting = print_tower(t3)

        print(f"{t1_mounting}{t2_mounting}{t3_mounting}   ")
    else:
        print(f"{' '*9 if selected_tower is not t1 else ' '*6}"
              f"{'-> ' if selected_tower is t1 else ''}T-1{' <-' if selected_tower is t1 else ''}"
              f"{' '*9 if selected_tower is not t1 else ' '*6}"
              
              f"{' '*9 if selected_tower is not t2 else ' '*6}"
              f"{'-> ' if selected_tower is t2 else ''}T-2{' <-' if selected_tower is t2 else ''}"
              f"{' '*9 if selected_tower is not t2 else ' '*6}"
              
              f"{' '*9 if selected_tower is not t3 else ' '*6}"
              f"{'-> ' if selected_tower is t3 else ''}T-3{' <-' if selected_tower is t3 else ''}"
              f"{' '*9 if selected_tower is not t3 else ' '*6}")
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

def app():
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
    t1 = Tower(8, initial_discs.copy())
    t2 = Tower(8)
    t3 = Tower(8)
    towers = [t1, t2, t3]

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

        new_print_towers(t1, t2, t3, selected_tower)

        towers_less_selected = towers.copy()
        towers_less_selected.remove(selected_tower)
        target_tower = select_tower("Selecine a torre que você colocará o disco: ", towers)

        selected_tower.transfer_disc(target_tower)
        big_space()
    else:
        new_print_towers(t1, t2, t3)
        print("Você ganhou!")

if __name__ == '__main__':
    app()
