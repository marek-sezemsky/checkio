def checkio(game_result):
    """Given game_result, return who win or draw"""

    def get_wins(gr, player):
        "Return number of 'wins' for given game_result gr"
        wins = 0
        for row in gr:
            print(row)
            if row == (player * 3):
                wins += 1

        for col in zip(*gr):
            col = "".join(col)
            if col == (player * 3):
                wins += 1

        if (player * 3) == gr[0][0] + gr[1][1] + gr[2][2]:
            wins += 1

        if (player * 3) == gr[2][0] + gr[1][1] + gr[0][2]:
            wins += 1

        print("{} for {}".format(wins, player))
        return wins

    cnt_x = get_wins(game_result, 'X')
    cnt_o = get_wins(game_result, 'O')
    if cnt_x < cnt_o:
        return "O"
    elif cnt_x > cnt_o:
        return "X"
    else:
        return "D"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

