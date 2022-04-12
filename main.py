stroka = input("")
item = "@"

stroka = stroka[::-1]
index = stroka.index(item)

stroka = (stroka[index+1:])
print(stroka[::-1])