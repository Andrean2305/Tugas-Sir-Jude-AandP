def convert_to_days():
    a= eval(input("Enter number of hours: "))
    b= eval(input("Enter number of minutes: "))
    c= eval(input("Enter number of seconds: "))
    ce = get_days(a,b,c)
    print(f"The number of days is: {ce}")

def get_days(a,b,c):
    ba=((a/24)+(b/1440)+(c/86400))
    return round(ba,4)
        
convert_to_days()
