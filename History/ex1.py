def kmerCounts(seq, k):
    kmerDict = {}
    l = len(seq)
    seq = seq+seq[1:k+1]
    print(seq)
    for i in range(1,l+1):
        kmer = seq[i:i+k]
        print(kmer)
        kmerDict[kmer] = kmerDict.get(kmer,0) + 1
    return kmerDict

print("armaan\n",kmerCounts("+ACATATAGAGAGACATTAG", 3))

def kmerCounts_old(seq, k):
    kmerDict = {}
    for i in range(1,len(seq)-k+1):
        kmer = seq[i:i+k]
        kmerDict[kmer] = kmerDict.get(kmer,0) + 1
    return kmerDict

print("mcmillan\n",kmerCounts_old("+ACATATAGAGAGACATTAG", 3))

def kmerCountsrob(seq, k):
    kmerDict = {}
    for i in range(1,len(seq)):
        if(i>len(seq)-k):
            pre = seq[i:len(seq)]
            post = seq[1:k-(len(seq)%i)+1]
            kmer = str(pre)+str(post)
            print(str(i)+' '+str(len(seq))+' '+pre+' | '+str(1)+' '+str(k-(len(seq)%i)+1)+' '+post)
        else:          
            kmer = seq[i:i+k]
        kmerDict[kmer] = kmerDict.get(kmer,0) + 1
    return kmerDict

print("rob\n",kmerCountsrob("+ACATATAGAGAGACATTAG", 3))


