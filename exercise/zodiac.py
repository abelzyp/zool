"""
元组不增删数据
列表一般可以增删数据
"""

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21))

(month, day) = (2, 15)

zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# print(zodiac_days)
zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_name[zodiac_len])

# 列表
a_list = ['abc', 'xyz']
print(a_list)
a_list.append('X')
print(a_list)
a_list.remove('xyz')
print(a_list)
