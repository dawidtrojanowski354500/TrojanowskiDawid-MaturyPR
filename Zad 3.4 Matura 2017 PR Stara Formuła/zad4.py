#Dawid Trojanowski
#zad 4 matura 2017 PR
#stara formuła
dane = []
with open('Dane_PR2/binarne.txt','r') as file:
	for line in file:
		dane.append(line.strip())

#zadanie1
zad1 = 0
zad1_maks = '0'
#zadanie2
zad2 = 0
zad2_najk = 100
def niepoprawny(a):
	for i in range(int(len(a)/4)):
		l = a[i*4 : i*4 + 4]
		if int(l,2) > 9:
			return True
	return False
#zadanie3
zad3 = 0
for q in dane:
	d = len(q)
	p = int(d/2)
	if q[0:p] == q[p:]:
		zad1 += 1
		if d > len(zad1_maks):
			zad1_maks = q
	if niepoprawny(q):
		zad2 += 1
		if d < zad2_najk:
			zad2_najk = d
	if int(q) > zad3:
		if int(q,2) < 65535:
			zad3 = int(q)

zad1_dl = len(zad1_maks)


with open('zadanie4.txt','w') as w:
	w.write('1)\n' + str(zad1) + '\n' + str(zad1_maks) + '\n' + str(zad1_dl) 
			+ '\n2)\n' + str(zad2) + '\n' + str(zad2_najk)
			+ '\n3)\n' + str(zad3))