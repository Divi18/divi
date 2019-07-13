n=input()
l1=["a","e","i","o","u"]
if n.isalpha():
  if n in l1:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("Invalid")
