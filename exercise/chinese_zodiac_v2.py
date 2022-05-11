"""
序列:
1.成员操作 in、not in
2.连接操作 +
3.重复操作 *
4.切片操作 [:]
"""

# 记录生肖，根据年份判断生肖

chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# year = int(input('请输入出生年份'))

# if chinese_zodiac[year % 12] == '狗':
#     print('狗年运势...')

for cz in chinese_zodiac:
    print(cz)

for i in range(1, 13):
    print(i)

for year in range(2000, 2019):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))
