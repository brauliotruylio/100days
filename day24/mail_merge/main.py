#TODO: Criar uma carta usando starting_letter.txt
#para cada nome em invited_names.txt
#Substitua o espaço reservado [nome] pelo nome real.
#Salve as cartas na pasta "ReadyToSend".

#Dica1: Este método ajudará você: https://www.w3schools.com/python/ref_file_readlines.asp
#Dica2: Este método também ajudará você: https://www.w3schools.com/python/ref_string_replace.asp
#Dica3: Este método ajudará você: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("day24/mail_merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("day24/mail_merge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"day24/mail_merge/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
