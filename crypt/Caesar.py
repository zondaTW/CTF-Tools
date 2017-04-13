#coding=UTF-8
#凱薩猜測明文程式
print("--凱薩加密法 猜測明文程式--")
s = input("輸入密文 :")

for j in range(1,26):
    print("key :",j," => ",end='')
    ans = ''
    for i in range(len(s)):
        if(s[i]>='a' and s[i]<='z'):
            ans += chr((ord(s[i])-j-ord('a'))%26+ord('a'))
        elif(s[i]>='A' and s[i]<='Z'):
            ans += chr((ord(s[i])-j-ord('A'))%26+ord('A'))
        else: 
            ans += s[i]
    print(ans)
input("\n--THE END--") #畫面暫停用
