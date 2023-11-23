from collections import Counter

word = 'абракадабра'
letter_cnt = Counter(word)

print(letter_cnt)
print(letter_cnt['а'])
print(letter_cnt['ю'])
print(letter_cnt.most_common(2))



letter_cnt['ю'] = -1
print(+letter_cnt)
print(-letter_cnt)



word2 = 'абырвалг'
letter_cnt2 = Counter(word2)
print(letter_cnt2)


print(letter_cnt - letter_cnt2)
print(letter_cnt + letter_cnt2)


print(letter_cnt | letter_cnt2)
print(letter_cnt & letter_cnt2)


