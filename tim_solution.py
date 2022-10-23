#initialized accumulator -- this is to keep track of each line of the file that has a keyword

count = 0
#setting file to variable and opening file
# setting file to be opened, read and read all lines

f = open('mbox-short.txt', 'r')
# msgs = dict()

# for line in f:
#     if (line[0:5] == 'From '):
#         split_list = line.split()[1]
#         # print(split_list)
#         two_parts = split_list.split('@')
#         prefix = two_parts[0]
#         domain = two_parts[1]
#         # print(prefix)
#         # print(domain)
#         count = count + 1
#         if (prefix in msgs):
#             print(msgs[prefix], ' ', prefix, ' exists as a key in this dictionary')
#             msgs[prefix] = msgs[prefix] + 1
#         else:
#             msgs[prefix] = 1


# print(msgs)

# for line in f:
#     if (line[0:5] == 'From '):
#         split_list = line.split()[1]
#         new_dict = {word for word in line.split() if '@' in word}
#         print(new_dict)

senders = dict()

# def organizer_dict(f):
#     for line in f:
#         if (line[0:5] == 'From '):
#             senders = {word for word in line.split() if '@' in word}
#             # print(senders)
#             two_fer = senders.split('@')
#             pref = two_fer[0]
#             dom = two_fer[1]
#             print(pref, '\n', dom)


# organizer_dict(f)

sender_values = []

for line in f:
    if (line[0:5] == 'From '):
        sender_values.extend(word for word in line.split() if '@' in word)
        # print(sender_values)
print(sender_values)