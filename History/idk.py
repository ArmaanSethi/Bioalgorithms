def kmerCounts(seq, k):
    kmerDict = {}
    seq = seq+seq[1:]
    print(seq)
    for i in range(1,len(seq)+1):
        kmer = seq[i:i+k]
        kmerDict[kmer] = kmerDict.get(kmer,0) + 1
    return kmerDict

print(kmerCounts("+ACATATAGAGAGACATTAG", 3))

def kmerCounts_old(seq, k):
    kmerDict = {}
    for i in range(1,len(seq)-k+1):
        kmer = seq[i:i+k]
        kmerDict[kmer] = kmerDict.get(kmer,0) + 1
    return kmerDict

print(kmerCounts_old("+ACATATAGAGAGACATTAG", 3))
