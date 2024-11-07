def split_call(s):
    result=s[0]
    for char in  s[1:]:
        if char.isupper():
            result += ' '
        result += char    
    return (result.lower())
s="EatHealthFoodStayHealth"
print(split_call(s))
