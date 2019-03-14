s="asdasfasf\tsadsf\tasdqwexzc"
s.expandtabs(6)
print(s, "s.expandtabs(6)=", len(s))
print("#################################")

s1="asdasfasf1234asda"
s2="asdasfo_*&12esadf"
print(s1 , "s1.isalnum()=" , s1.isalnum())
print(s2 , "s2.isalnum()=" , s2.isalnum())

print("#################################")

s1="asdasfasf1234asda"
s2="asdasfoasdsafas"
print(s1 , "s1.isalpha()=" , s1.isalpha())
print(s2 , "s2.isalpha()=" , s2.isalpha())


print("#################################")

s1="②③"
s2="23"
s3="二"

print(s1 , "s1.isdecimal()=" , s1.isdecimal())
print(s1 , "s1.isdigit()=" , s1.isdigit())
print(s1 , "s1.isnumeric()=" , s1.isnumeric())

print(s2 , "s2.isdecimal()=" , s2.isdecimal())
print(s2 , "s2.isdigit()=" , s2.isdigit())
print(s2 , "s2.isnumeric()=" , s2.isnumeric())

print(s3 , "s3.isdecimal()=" , s3.isdecimal())
print(s3 , "s3.isdigit()=" , s3.isdigit())
print(s3 , "s3.isnumeric()=" , s3.isnumeric())

print("#################################")

s="_123124asdasf"
print(s , "s.isidentifier()=" , s.isidentifier())


print("#################################")

s1="asfasdasf"
s2="asfas\t"
print(s1 , "s1.isprintable()=" , s1.isprintable())
print(s2 , "s2.isprintable()=" , s2.isprintable())

print("#################################")

s1="asfasd asf"
s2="     "
print(s1 , "s1.isspace()=" , s1.isspace())
print(s2 , "s2.isspace()=" , s2.isspace())

print("#################################")

s="chen jiang yu"
print(s , "s.istitle()=" , s.istitle())
s=s.title()
print(s , "s.istitle()=" , s.istitle())

print("#################################")

s=" join ".join("我站在烈烈风中！")
print(s)

print("#################################")

s="string"
print(s.ljust(20,"a"))
print(s.rjust(20,'1'))

print("#################################")

print("#################################")

s="String"
print(s , "s.islower()=" , s.islower())
s=s.lower()
print(s , "s.islower()=" , s.islower())

print("#################################")

s="String"
print(s , "s.isupper()=" , s.isupper())
s=s.upper()
print(s , "s.isupper()=" , s.isupper())

print("#################################")

s="      \tstring\n        "
s1="string"
print(s.lstrip())
print(s.rstrip())
print(s1.rstrip("ing"))
print(s.strip())

print("#################################")

s1="asdjifmsaoqtmdadsfasdgio"
s2=str.maketrans("aeiouy","012345")
s1=s1.translate(s2)
print(s1)

print("#################################")

s1="asdsfjasfdoisdfsds17sdf"
print(s1.partition("s"))
print(s1.rpartition("s"))

print(s1.split("s"))
print(s1.split("s",2))