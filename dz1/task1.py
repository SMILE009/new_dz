# TASK 1
# написати функцію, яка приймає словник і повертає список в якому всі значення словника помножені на 2

########################################################################################################################
myDict = {'a': 15, 'b': 21, 'c': 7, 'd': 9} #Словник не понятна хрень, кортеж?
spis = []
def myFunc(dict):
    for item in dict:
        spis.append(dict[item] * 2) #тут треба подумати як організувати краше переведення з словника в ліст
    return spis
print(myFunc(myDict))
########################################################################################################################