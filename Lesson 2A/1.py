from functools import lru_cache

# функия, которая возвращает все возможные ходы и  текущего положения x
# x - кол-во камней в куче
def moves(x):
    return x + 1, x + 3, x * 2


# симулятор игры
# x - кол-во камней в куче
@lru_cache(None)
def game(x):
    # если кол-во камней в куче не менее 28 => победа
    if x >= 28:
        return "W"  # win
    # если существуют ходы, ведущие в победу - побеждает Петя первым ходом
    if any(game(move) == "W" for move in moves(x)):
        return "P1"
    # если все возможные ходы ведут в П1 - побеждает Ваня первым ходом
    if all(game(move) == "P1" for move in moves(x)):
        return "V1"
    # если существуют ходы, ведущие в В1 - побеждает Петя вторым ходом
    if any(game(move) == "V1" for move in moves(x)):
        return "P2"
    # если все возможные ходы ведут в П1 или П2 - побеждает Ваня12 ходом
    if all(game(move) in ("P1", "P2") for move in moves(x)):
        return "V12"


# если ход пети неудачный - ваня красавчик - any
for x in range(1, 30):
    print(x, game(x))
