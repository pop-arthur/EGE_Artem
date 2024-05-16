from functools import lru_cache

# функия, которая возвращает все возможные ходы и  текущего положения x
# x - кол-во камней в 1 куче, y - во 2
def moves(x, y):
    return (x + 1, y), (x, y + 1), (x * 3, y), (x, y * 3)


# симулятор игры
# x, y - кол-во камней в кучах
@lru_cache(None)
def game(x, y):
    # если кол-во камней в куче не менее 28 => победа
    if x + y >= 49:
        return "W"  # win
    # если существуют ходы, ведущие в победу - побеждает Петя первым ходом
    if any(game(*move) == "W" for move in moves(x, y)):
        return "P1"
    # если все возможные ходы ведут в П1 - побеждает Ваня первым ходом
    if all(game(*move) == "P1" for move in moves(x, y)):
        return "V1"
    # если существуют ходы, ведущие в В1 - побеждает Петя вторым ходом
    if any(game(*move) == "V1" for move in moves(x, y)):
        return "P2"
    # если все возможные ходы ведут в П1 или П2 - побеждает Ваня12 ходом
    if all(game(*move) in ("P1", "P2") for move in moves(x, y)):
        return "V12"


# если ход пети неудачный - ваня красавчик - any
for y in range(1, 50):
    print(y, game(5, y))
