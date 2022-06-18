import json,re
print("welcome to login signup page")
file=input("enter the login signup:-")
if True:
    if file=="signup":
        a = open("details.json","r")
        c = a.read()
        data = json.loads(c)
        username=input("enter the name-:")
        surename=input("enter the surename")
        mobile_number=int(input("enter the mobile number-:"))
        if (len(str(mobile_number)))==10:
            otp=int(input("enter the otp-:"))
            if (len(str(otp)))==6:
                date_of_birth=input('enter the date of birth:-')
                gender=input('enter the gender-:')
                if gender=="female" or gender=="male" or gender=="other":
                    bio=input("enter your bio:-")
                    password=input("enter your password-:")
                    if re.fullmatch(r'[A-Z a-z 0-9 @#$&]{8,}',password):
                        print("strong password-:")
                        confrom_password=input("enter your confrom password-:")
                    
                        username = {"username":username,"surname":surename,"mobile_number":mobile_number,"otp":otp,"date_of_birth":date_of_birth,"gender":gender,"bio":bio,"password":password}
                        data.append(username)   
                        if password==confrom_password:
                            print("**registation successfuly**")    
                            with open('khushbu.json',"w") as f:
                                b=json.dump(data,f,indent=4)
                        else:
                            print("your password is wrong")
                    else:
                        print("your password is invalid")
                else:
                    print("your gender is wrong")
            else:
                print("your otp is non valid")
        else:
                print("your mobile number is non valid")
    elif file=="login":
        username=input("enter your username-:")
        password=input("enter your password-:")
        my_file=open('khushbu.json',"r")
        a=json.load(my_file)
        b={}
        for i in a:
            print(i)
            # break
        print("login successfully")
    #     c=[]
    # if username == password:
    #     c.update(login_signup)
    # print(c)
            


            
            
        




