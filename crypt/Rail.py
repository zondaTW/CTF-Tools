#柵欄加密法解密程式

print("--柵欄加密法 解密程式--")
s = input("輸入密文 : ").split(" ")
for i in range(len(s)-1):
    s[0]+=s[1]
    del s[1]

for j in range(2, (len(s[0]) - 1) ):
    ans = ''
    for i in range(len(s[0])):
            ans += s[0][(i*j + i*j // len(s[0])) % len(s[0])]

    print("key : ",j," => ",ans)
input("\n--THE END--") #畫面暫停用
