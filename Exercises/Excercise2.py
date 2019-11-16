# Exercise #2
from collections import Counter
from random import randint

# This one-liner creates a random 1024 basepair sequence
sequence = ''.join(["ACGT"[randint(0,3)] for i in range(1024)])

# This one-liner is yet another way of creating a dictionary
# with how many times each 5-mer appears in a sequence
kmerDict = Counter([sequence[i:i+5] for i in range(len(sequence)-5+1)])

# Write a short code fragment to find the most frequent 5-mer in sequence

maxKmer = max(kmerDict.values())
print(maxKmer)

# returns all max values
for kmer, count in kmerDict.items():
    if count == maxKmer:
        print (kmer)