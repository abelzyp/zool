"""
序列:
1.成员操作 in、not in
2.连接操作 +
3.重复操作 *
4.切片操作 [:]
"""

# 记录生肖，根据年份判断生肖

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# print(chinese_zodiac[0:4])

# print(chinese_zodiac[-1])

year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])

print('狗' not in chinese_zodiac)
print(chinese_zodiac + chinese_zodiac)
print(chinese_zodiac * 2)
