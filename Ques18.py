s1=input("Enter your first string==")
s2=input("Enter your second string==")
if len(s1)!=len(s2):
    print("Strings are not anagrams")
else:
    if sorted(s1)==sorted(s2):
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")