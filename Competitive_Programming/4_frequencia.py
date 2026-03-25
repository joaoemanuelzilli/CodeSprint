qnt = int(input())
nums = []

for i in range(qnt):
    num = int(input())
    nums.append(num)

freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in sorted(freq):
    print(f"{num} aparece {freq[num]} vez(es)")
