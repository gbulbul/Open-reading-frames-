codons = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
'UCU':'S', 'UCC':'s', 'UCA':'S', 'UCG':'S',
'UAU':'Y', 'UAC':'Y', 'UAA':'STOP', 'UAG':'STOP',
'UGU':'C', 'UGC':'C', 'UGA':'STOP', 'UGG':'W',
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}


dna_string='AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
dna_string=dna_string.replace('A','U')
dna_string=dna_string.replace('T','A')
def swapping_C_G(ncs, n1, n2):
    ncs = ncs.replace(n2, '!',)
    ncs = ncs.replace(n1, n2)
    ncs = ncs.replace('!', n1)
    return ncs
dna_string=swapping_C_G(dna_string,'C','G')
#print(dna_string[dna_string.find('AUG'):])  # Start codon must be the beginning of the string
dna_string_reverse=dna_string[::-1]
#print(dna_string_reverse)
dna_string_reverse=dna_string_reverse[dna_string_reverse.find('AUG'):]  # Start codon must be the beginning of the reverse string
stop_codons_list=[]
for key in codons.keys():
    if codons[key]=='STOP':
        stop_codons_list.append(key)
        list_of_places_string_reverse=[]
        for i,v in enumerate(stop_codons_list):
            list_of_places_string_reverse.append(dna_string_reverse.find(stop_codons_list[i]))
            min_place_string_reverse=min(list_of_places_string_reverse)
#print(stop_codons_list)
#print(list_of_places)
#print(min_place_string)
#dna_string_reverse=dna_string_reverse[:min_place_string_reverse]  #A stop codon must be the end of the reverse string
print(dna_string_reverse[:min_place_string_reverse] ) 
class DNA_to_protein_class:
    stop=False
    def DNA_to_protein(string):
        prot=''
        possible_prots=[]
        for i in range(0,len(string),3):
            for key in codons.keys():
                if string[i:i+3]==key:
                    if codons[key] == 'STOP':
                       stop = True
                       break
                    prot+=(codons[key])
                    possible_prots.append(prot)
        return possible_prots
print(DNA_to_protein_class.DNA_to_protein(dna_string_reverse))