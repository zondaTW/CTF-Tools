#Playfair加密法解密程式
print("--Playfair加密法 解密程式--")
s = input("輸入密文 : ")
key = input("輸入KEY : ")
#字母使用陣列 編碼陣列  清0
matrix_use=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matrix_password=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
matrix_password_2=[['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0'],['0','0','0','0','0']]
x=0
y=0
print("     -編碼表-")
for i in range(len(key)):
    if(ord(key[i])>=ord('a') and ord(key[i])<=ord('z')):
        if(matrix_use[ord(key[i])-ord('a')]==0):
            matrix_use[ord(key[i])-ord('a')]=1
            matrix_password[ord(key[i])-ord('a')]=x*10+y
            if(key[i]=='i'):
                matrix_use[ord('j')-ord('a')]=1
                matrix_password[ord('j')-ord('a')]=x*10+y
            if(key[i]=='j'):
                matrix_use[ord('i')-ord('a')]=1
                matrix_password[ord('i')-ord('a')]=x*10+y
            matrix_password_2[x][y]=key[i]
            print(" ",key[i],end='')
            x=x+(y+1)//5
            y=(y+1)%5
            if(y==0):
                print()
for i in range(26):
    if(matrix_use[i]==0):
        matrix_use[i]=1
        matrix_password[i]=x*10+y
        if(i==ord('i')-ord('a')):
            matrix_use[ord('j')-ord('a')]=1
            matrix_password[ord('j')-ord('a')]=x*10+y
        if(i==ord('j')-ord('a')):
            matrix_use[ord('i')-ord('a')]=1
            matrix_password[ord('i')-ord('a')]=x*10+y
        matrix_password_2[x][y]=chr(i+ord('a'))
        print(" ",chr(i+ord('a')),end='')
        x=x+(y+1)//5
        y=(y+1)%5
        if(y==0):
            print()
print("\n明文 : ",end='')
for i in range(0,len(s),3):
    number=matrix_password[ord(s[i])-ord('a')]
    number2=matrix_password[ord(s[i+1])-ord('a')]
    if(number%10 == number2%10): #同一行(直)
        print(matrix_password_2[(number//10-1)%5][number%10]+matrix_password_2[(number2//10-1)%5][number2%10],end='')
    elif (number//10 == number2//10): #同一列(橫)
        print(matrix_password_2[number//10][(number%10-1)%5]+matrix_password_2[number2//10][(number2%10-1)%5],end='')
    else: #對角
        print(matrix_password_2[number//10][number2%10]+matrix_password_2[number2//10][number%10],end='')        
    print(' ',end='')
input("\n--THE END--") #畫面暫停用
