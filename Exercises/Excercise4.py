bwt = "CTTACTTGTTATTTTATTTCTTTTTTTTGTTTTTTTTCATTCTTTTTTGTTGTTTTTTTT" \
    + "TTTTTTCTTTTATTCTTTGATTTTTTCGTTTTTGTATTCTTTCTAATTTGTTTTTTGTGC" \
    + "GTTTTTTGATTTCGTGTATTTTTTTTTTTTTTTTGTTTCTTTTTTTTTTTTTGTCTTTTT" \
    + "TTTTTTTTTTTTGGTTGTTGTTTTTTGGTTTTTTTTATATTTTTCCTTTTTTTTTCGTTA" \
    + "TTTTTGTTTATTTTTTTTTACTCTCGTATTGTTTGTCCTTATTTTTTTAATTTTTCTTTA" \
    + "TTTTTTTGTTTTTTTTTTTTACTTCTTGTTTTTTTTTATCGTTTTTTTTTTTTTTTTGTT" \
    + "TATTCATTTTTTTTTTTTTTTTTCTTTTTTTTGCTTTTTTATTATATTTTTTTTTTAGTT" \
    + "TTTTTTTTTTTTTAATTTATTCTTTTTTTTTTTTTTTTTTTATCTATTTTTTTCTTTTTT" \
    + "TTTATTTACTATCTTTTTTTTTGTTTGTTTTATTTTTTTTTATTATTTTTTTTTTTTTTC" \
    + "CTTTTTGTTTTTTTTATTTTTTTTATTTATTTTTATATTTTTTTTTTTGTTTCTTTTTTC" \
    + "TCGTTTTTTTATGAGTTTGTTGCTTTTTCGAATGTTCTTTTTTTCTTTTTTTATTTTTGT" \
    + "CGTTCTTTTTTTGTTTTTCTTATTTTTTCTTCGTTCATTTTTTTGCGTTTTTTTCTTTTT" \
    + "TTTATGTTTTCTTTGCTTTTTTTTTTTTTTTTTTTTTTCCTTTTTTTTTCTTTTTTTTTT" \
    + "TTCTATTTTCTTCTTTGTTTCTTTTTTTGTTTTTACTTTTGAGATTTCGATTTTTTTTTT" \
    + "GACTTTTTTTAATGCCTTTTTTTTGTTTTTCTTTATTTATTCTTTATTGTTTTTTATTCT" \
    + "TCTGACTTCTTTTATCGTTTTTTTTTGCTTCCTTTTTTTTTGTATTTGTTCTTTTTTTTT" \
    + "ATTTTTTTTTTTTTTTTATATTTTCTAGTTATTTTTTTTTTTCTGTTCTTTTTTTTTTTT" \
    + "TTTTTGATTATTTCTGGTTGGTTAT$TTTTTTTTTTATTTTCGTTATTTTTATTTGCGTT" \
    + "TTTTTTCATTGTTTTTTTAGTTTTTTTCTACTTTTTTTTACTTTTTCTTTTTTTATTTGT" \
    + "TTTTCTTCTTCCTCTCTCTTTTGTTTCCTTTTTTACTTATTTTTTTTGTTTCTTGGTTGT" \
    + "TTTTGTGTCTTTTATTTTTTTTTTCTTGGTTTTTTTCTAATATTCTTTTCTTTTTTATTT" \
    + "CCTTCTTTTTTTTTTGTGTTTTTTTTGTTTTTTTTTTGTTTTTACTCTTATTGTTTCTTT" \
    + "TTTATCTTTTTTTTTCTTTTTTTTTTTTTTTTGTTTTTTATTTTTTTTAATTTTTTCTTT" \
    + "TACGTTATTTTTTTGTGTTTTTTCTTTTTTTTATTTGTTTTTTTTTTTCTTTTTTTGTTT" \
    + "GTTTCCTGTTTCTTTTTGTTTTTTTACTTTATTTTTTCTTTTTTTTTTTTATGTCTCTTT" \
    + "TTGTTTTTTAATTTATTTTTTTTTTTTTATTTTTTTTTTTTTATTTGTTATGTTTGTTTT" \
    + "TTATTTTTTTCTTTCTTATGATCGAATTTTTTCTCTTTTTTTTCTTTTTTTCGTCACTAT" \
    + "TTTCTTTTTTATTTTTTGTTACATTTTTTTTTGTGTTTGTTGCTTTGTTTGTGTTTTTTT" \
    + "TGTTATTTTTTTTGTTCTTTTTTTTTTTTTCTCTTGTTTTGTTTCTCTTTTTTTTTTATT" \
    + "TTTTTCTTTTTTTTTTTTTTCATTTTTTTTATTTTTTTTTATTTTTAGGCTTTTGTTTGT" \
    + "TTTCTATTTTTTTTGTTTTATCTTTTTGTTTCCTTTTTTTTTAGTTATCTTCTATTTTAC" \
    + "TTTTTTTTTATTTTTTTTTTTTTACTTTATTTTTTTTTTTGTCTCTAGATTTTTTTTTTT" \
    + "TTTTTTTTTTATTTCTTTTTTTTTGTTTGTTCGTATTTATTTTTTTATTTTTTATTGTGT" \
    + "TCTTTTTTTTTCTTGCGTTTC"

def findBWT(pattern, FMIndex, Offset):
    lo = 0
    hi = len(FMIndex) - 1
    for symbol in reversed(pattern):
        lo = Offset[symbol] + FMIndex[lo][symbol]
        hi = Offset[symbol] + FMIndex[hi][symbol]
    return lo, hi

def FMIndex(bwt):
    fm = [{c: 0 for c in bwt}]
    for c in bwt:
        row = {symbol: count + 1 if (symbol == c) else count for symbol, count in fm[-1].items()}
        fm.append(row)
    offset = {}
    N = 0
    for symbol in sorted(row.keys()):
        offset[symbol] = N
        N += row[symbol]
    return fm, offset

fm, offset = FMIndex(bwt)
pattern = "TA"

while True:
    lo, hi = findBWT(pattern, fm, offset)
    if (hi - lo > 0):
        print(hi-lo, pattern)
        pattern = "T" + pattern
    else:
        break
