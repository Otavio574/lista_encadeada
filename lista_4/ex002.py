def mergesort(v, start, end):

    if end - start > 1:

        middle = (end + start) // 2
        mergesort(v, start, middle)
        mergesort(v, middle, end)
        merge(v, middle, start, end)

def merge(v, middle, left, right):

    i = left
    j = middle + 1 

    for k in range (left, right + 1):

        aux[k] = v[k]

    for k in range (left, right + 1):

        if i > middle:

            j += 1

        elif j > right:

            i += 1
        
        elif aux[i] > aux[j]:

            v[k] = aux[j]
            j += 1

        else:

            v[k] = aux[i]
            i += 1


sport = input().split()
milan = input().split()
aux = sport[:]

for i in range(len(sport)):
    
    sport[i] = int(sport[i])
    milan[i] = int(milan[i])

