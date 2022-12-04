n = int(input())

zodiac_forward = ('Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox')
zodiac_backward = ('Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat')
#Mildred born in previous Dragon year from Bessie
name1 = []
name2 = []
forward = []
year = []
cow_to_year = {}
calendar = {}
for i in range(n):
    line = input().split()
    name1.append(line[0])
    name2.append(line[7])
    forward.append(True) if line[3] == 'next' else forward.append(False)
    year.append(line[4])
    cow_to_year[name1[len(name1)-1]] = year[len(year)-1]
cow_to_year['Bessie'] = 'Ox'
calendar['Bessie'] = 0
prev = name2.index('Bessie')
prevCow = name1[prev]
if(forward[prev]):
    start_difference = zodiac_forward.index(year[prev]) + 1
else:
    start_difference = -(12 - zodiac_backward.index(year[prev]))
calendar[name1[prev]] = start_difference
#print(start_difference)
prev_year = year[prev]
name1.pop(prev)
name2.pop(prev)
forward.pop(prev)
year.pop(prev)
curr_index = prev
for i in range(n-1):
    if(prevCow in name2):
        curr_index = name2.index(prevCow)
    else:
        for name in name2:
            if(name in calendar.keys()):
                curr_index = name2.index(name)
                prev_year = cow_to_year[name]
                prevCow = name
                break
    if(forward[curr_index]):
        if(zodiac_forward.index(prev_year) > zodiac_forward.index(year[curr_index])):
            diff = calendar[prevCow] + 12 - zodiac_forward.index(prev_year) + zodiac_forward.index(year[curr_index])
        else:
            diff = calendar[prevCow] + zodiac_forward.index(year[curr_index]) - zodiac_forward.index(prev_year)
    else:
        if(zodiac_backward.index(prev_year) < zodiac_backward.index(year[curr_index])):
            diff = calendar[prevCow] - (12 - zodiac_backward.index(year[curr_index]) + zodiac_backward.index(prev_year))
        else:
            diff = calendar[prevCow] - zodiac_backward.index(year[curr_index]) + zodiac_backward.index(prev_year)
        
    calendar[name1[curr_index]] = diff
    #print('{} : {}' .format(name1[curr_index], diff))
    prevCow = name1[curr_index]
    prev_year = year[curr_index]
    name1.pop(curr_index)
    name2.pop(curr_index)
    forward.pop(curr_index)
    year.pop(curr_index)


answer = abs(calendar['Bessie'] - calendar['Elsie'])
print(answer)
