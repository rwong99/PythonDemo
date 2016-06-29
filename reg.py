import re

secret_code = 'asdwefjxxIxxsahdweu4xxLOVExxhuiehuwerj22wxxYOUxxhsfhwrijfhf'

# a = 'abc123'
# b = re.findall('a..',a)
# print(b)

# a = 'xyxyxy123'
# b = re.findall('x*',a)
# print(b)

# a = 'xy123'
# b = re.findall('x?',a)
# print(b)

# # .*是一个贪心做法，尽可能多吃
# b = re.findall('xx.*xx',secret_code)
# print(b)
# # 。*？像一个婴儿，少吃多餐
# c = re.findall('xx.*?xx',secret_code)
# print(c)
# d = re.findall('xx(.*?)xx',secret_code)
# print(d)
# for each in d:
#     print(each)

# re.S可以让点号查找换行符
s = '''adddxxHello
xxfdsssxxWorldxxlkk...'''
d = re.findall('xx(.*?)xx',s,re.S)
print(d)

# \d+匹配纯数字
s2 ='axx12345jdijfxx555jf'
num = re.findall('(\d+)',s2)
num2 = re.findall('xx(.*?)xx',s2)
print(num2)
print(num)