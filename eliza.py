#eliza.py
#En verkligt simpel version av ett Eliza-liknande program
#1) Önskar användaren välkommen
#2) Upprepar följande i all oändlighet
# 2.1) Väntar på att användaren "säger" något
# 2.2) Svarar på ett sätt som verkar intelligent
# Svaret väljs alltid slumpmässigt ur en samling uttryck som vi lagrat i en
# lista. På detta sätt får vi användaren att tro
#att Eliza faktiskt är smart. Eller så inte :)
import string
import random

def main():
    positiva = ["Berätta mer",
    "Jag förstår...",
    "Ahaa...",
    "Jag lyssnar..."]

    negativa = ["Inte det?", 
    "Varför inte?", 
    "Är du helt säker?",
    "Är det sant", 
    "Säger du en negativ mening för att vara negativ?"]


    print ("**************************************************")
    print ()
    print (" Välkommen till Elizas mottagning ")
    print ()
    print ("**************************************************")
    print ()
    print ('(Du kan sluta när som helst genom att svara "hejda")')
    print ()
    print ('Berätta för mig om dina problem...')
    # Fortsätt diskussionen i all oändlighet
    while True:
        # Vänta på att användaren matar in något
        text = input("\n> ")
        text = text.lower()
        
        urspr_ord = str.split(text)
        nya_ord = replace_words(urspr_ord) 
        ny_text = " ".join(nya_ord)

        #  Quit
        if text == "hejda":
            break
       
        # Choose Answer
        elif "nej" in urspr_ord or "aldrig" in urspr_ord or "inte" in urspr_ord:
            print (random.choice(negativa))
        elif nya_ord == urspr_ord:
            # Svara "smart" genom att slumpmässigt välja ett uttryck ur listan
            print (random.choice(positiva))
        else:
            print(ny_text + "?")

    print ('Tack för besöket. Betala in 150 EUR på mitt konto.')


def replace_words(urspr_ord):
    # Dictionary with replacement words
    replaceDict = {
        "jag": "du",
        "min": "din",
        "mitt": "ditt",
        "mig": "dig",
        "mina": "dina"
    }

    # Arrays
    first_pers_list = list(replaceDict.keys()) # list of keys --> ['jag', 'min', 'mitt'...]
    second_pers_list = list(replaceDict.values()) # list of values --> ['du', 'din', 'ditt'...]
    nya_ord = list(urspr_ord) # copy of list ursp_ord
    dont_change_index = [] # if word already replaced dont change --> used to track second person to first person replacements

    # Replace words
    for i in range(len(urspr_ord)):

        # Second Person Singular --> First Person Singular
        if urspr_ord[i] in second_pers_list:
            dont_change_index.append(i)
            index = second_pers_list.index(urspr_ord[i]) # index off valuesArr --> the same as index of keysArr
            nya_ord[i] = first_pers_list[index]

        # First Person Singular --> Second Person Singular
        if urspr_ord[i] in first_pers_list and i not in dont_change_index:
            index = first_pers_list.index(urspr_ord[i])
            nya_ord[i] = second_pers_list[index]

    return nya_ord

main()