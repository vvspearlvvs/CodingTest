'''
def birthdayCakeCandles(candles):
    maxc=max(candles)
    #temp=''.join(candles)
    c=candles.count(maxc)
    print(c)

candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
result = birthdayCakeCandles(candles)
'''

for i in range(6):
    for j in range(i+6,6):
        print("#",end='')
    print()
