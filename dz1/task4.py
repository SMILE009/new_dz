#TASK 4
# написати функцію, яка сортує масив слів по кількості голосних і видаляє
# з масиву інші (не string) типи (потрібно використати функцію для перевірки типу)

mass = ['hello', 2, 'Victor', 'mmalkush', 'Dzvinkaa']

def myFunc(list):
    def removeString(list):
        position = 0
        for item in list:
            if not isinstance(item, str):
                del list[position]
            position += 1
        return list
    def countvowels(list):
        vowels = {}
        position = 0
        for word in list:
            vowels.update({word: 0})
            for item in word:
                if item.lower() in 'aeiouy':
                   vowels[word] += 1
            position += 1
        return vowels
    removeString(list)
    print(countvowels(list))

print(myFunc(mass))

# можна відправляти на говнокод.ру (не вкурю як тепер посортувати той словник)

