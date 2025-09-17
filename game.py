import screen
import consts

def game_loop():
    for pokimon in consts.POKI_DICT:
        screen.add_poki(consts.POKI_DICT.get(pokimon))