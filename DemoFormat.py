# DemoFormat.py

URL = "https://www.credu.com/?page=" + str(1)
print(URL)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("--오른쪽정렬--")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("--0으로 채우기--")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5))


print("--서식 지정 문자--")
