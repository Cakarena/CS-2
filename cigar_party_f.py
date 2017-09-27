def cigar_party(cigars, is_weekend):
	if is_weekend == True and cigars >= 40:
		success=True
	elif is_weekend == False and cigars >= 40 and cigars <= 60:
		success=True
	else:
		success=False
	print(success)

cigar_party(30,False)
cigar_party(50,False)
cigar_party(70,True)
cigar_party(30,True)
cigar_party(50,True)
cigar_party(60,False)
cigar_party(61,False)
cigar_party(40,False)
cigar_party(39,False)
cigar_party(40,False)
cigar_party(39,False)
