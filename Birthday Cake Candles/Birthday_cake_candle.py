import os

def BirthdayCakeCandles(candles):
    max_height = max(candles)

    # Count how many candles have the maximum height
    count_max_height = candles.count(max_height)
    return count_max_height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())
    candles       = list(map(int, input().rstrip().split()))
    
    result = BirthdayCakeCandles(candles)
    
    # Write the result to the output file
    fptr.write(str(result) + '\n')
    fptr.close()
