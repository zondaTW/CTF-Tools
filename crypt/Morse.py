#摩斯密碼解密程式
print("--摩斯密碼 解密程式--")
s = input("輸入密文 : ").split(" ")
print("明文 : ")
answer = ''
for i in range(len(s)):
    if(s[i]=='.-'):
        answer += 'a'
    elif(s[i]=='-...'):
        answer += 'b'
    elif(s[i]=='-.-.'):
        answer += 'c'
    elif(s[i]=='-..'):
        answer += 'd'
    elif(s[i]=='.'):
        answer += 'e'
    elif(s[i]=='..-.'):
        answer += 'f'
    elif(s[i]=='--.'):
        answer += 'g'
    elif(s[i]=='....'):
        answer += 'h'
    elif(s[i]=='..'):
        answer += 'i'
    elif(s[i]=='.---'):
        answer += 'j'
    elif(s[i]=='-.-'):
        answer += 'k'
    elif(s[i]=='.-..'):
        answer += 'l'
    elif(s[i]=='--'):
        answer += 'm'
    elif(s[i]=='-.'):
        answer += 'n'
    elif(s[i]=='---'):
        answer += 'o'
    elif(s[i]=='.--.'):
        answer += 'p'
    elif(s[i]=='--.-'):
        answer += 'q'
    elif(s[i]=='.-.'):
        answer += 'r'
    elif(s[i]=='...'):
        answer += 's'
    elif(s[i]=='-'):
        answer += 't'
    elif(s[i]=='..-'):
        answer += 'u'
    elif(s[i]=='...-'):
        answer += 'v'
    elif(s[i]=='.--'):
        answer += 'w'
    elif(s[i]=='-..-'):
        answer += 'x'
    elif(s[i]=='-.--'):
        answer += 'y'
    elif(s[i]=='--..'):
        answer += 'z'
    elif(s[i]=='.----'):
        answer += '1'
    elif(s[i]=='..---'):
        answer += '2'
    elif(s[i]=='...--'):
        answer += '3'
    elif(s[i]=='....-'):
        answer += '4'
    elif(s[i]=='.....'):
        answer += '5'
    elif(s[i]=='-....'):
        answer += '6'
    elif(s[i]=='--...'):
        answer += '7'
    elif(s[i]=='---..'):
        answer += '8'
    elif(s[i]=='----.'):
        answer += '9'
    elif(s[i]=='-----'):
        answer += '0'

print('大寫 = ',answer.upper())
print('小寫 = ',answer)
print('',end='')
input("\n--THE END--") #畫面暫停用
