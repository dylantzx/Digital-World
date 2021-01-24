def get_base_counts2(dna):
    dna_count = {"A": 0, "C": 0, "G":0, "T": 0}
    if not dna.isalpha() or not dna.isupper():
        return "The input DNA string is invalid"
    else:
        for char in dna:
            if char == "A":
                dna_count["A"]+=1
            elif char == "C":
                dna_count["C"]+=1
            elif char == "G":
                dna_count["G"]+=1
            elif char == "T":
                dna_count["T"]+=1
        return dna_count
        
print(get_base_counts2("BACaAD131CR2ST"))
print(get_base_counts2("12323142341"))
print(get_base_counts2("asdfasvu"))
print(get_base_counts2("ACAINTCGKSGG"))

