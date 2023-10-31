import pandas
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# student_data_frame = pandas.DataFrame(student_dict)
# new_dict = {row.student: row.score for (index, row) in student_data_frame.iterrows()}
# print(new_dict)

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_data_frame = pandas.DataFrame(alphabet_csv)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = [alphabet_dict[name.upper()] for name in input("What's your name?: ")]
print(word)
