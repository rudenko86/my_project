a = "уёрёсэ нпа рпсб а оё мявмя гётоь"

def f (x):
    
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    n=''
    
    for i in x:
        index_ = 1
        while True:
            if i == 'а': #последняя буква
                n += 'я'
                break
            if i == letters[index_]: #маленькие буквы
                n += letters[index_-1]
                break
            if i == ' ': #пробел
                n += ' '
                break
            if i == '.': #точка
                n += '.'
                break
            if i == '!': #восклицательный знак
                n += '!'
                break
            if i == ',': #кома
                n += ','
                break
            if i == '?': #знак вопроса
                n += '?'
                break
            if i == '-': #дефис
                n += '-'
                break
            if i == ':': #двоеточие
                n += ':'
                break
            if i == ';': #точка с комой
                n += ';'
                break
            index_ += 1
                     
    print(n)

f(a)