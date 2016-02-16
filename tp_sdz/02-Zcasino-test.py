import modules.Zcasino as Zcasino
from time import sleep

pot = 500;
end = False
while (end is False):
    if pot <= 0:
        print("Vous avez tout perdu !")
        exit()
    print("Vous pouvez miser jusqu'à",pot,"$")
    playedNum = input("Miser sur le numéro (0-49) : ")
    mise = input("Montant misé : ")
    try:
        mise = int(mise)
        pot = pot - mise
        playedNum = int(playedNum)
        print("Rien ne va plus...")
        sleep(2)
        argentGagne = Zcasino.play(playedNum, mise)
        print("Vous avez gagné : ", argentGagne, " $")
        pot = pot + argentGagne
    except:
        print("Saisie invalide")
        end = True
