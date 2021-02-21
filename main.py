# import tryalgo
# import math
# from collections import defaultdict
import sys
# import os

def main():
   # height, width = map(int, sys.stdin.readline().split())
   # print(str(height) + "  " + str(width))
   # instance = list(map(int, os.read(0, 3333).split()))
   # g = defaultdict(dict)
   # nb_edges = int(input())
   # for _ in range(nb_edges):
   #    u, v, weight = input().split()
   #    g[u][v] = int(weight)
   #    # g[u][v] = int(weight) # For undirected graph
   # print(g)
   n, k = map(int, sys.stdin.readline().split())
   ans = 0
   for i in range(n):
     x = int(sys.stdin.readline())
     if (x % k == 0):
        ans = ans + 1
   sys.stdout.write(str(ans))

if __name__ == "__main__"  :
   main()