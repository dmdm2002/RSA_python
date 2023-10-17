"""원본 코드: https://blog.naver.com/PostView.nhn?blogId=locha0305&logNo=222013872911"""
p = 13
q = 29
n = p * q
tot = (p - 1) * (q - 1)


# 최대공약수 구하는 거
def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


# 공개키
def publickey():
    global tot
    e = 2
    while e < tot and gcd(e, tot) != 1:
        e += 1
    return e


# 개인키
def privatekey():
    global e
    global tot
    d = 1
    while (publickey() * d) % tot != 1 or d == publickey():
        d += 1
    return d


ori = (input("평서문 : "))
oris = list(ori)
orior = []
eori = []

etext = ""
for orisc in range(0, len(oris)):
    orior.append(ord(oris[orisc]))
for oriorc in range(0, len(orior)):
    eori.append(((orior[oriorc] ** publickey()) % n))

for eoric in range(0, len(eori)):
    etext += (chr(eori[eoric]))

print("암호문(NUMBER) : {}".format(eori))
print("암호문(ASCII) : {}".format(etext))
print("N : {}".format(n))
print("공개키 : {}".format(publickey()))
print("개인키 : {}".format(privatekey()))

# -- 복호화 --
n = int(input("N의 값을 입력하세요 : "))
eori = (input("암호문을 입력하세요 : "))

d = int(input("개인키를 입력하세요 : "))

eoris = list(eori)
eroiso = []
eroisor = []
eroar = []
text = ""
for eorisc in range(0, len(eoris)):
    eroiso.append(ord(eoris[eorisc]))
for eroisoc in range(0, len(eroiso)):
    eroisor.append((eroiso[eroisoc] ** d) % n)
for eroisorc in range(0, len(eroisor)):
    eroar.append(chr(eroisor[eroisorc]))
for eroarc in range(0, len(eroar)):
    text += eroar[eroarc]

print("평서문 : {}".format(text))
