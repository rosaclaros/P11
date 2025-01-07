
def hoeverlust(prozent):
    
    if prozent >= 20 and prozent <= 40:
        befund = "geringradige Schwerhörigkeit"
    elif prozent >= 40 and prozent <= 60:
        befund = "mittlere Schwerhörigkeit"
    elif prozent >= 60 and prozent <= 80:
        befund = "hochgradige Schwerhörigkeit"
    elif prozent >= 80 and prozent <= 95:
        befund = "Resthörigkeit"
    elif prozent == 100:
        befund = "Taubheit"
    else:
        befund = 'Kein gültige Eingabe'
              
    return (befund)

print('Der Befund lautet: '+ hoeverlust(0) + '.')
print('Der Befund lautet: '+ hoeverlust(100) + '.')

