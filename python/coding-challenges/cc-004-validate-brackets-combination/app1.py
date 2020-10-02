# Write a function that given a string containing just the characters 
# `(`, `)`, `{`, `}`, `[` and `]`, determines if the input string is 
# valid or not by using following rules.
validation_dic= {"(":")", "{":"}", "[":"]"} 
validation_list = ["(", ")", "{", "}", "[", "]" ]
user = input("Please enter the characters `(`, `)`, `{`, `}`, `[` and `]` with \
    closing pair components for being validation\n")
user_list = list(user)
result = False
def x():
    user_iter = iter(user_list)
    next(user_iter, user_list[-1])
    for a, i in enumerate(user_list):
        b=next(user_iter,user_list[-1])
        if i in validation_dic.keys():
            if b == validation_dic[i]:
                if b == user_list[-1] and len(user_list)<3:
                    global result 
                    result = True
                    break
                user_list.pop(a)
                user_list.pop(a)
                x()
if len(user) == 0:
    result = True
else:
    x()
if result:
    print("true")
else:
    print("false")