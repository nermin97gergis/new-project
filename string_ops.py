def repeated_substring(word):
   # word=input()
    string=""
    for ch in word:
        string=string+ch
        count=word.count(string)
        t=len(string)
        if t*count==len(word):
            tuple=(string, count)
            return(tuple)
repeated_substring('ababab')






def is_palindrome(text):
    text=str(input())
    text= text.replace(" ","")
    text= text.upper()
    if len (text)>1:
        if text==text[::-1]:
            return("palindrome")
        else:
            return("not palindrome ")
    else:
        return("empty string")


is_palindrome('text')

def solve(a,b):
       a=input()
       b=input()
       x="*"
       tup=(a,b)
       if a==b:
           return((tup,True))

       elif x in a:
           if(len(a)-1)<=len(b):
               return((tup,True))
           else:
              return ((tup,False))
       else:
           return((tup,False))



solve('a','b')













