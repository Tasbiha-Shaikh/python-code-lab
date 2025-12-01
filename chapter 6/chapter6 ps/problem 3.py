p1 = "make a lot of money"
p2 = "buy now"
p3 = "click this"
p4 = "subscribe this"

message = input("enter your comment: ")
if((p1 in message) or (p2 in message) or (p3 in message)or (p4 in message)):
    print("this comment is a spam")
else:
    print("this comment is not a spam")