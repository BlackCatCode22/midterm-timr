
f = open('mbox-short.txt', 'r')

msgs = dict()

for line in f:
    if (line[0:5] == 'From '):
        list_words = line.split()
        parts = list_words[1].split('@')
        pre = parts[0]
        doma = parts[1]
        print(pre)
        # print(doma)
        if (pre in msgs):
            # print(msgs[pre], ' ', pre, ' exists as a key in this dictionary')
            msgs[pre] = msgs[pre] + 1
        else:
            msgs[pre] = 1

big_count = None
big_word = None

for my_key, my_val in msgs.items():
    if big_count is None or my_val > big_count:
        big_word = my_key
        big_count = my_val

# print('\n Most messages is by...')
# print(big_word, big_count)

# print('\n the msgs dict is :')
# print(msgs)
