#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
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




# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compar("W:\Alexandre\Ecoles\Polytechnique_2020-2021\INF1007\c04-ch8-exercices-Auzrid\exemple.txt","./2.txt")
    exo2("W:\Alexandre\Ecoles\Polytechnique_2020-2021\INF1007\c04-ch8-exercices-Auzrid\exemple.txt","./exemple3.txt")

    pass
