from __future__ import print_function

from heapq import heappush, heappop

def main():
    heap = []
    heappush(heap, 10)
    heappush(heap, 32)
    heappush(heap, 5)
    heappush(heap, 3)
    heappush(heap, 54)
    heappush(heap, 8)
    heappush(heap, 100)

    heaplist = []
    while heap:
        heaplist.append(heappop(heap))
    
    print(' '.join(
        [str(n) for n in reversed(heaplist)]
    ))

main()