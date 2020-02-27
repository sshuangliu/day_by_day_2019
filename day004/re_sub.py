# coding:utf-8

# 引入正则表达式模块
import re


#############################
# 需求一：
# 需要把一个数字和一个字母组合替换成"("左括号，再把一个字母和一个数字的组合替换成")"右括号。
# 注意我说的数字和字母顺序，例如："4j"将替换成"("；"j4"将替换成")"

# 替换方法
def repl_text(content):
    text = re.sub(r'\d[a-z]', '(', content)
    text = re.sub(r'[a-z]\d', ')', text)
    return text


# 原文本内容
content1 = '34jehsekh413kjlwjk352121j5h43j5'

# 执行替换并输出结果
print(repl_text(content1))


###############################################################

# 需求二：
# 例如再加个条件，如果是数字4开头的不替换
# 替换方法
def repl_method(match):
    # 匹配到的内容
    text2 = match.group()
    print(text2)

    # 判断是不是字母和数字组合
    if re.search(r'^[a-z]\d$', text2):
        result = ')'
    elif text2[0] == '4':
        # 判断开头是否是4，若是的话，返回原文本
        result = text2
    else:
        result = '('

    # 返回替换的结果
    return result


conten2 = '34jehsekh413kjlwjk352121j5h43j5'

text2 = re.sub(r'\d[a-z]|[a-z]\d', repl_method, conten2)
print(text2)



###################
#需求三
#IP地址最后一组的替换

ipv4add = '24.53.133.243'
def ipv4add_def(match_obj):
    obj_001 = match_obj.group()
    print(obj_001)
    if re.match()




new_ipv4add = re.sub(r'\d{1,3}',ipv4add_def,ipv4add)
print(new_ipv4add)

re.sub(r'\d+$','1',ipv4add)
re.sub(r'^\d+','1',ipv4add)


re.findall(r'(\d)(\d+)',ipv4add)
# [('2', '4'), ('5', '3'), ('1', '33'), ('2', '43')]