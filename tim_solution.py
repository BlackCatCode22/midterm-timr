#1 TODO: an accumulator tallies up the amount of lines found to meet your criteria; count will count up amount of senders found, duplicates included

count = 0
#setting file to variable and opening file
# setting file to be opened, read and read all lines

f = open('mbox-short.txt', 'r')
# msgs = {}
sender_values = []
#2 TODO: my_line(used in for loop to iterate through file) and my_file_handle(locates text file and opens setting it to either r(read), w(write), or a(append))
for line in f:
    #3 TODO: includes first 5 characters through each line, used to locate sender portions of text
    if (line[0:5] == 'From '):
        #4 TODO: elements of a list are each indexes data
        sender_values.extend(word for word in line.split() if '@' in word)
        count = count + 1
        
# print(sender_values)
senders_msgs = sender_values
# print(count, 'is amount of gathered contacts, dupes included')
#5 TODO: produces the prefix@domain after the 'From ' conditional
#6 TODO: splitting the prefix and domain @ the '@' into to separate list indexes
#7 TODO: from what I've read online ++/-- operators allow for error so clarification is needed in Python
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
sender_dict = {}
#convert list to dictionary using zip method
def dict_maker(x, y, z = 0):
    for z in range(len(x)):
        z = z + 1
        # z not in use anymore but leaving for question
    it = iter(x)
    y = dict(zip(x, it))
    # print(y)
    return y
list_pref = pref
dom = dict_maker(dom, dom_dict)
pref = dict_maker(pref, pref_dict)
# print(dom,'\n', pref)
#reminder to ask professor mohle how to better iterate so that each key increases by 1 instead of using key and val to be the same

# converted wrong part into dictionaries for assignment
sender_values = dict_maker(sender_values, sender_dict)
# print(sender_values)
# print(list_pref)
new_counter = 0
for i in range(len(list_pref)):
    # print(sender_values)
    # print(list_pref[3])
    first_val = list(sender_values.values())[i]
    if list_pref[i] in sender_values:
        new_counter = new_counter + 1
        print(list_pref[i], 'has:', new_counter, 'msgs')
    # print(sender_values)


msgs_sent_per = {}
for i in senders_msgs:
    print(senders_msgs.count(i))
# print(msgs_sent_per)


# print(sorted(sender_values.keys()))

# print(sorted(sender_values.values()))
# print(new_counter)
# 8 TODO: C++
# 9 TODO: tallies up the amount of message sent per prefix
# 10 TODO: Java
