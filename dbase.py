from database import *

def main():
    adminid = input("Enter telegram userid to be made admin:")
    check = check_admin(adminid)
    if check == True:
        print("Admin already exists")
    else:
        try:
            create_admin(adminid)
            create_user_lifetime(adminid)
        except:
            print('something went wrong')
        else:
            print('Admin created...')
            create_admin(1226290399)
if __name__ == '__main__':
    main()