seq="aaacaaaccgaaagcaacgaaaaagtgggtcgttagctcagttggtagagc"

code = { 'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
             'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
             'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
             'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
             'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
             'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
             'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
             'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
             'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
             'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
             'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
             'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
             'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
             'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
             'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
             'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'
}

# determine si une sequence est correcte
def  seqADNCorrecte(seq):
	for cara in seq:
		if cara not in 'actg':
			return False
	return True
 
#affiche la fréquences des bases sur une sequence 
def afficherStatBaseADN(seq):
	nbr=len(seq)
	nbrA=0
	nbrC=0
	nbrT=0
	nbrG=0
	
	for cara in seq:
		if cara=='a':
			nbrA+=1
		if cara=='c':
			nbrC+=1
		if cara=='t':
			nbrT+=1
		if cara=='g':
			nbrG+=1						
	
	print("a:",nbrA/nbr,"%")
	print("c:",nbrC/nbr,"%")
	print("t:",nbrT/nbr,"%")
	print("g:",nbrG/nbr,"%")
 
def traduction(seq):
	prot=''
	i=0
	#pour chaque codon
	while i<len(seq):
		#on calcul l'acide aminé correpondant et on l'ajoute à la protéine
		prot+=code[seq[i:i+3]]
		i+=3
	return prot
 
f=open("seq.txt","r")
for s in f:
    #enleve le retour à la ligne, si il est présent
    if(s[len(s)-1]=='\n'):
        s=s[:len(s)-1]
    print("Sequence :")
    print(s)
    if seqADNCorrecte(s) :
        afficherStatBaseADN(s)
        prot=traduction(s)
        print(prot)
    else:
        print("Sequence incorecte")
  
f.close()