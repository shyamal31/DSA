#remove all the a's from the string
##1 using processed and unprocessed string in the argument of the function
def removea(p,up):
    if len(up) == 0:
        print(p)
        return 
    ch = up[0]
    if ch == 'a':
        removea(p,up[1:])
    else:
        removea(p+ch,up[1:])


removea("","abcbaabd")

#method2. without using arguments passig the string into the function body

def removea2(s,index):
    new_str = ''
    #base condition
    if index == len(s):
        return ''

    ch = s[index]
    if ch == 'a':
        old_str = removea2(s,index+1)
        new_str+=old_str
        return new_str
    else:
        new_str+=ch
        old_str = removea2(s,index+1)
        new_str+=old_str
        return new_str

print(removea2('ababcaaaaa',0))
