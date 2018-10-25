import math
from Queue import ArrayQueue

def radixsort(X):
    bin_ = [ArrayQueue() for _ in range(10)]    #Creates a seperate category for each digit 0-9
    maxdig = int(math.ceil(math.log(max(X),10)))    #Checks the number with the highest number of digits

    for i in range(maxdig):     #Runs for the highest number of digits
        for j in X:     #Cycles through the array
            digit = j // 10**i % 10     #Gets the digit for that member of the array
            bin_[digit].enqueue(j)      #Places the member of the array in the appropriate category based on the digit

        t = []      #Seperate array to hold each iteration of the sorted array
        for binnum in bin_:
            while not binnum.is_empty():
                t.append(binnum.dequeue())      #Dequeues the numbers stored in the bins
        for k in range(len(X)):     #Copies the final iteration of t back into X
            X[k] = t[k]





X = [64, 32, 45555, 5, 2]
radixsort(X)
for k in range(len(X)):
    print(X[k])