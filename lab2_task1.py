with open("sequences.txt") as f:
    contents = f.read()
content = contents.split(">")

genomes = []        # a list of full one line genomes
length = 0          # a length of single genome
base = []       #the first genome - oldest one without mutations

#[A, G, T, C]
for genome in content:
    genome = genome.split("\n")[1:]
    gen=""
    for line in genome:
        gen=gen+line
    genomes.append(gen)
    if not length:
        length = len(gen)
        for i in range(length):
            base.append({"A":0, "T":0, "G":0, "C":0})   #[0, 0, 0, 0] [A, T, G, C]
        #print("Each sequence is consists of:", length, "oligonucleotides")
    for i, letter in enumerate(gen):
        if letter == "A":
            base[i]["A"]+=1
        if letter == "T":
            base[i]["T"]+=1
        if letter == "G":
            base[i]["G"]+=1
        if letter == "C":
            base[i]["C"]+=1
genomes = genomes[1:]
genome_amount = len(genomes)
gen_count= [0] * genome_amount  #ile razy każdy gen był taki jak najczęstsze wystąpienie
#base_seq = ""
impact_letter_num_list = []
for i, dict in enumerate(base):
    frequent = max(dict, key=dict.get)  #the letter most often in the sequences at this collumn
    if(dict[frequent]==genome_amount):      #the amount it appeared
        #delete collumns with identical values for ALL GENES
        pass
    else:           #some mutated
        for j, genome in enumerate(genomes):    #for each genome give him one
            if(genome[i]==frequent):
                gen_count[j]+=1             #ile razy każdy gen był taki jak najczęstsze wystąpienie
        impact_letter_num_list.append(i)    #kolumny, których nie usówamy
        #the collumns with mutations
max_count = 0
max_count_iterator = None
for i, g in enumerate(gen_count):
    if g>max_count:
        max_count = g
        max_count_iterator = i
long_base_seq=genomes[max_count_iterator]     #z najwyższym countem - czyli najczestszy (na razie cały)
base_seq =""
for i, letter in enumerate(long_base_seq):
    if(i in impact_letter_num_list):
        base_seq+=letter
#print("MAAAXX", max_count,"the ase iterator:", max_count_iterator, "len of a BASE", len(base_seq), "the gene", base_seq)
#print("meaning base: len", len(base_seq),base_seq)
#print(base)

#USUWAMY NIEZNACZĄCE KOLUMNY
meaning_genoms = []
for j, genome in enumerate(genomes):
    new_genome=''
    for i, (num, b) in enumerate(zip(impact_letter_num_list, base_seq)):
        if(genome[num]==base_seq[i]):
            new_genome+='0'
        else:
            new_genome+='1'
    # print(j)
    # print("new gen len", len(new_genome), new_genome)
    # if(j == max_count_iterator):
    #     if('1' in new_genome):
    #         print("ERROR")
    #     else:
    #         print("The base sequence consists of only 0 - CORRECT")
    meaning_genoms.append(str(new_genome))
base_seq = meaning_genoms[max_count_iterator]
print("There are", len(meaning_genoms), "sequences.")
print("The sequences have", len(base_seq), "segregating sites." )
print("The base genome (not evolved) is the:", max_count_iterator, "th one the genomes matrix.")
print("Binary matrix of segregating sites:")#, meaning_genoms)
for j, genome in enumerate(meaning_genoms):
    print(genome)
    if(j == max_count_iterator):
        if('1' in genome):
            print("ERROR")
        else:
            print("The base sequence consists of only 0 - CORRECT")

