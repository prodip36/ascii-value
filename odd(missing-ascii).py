i=chr
for i in range(ord('a'),ord('z')+1):
    if i%2!=0:
        print(chr(i),"-",i)