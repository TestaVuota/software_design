"""
src = https://youtu.be/-njsRb8Tn70
"""


list_of_words = ["hello","yes","goodbye","cul"]
#%% Exemple 1
print(list_of_words[0]+","+list_of_words[1]+","+list_of_words[2]
      +","+list_of_words[3])


#%% Exemple 2
to_print=""

for i in range(len(list_of_words)):
    to_print += list_of_words[i]
    if i != len(list_of_words):
        to_print+= ","
        
print(to_print)

#%% Exemple 3
DELIMITER = ","
print(DELIMITER.join(list_of_words))

