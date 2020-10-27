#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from os import path
import pickle
from recettes import add_recipes, print_recipe

def compar(a,b):
    with open(a,encoding="utf-8") as f1, open(b,encoding="utf-8") as f2:
        for index, line1 in enumerate(f1):
            line2 = f2.readline()

            if line1 != line2:
                print(f"different, {index + 1}, ")
                print(line1)
                print('et on a')
                print(line2)
                break

def exo2(a,b):
    with open(a, encoding="utf-8") as f1, open(b,"w", encoding="utf-8") as f2:
        for line in f1:
            words = line.split()
            line_triple = "   ".join(words)
            f2.write(line_triple+'\n')


def exercice3(file_path, result_file):
    with open(file_path, encoding = "utf-8") as f:
        note_per = f.readlines()

    with open(result_file, "w", encoding= "utf-8") as f1:
        for note in note_per:
            for key, item in PERCENTAGE_TO_LETTER.items():
                if item[0] <= int(note) < item[1]:
                    f1.write(note.strip() + " " + key + "\n")
                    break





def deleted_recipe(recipes):
    name = input('entrez nom recette pour supprime \n')

    if name in recipes:
        del recipes[name]
        print('la recc est supprime\n')
    else:
        print("la rec pas la")

    return recipes


def exo4(filepath = "./exemple3.p"):
    if path.exists(filepath):
        recipes = pickle.load(open(filepath, 'rb'))
    else:
        recipes = dict()
    while True:
        choice = input("a) ajout? \n b) modif? \n c) supprim \n d) aff \n e) quitter").strip()

        if choice == "a":
            add_recipes(recipes)
        elif choice == "b":
            add_recipes(recipes)
        elif choice == "c":
            recipes = deleted_recipe(recipes)
        elif choice == "d":
            print_recipe(recipes)
        elif choice == "e":
            break
        else:
            print("choix n'est pas valide")

    pickle.dump(recipes, open(filepath, 'wb'))



# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compar("W:\Alexandre\Ecoles\Polytechnique_2020-2021\INF1007\c04-ch8-exercices-Auzrid\exemple.txt","./2.txt")
    exo2("W:\Alexandre\Ecoles\Polytechnique_2020-2021\INF1007\c04-ch8-exercices-Auzrid\exemple.txt","./exemple3.txt")
    exercice3("W:\Alexandre\Ecoles\Polytechnique_2020-2021\INF1007\c04-ch8-exercices-Auzrid\potes.txt","./exemple3.txt")
    exo4()
    pass
