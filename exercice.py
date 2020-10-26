#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def file_comparator(file1, file2):
    if file1 != file2:
        with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
            for index, line1 in enumerate(f1):
                line2 = f2.readline()
                if line1 != line2:
                    print(f"Les fichiers diffèrent à la ligne {index + 1}, on a: \n{line1} et on a: \n{line2}")
                    break

def triple_space(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "w", encoding="utf-8") as f2:
        """
        for character in f1:
            if character == " ":
                f2.write(character * 3)
            else:
                f2.write(character)
        """
# verifier si les retours à la ligne sont
        for line in f1:
            words = line.split()
            line_triple = "   ".join(words)
            f2.write(line_triple)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print("./exemple.txt")
    pass
