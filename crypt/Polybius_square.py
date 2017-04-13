#Polybius square解密程式
print("--Polybius square 解密程式--")
s = input("輸入密文 : ").split(" ")
matrix_password=['abcde','fghik','lmnop','qrstu','vwxyz']
print("  -編碼表-")
for i in range(len(matrix_password)):
    print("  ",matrix_password[i])
print("明文 : ",end='')
for i in range(len(s)):
    for j in range(0,len(s[i]),2):
        print(matrix_password[int(s[i][j])-1][int(s[i][j+1])-1],end='')
    print(" ",end='')
input("\n--THE END--") #畫面暫停用
