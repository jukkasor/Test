#Tehdään yksinkertainen laskin
#Laskin ottaa kaksi arvoa sekä operaattorin ja laskee niiden summan, erotuksen, kertomisen tai jakolaskun
#Tehtäväsi on parannella laskinta järkevämmäksi

def laskin(luku1,luku2,operaattori):
	#Summa
	if(operaattori ==  "+"):
		summa = 0
		summa = luku1 + luku2
		return summa
	#Miinuslasku	
	elif(operaattori == "-"):
		erotus = 0
		erotuksen = luku1 - luku2
		return erotus
	#Kertolasku	
	elif(operaattori == "*"):
		kertominen = 0
		kertominen = luku1*luku2
		return kertominen
	elif(operaattori == "/"):
		jakolasku = 0
		jakolasku = luku1 / luku2
		return jakolasku
	else:
		print("Väärä operaattorin valinta. Operaattorreita ovat +,-,* ja /")
		print("Operaattosi oli", operaattori)
		return -1
		
		
print("Yksinkertainen laskin")
tulos = laskin(2,2,"*")
print("Tulos on", tulos)