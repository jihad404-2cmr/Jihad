dic = {
    "username": "ali",
    "pass": "12345678",
    "name": "ali ahmed",
    "age": 21,
    "mail": "ali@mail.ru",
}

attempts = 3 

while attempts > 0:
    user_input = input("enter the username : ").strip()
    pass_input = input("enter the password : ").strip()


    if user_input == dic.get("username") and pass_input == dic.get("pass"):
        print(f"\n oh hiii ، {dic.get('name')}!")
        print("information about the account in the dictionary :")
        for key, value in dic.items():
            print(f"{key}: {value}")
        break  

    
    attempts -= 1
    if attempts > 0:
        print(f"failed ... the password or the username is incorrect ...so you have {attempts} attempts.\n")
    else:
        
        dic.pop("username", None)
        dic.pop("pass", None)
        dic["locked"] = True
        print("\nfailed for three times.")
        print("the data removed and the account locked)
