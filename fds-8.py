post = input("what is the post")
days = int(input("how many days of working"))
which_month = input("which month ")
month = {"jan":31, "feb" : 29, "mar" : 31,"apr" : 30, "may":31,"jun":30,"jul":31,
       "aug":31, "sep":30, "oct" : 31, "nov":30,"dec":31}
salary=0
if post == "manager":
    if days <= month[which_month]:
        salary += days * 2000
        ask_overt = int(input("how many days of overtime"))
        if ask_overt >= 0:
            salary += ask_overt*(2000/2)
            print(salary)
    else:
        print("wrong input")

elif post == "teamleader":
    if days < 32:
        salary += days * 1800
        ask_overti = int(input("how many days of overtime"))
        if ask_overti >= 0:
            salary += ask_overti*(1800/2)
            print(salary)
    else:
        print("wrong input")

elif post == "member":
    if days < 32:
        salary += days * 1500
        ask_overtim = int(input("how many days of overtime"))
        if ask_overtim >= 0:
            salary += ask_overtim*(1500/2)
            print(salary)
    else:
        print("wrong input")