import sys
def initial_phonebook():
    rows,cols=int(input("Please enter number of contacts:")),5
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("Enter the contact %d details in the following order:"%( i+1))
        print("Note: indicates mandatory fields")
        print("...............................................................................")
        temp=[]
        for j in range(cols):
            if j==0:
                temp.append(str(input("Enter the name*: ")))
                if temp[j]=='':
                    sys.exit("Name is a mandatory field. Exiting due to empty name.")

            if j==1:
                temp.append(int(input("Enter the number*: ")))
 
            if j==2:
                temp.append(str(input("Enter the email address: ")))
                if temp[j]==' ' or temp[j]== ' ':
                    temp[j]=None
            if j==3:
                temp.append(str(input("Enter date of birth in format (dd/mm/yyyy): ")))
                if temp[j]=='' or temp[j]=='  ':
                    temp[j]=None

            if j==4:
                temp.append(str(input("Enter category(Family/Friends/Work/Others): ")))
                if temp[j]=='' or temp[j]==' ':
                    temp[j]=None
    print(phone_book)
    return phone_book
initial_phonebook()


    