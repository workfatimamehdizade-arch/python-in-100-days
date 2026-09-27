import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(phonetic_dict)
#  Create a list of the phonetic code words from a word that the user inputs.

