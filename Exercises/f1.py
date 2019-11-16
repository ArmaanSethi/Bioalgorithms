import numpy

def Alignment(b,v,w,i,j):
    if ((i == 0) and (j == 0)):
        return ['','']
    if (b[i,j] == 3):
        result = Alignment(b,v,w,i-1,j-1)
        result[0] += v[i-1]
        result[1] += w[j-1]
        return result
    else:
        if (b[i,j] == 2):
            result = Alignment(b,v,w,i,j-1)
            result[0] += "_"
            result[1] += w[j-1]
            return result
        else:
            result = Alignment(b,v,w,i-1,j)
            result[0] += v[i-1]
            result[1] += "_"
            return result


def GlobalAlign(v, w, scorematrix, indel):
    s = numpy.zeros((len(v)+1,len(w)+1), dtype="int32")
    b = numpy.zeros((len(v)+1,len(w)+1), dtype="int32")
    for i in xrange(1,len(v)+1):
        for j in xrange(1,len(w)+1):
            score = s[i-1,j-1] + scorematrix[v[i-1],w[j-1]]
            vskip = s[i-1,j] + indel
            wskip = s[i,j-1] + indel
            s[i,j] = max(vskip, wskip, score)
            if (s[i,j] == vskip):
               b[i,j] = 1
            elif (s[i,j] == wskip):
               b[i,j] = 2
            else:
               b[i,j] = 3
    return (s, b)


match = {('A','A'):  2, ('A','C'): -2, ('A','G'): -1, ('A','T'): -2,
         ('C','A'): -2, ('C','C'):  2, ('C','G'): -2, ('C','T'): -1,
         ('G','A'): -1, ('G','C'): -2, ('G','G'):  2, ('G','T'): -2,
         ('T','A'): -2, ('T','C'): -1, ('T','G'): -2, ('T','T'):  2}

v = "AACACAAACTGAGCCCCTACCCCAAATTAGAACTGGATCTGGACCCTTCCATTCATTAGTCAGGGGGTCCTTCCATTTTACCAATGCATA"
w = "AAAAACACAAACTGAGCCCCTACCCCAAATTAGGACTGGATCTGGACCCTTCCATTCATTAGTCAGGGGGTCCTTCTATTTTACCAATGT"

s, b = GlobalAlign(v, w, match, -3)
align = Alignment(b, v, w, b.shape[0] - 1, b.shape[1] - 1)

print "score =", s[b.shape[0] - 1, b.shape[1] - 1]
print "v =", align[0]
print "w =", align[1]