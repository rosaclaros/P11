
wetter = [
 "Munchen",
 ["Do", "Fr", "Sa", "So", "Mo", "Di", "Mi"],
 [14, 12, 11, 11, 11, 19, 6]
 ]

def maximal (aktuellesMax, liste):
    if len(liste) == 0:
        return aktuellesMax
    elif liste[0] > aktuellesMax:
        neuesMax = liste[0]
        return maximal (neuesMax, liste[1:])
    else:
        return maximal (aktuellesMax, liste[1:])