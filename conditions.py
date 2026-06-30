vitesse = 30 
obstacle_detecte = True
batterie = 15 
print("======FICHES DE CONDITIONS======")
if obstacle_detecte:
    print("ALERTE: Obstacle détecté - Arrêt immédiat")
else:
    print("voie libre - continuer la route ")
if batterie < 20:
    print("ALERTE: batterie faible - recharcge necessaire")
else:
    print("batterie ok :", batterie,"%")
if vitesse > 25:
    print("ALERTE: vitesse excessive - ralentir")
else:
    print("vitesse ok :", vitesse,"km/h")