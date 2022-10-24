#count will count up amount of senders found, duplicates included

count = 0
#setting file to variable and opening file
# setting file to be opened, read and read all lines

f = open('mbox-short.txt', 'r')

sender_values = []

for line in f:
    if (line[0:5] == 'From '):
        sender_values.extend(word for word in line.split() if '@' in word)
        count = count + 1
# print(count, 'is amount of gathered contacts, dupes included')
senders = [*set(sender_values)]
# print(senders)
# *set() will find and remove duplicates in list and return as new list

# See about mapping to organize list into further detailed list
# find way to implement find method ex: locater = senders[1].find("@") or maybe just split
pref = []
dom = []
two_parts = []
for i in range(len(senders)):
    two_parts.extend(senders[i - 1].split('@'))

# print(two_parts)

dom = two_parts[1::2]
pref = two_parts[0::2]
dom = [*set(dom)]
# print(dom)
# print(pref)

pref_dict = {}
dom_dict = {}
#convert list to dictionary using zip method
def dict_maker(x, y):
    it = iter(x)
    y = dict(zip(it, x))
    print(y)
    return y

dom = dict_maker(dom, dom_dict)
pref = dict_maker(pref, pref_dict)
print(dom,'\n', pref)
