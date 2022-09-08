import re
text_ = '“I want to go to the grocery store'
def firstSolution(text):
    return {i:re.findall(r'\w+', text).count(i) for i in re.findall(r'\w+', text)}
def secondSolution(text):
    dic = {}
    for j in re.findall(r'\w+', text):
        if j in dic:
            dic[j] +=1
        else:
            dic[j] =1
    return dic
print('By first solution : ',firstSolution(text_))
print('By second solution : ',secondSolution(text_))
   