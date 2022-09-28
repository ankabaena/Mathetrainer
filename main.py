##This a a math training program for my daughter.

from replit import clear
from art import logo
import random

print(logo)
# NAME = input("Hallo! Wie heißt du?: ")
NAME = 'Nora'  # just to test


def game():
    clear()
    print(logo)
    print(f"Hallo {NAME}! Klar um Mathe zu üben? Los geht's!")

    def zahlenraum():
        mehr = True
        zahlenreihe = []
        while mehr:
            n = int(input("\nWelche Zahlenreihe möchtest Du üben?: "))
            if n == 0 or n == 1:
                print(f"Haha, du Witzbold! {n} ist VIIIIEEEL zu einfach!")
            else:
                zahlenreihe.append(n)
                x = input("Noch weitere? 'j'oder 'n': ").lower()
                if x == 'n':
                    mehr = False
        return zahlenreihe

    def gross_klein():
        a = input("\nWelches 1x1 möchtest Du üben? \n'k' für klein oder 'g' für groß: ").lower()
        if a == 'k':
            return list(range(1, 10 + 1))
        if a == 'g':
            return list(range(1, 20 + 1))

    def aufgaben():
        clear()
        print(logo)
        print(f"Gut {NAME}, ich stelle Dir jetzt 10 Augaben:  ")
        richtig = 0
        richtig2 = 0
        falsch = 0

        for i in range(1, 11):
            print(f"\nAufgabe {i}:")
            a = random.choice(einmaleins)
            b = random.choice(reihe)
            answer = int(input(f"\n{a} x {b} = "))
            if answer == a * b:
                print("\n RICHTIG! :)")
                richtig += 1
            else:
                print("\nLeider falsch. Versuch es nochmal:")
                answer2 = int(input(f"\n{a} x {b} = "))
                if answer2 == a * b:
                    print("\nGut, jetzt ist es richtig!")
                    richtig2 += 1
                else:
                    print(f"Leider auch falsch. :(\n{a} x {b} = {a * b}")
                    falsch += +1
            input("\nWeiter? Dann drück 'Enter':")
            clear()
            print(logo)

        out = [richtig, richtig2, falsch]
        return out

    def champion():
        clear()
        print(logo)
        print(f"Gut {NAME}, wie viele Augaben kannst du hintereinander richtig lösen?  ")
        richtig = 0
        champion = True
        while champion:
            print(f"\nAufgabe {richtig + 1}:")
            a = random.choice(einmaleins)
            b = random.choice(reihe)
            answer = int(input(f"\n{a} x {b} = "))
            if answer == a * b:
                print("\n RICHTIG! :)")
                richtig += 1
            else:
                print(f"Leider falsch. :(\n{a} x {b} = {a * b}\n")
                champion = False
                if richtig >= 20:
                    print(f"\nAPPLAUS!!!! Du hast {richtig} Augaben richtig gelöst!")
                    print(f"         {NAME}, du bist ein Mathe-Genie!")
                if richtig < 20 and richtig > 10:
                    print(f"Nicht übel, gar nicht übel, {NAME}!")
                    print(f"\nDu hast {richtig} Augaben richtig gelöst.")
                if richtig <= 10:
                    print(f"Das kannst du besser, {NAME}! \nVersuch es gleich noch einmal!")
                    print(f"\nDu hast {richtig} Augaben richtig gelöst.")
            input("\nWeiter? Dann drück 'Enter':")
            clear()
            print(logo)

        out = [richtig]
        return out

    def feedback(resultat):
        score = resultat[0] * 2 + resultat[1]
        print("Diese Runde ist fertig! :) \n")
        if score == 20:
            print("APPLAUS!!!! Du hast alle Augaben sofort richtig gelöst!")
            print(f"         {NAME}, du bist ein Mathe-Genie!")
        if score < 20 and score > 10:
            print(f"Nicht übel, gar nicht übel, {NAME}!")
        if score <= 10:
            print(f"Das kannst du besser, {NAME}! \nVersuch es gleich noch einmal!")
        print(
            f"\nVon 10 Aufgaben hast du \n{resultat[0]} Aufgaben sofort, \n{resultat[1]} beim 2. Versuch und \n{resultat[2]} nicht richtig gelöst\n")

    reihe = zahlenraum()
    einmaleins = gross_klein()
    version = input("\nWas möchtest du spielen: \n1)'10 Aufgaben' \n2)'Champion'\n\nTippe '1' oder '2: '")
    same = True
    while same:
        if version == '1':
            resultat = aufgaben()
            feedback(resultat)
        elif version == '2':
            champion()
        x = input("Noch eine Runde mit dem gleichen 1x1 und den gleichen Zahlenreihen? \n'j' oder 'n': ").lower()
        if x == 'n':
            same = False
            y = input("\nNoch einmal von vorne anfangen? 'j' oder 'n': ").lower()
            if y == 'j':
                game()
            else:
                print(f"\nCool, dass du geübt hast, {NAME}! Goodbye :)")


game()

# Start with Multiplication:
# Ask Nora which number-row she wants to practice
# ASk Nora if she wants to do it for the big or small 1x1
# Ask Nora how many excercises she wishes to do per round

# Calculations:
# Pick random numbers from the range selected, multiply
# Display excercise
# check if result correct
# if correct, count and do another round
# if wrong give her another try
#    if wrong
#     Output count, go, again
#
# after number of round, give her final feedback (right, 2nd rights, wrongs, comment)
# ask her if she wants to go again

# go_again = input("\nMöchtest du noch eine Runde spielen? 'ja' oder 'nein': ").lower
# if go_again == 'ja':
#   game()
# else:
#   print(f"\nToll, dass du geübt hast, {NAME}! Bis zum nächsten Mal :)")

# Ask Nora what she wants to do: Multiplikation, Division, Addition, Substraction



