#1789 수들의 합 근의 공식과 수열의 합 이용
from sys import stdin





input=stdin.readline





s=int(input())





a=(-1+(1+8*s)**(1/2))/2


b=(-1-(1+8*s)**(1/2))/2




print(int(max(a,b)))

