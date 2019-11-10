f = open('sample.txt', 'r')
line = f.readline()


print("let ts=[")
while line:
    print('"'+line.strip()+'",')
    line = f.readline()
f.close()
print('"","終わり。"];')
