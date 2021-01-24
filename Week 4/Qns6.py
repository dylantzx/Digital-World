def get_base_counts(dna):
    #dna is a string
    dna_count = {"A": 0, "C": 0, "G":0, "T":0}
    for i in dna:
        if i in dna_count:
            dna_count[i]+=1
        else:
            return "The input DNA string is invalid"
    return dna_count

print(get_base_counts("AACCGT"))
print(get_base_counts("AACCG"))
print(get_base_counts("AAB"))
print(get_base_counts("AaCcGT"))
