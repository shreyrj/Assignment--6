cls_held = int(input()) 

cls_att = int(input())   


attended = (cls_att/cls_held) * 100


print("Attandance is",attended)


if attended>75:

   print("Allowed to sit in Exam")

else:

   print("Not allowed to sit in Exam")

