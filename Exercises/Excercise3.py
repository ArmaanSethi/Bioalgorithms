# given the following text
text = "imissmissmississippiskiss$"

# use a suffix array to find all occurrences
# of the substring "iss" in text, and print
# the index and suffix of each occurrence.
#
# Your answer should look like:
# 22 iss$
# 13 issippiskiss$
# 10 ississippiskiss$
# 6 issmississippiskiss$
# 2 issmissmississippiskiss$

def suffixArray(string):
    return [index for suffix, index in sorted((string[i:], i) for i in range(len(string)))]

def findFirst(pattern, text, suffixarray):
    lo, hi = 0, len(text)
    while (lo < hi):
        middle = (lo+hi)//2
        if text[suffixarray[middle]:] < pattern:
            lo = middle + 1
        else:
            hi = middle
    return lo

def findLast(pattern, text, suffixarray):
    lo, hi = 0, len(text)
    while (lo < hi):
        middle = (lo+hi)//2
        if text[suffixarray[middle]:suffixarray[middle]+len(pattern)] <= pattern:
            lo = middle + 1
        else:
            hi = middle
    return lo

sb = suffixArray(text)
print(sb)

lo = findFirst('iss', text, sb)
hi = findLast('iss', text, sb)

print(lo, hi)

for i in range(lo,hi):
    print(text[sb[i]:])