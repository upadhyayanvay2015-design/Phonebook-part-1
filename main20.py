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
        phone_book.append(temp)
    print(phone_book)
    return phone_book

def menu():
    print("\nPlease select an option from the menu below:")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Display all contacts")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice
def add_contact(phone_book):
    dip=[]
    for i  in range(len(phone_book[0])):
        
        if i==0:
            dip.append(str(input("Enter name*:")))
        if i==1:
            dip.append(str(input("Enter number*:")))
        if i==2:
            dip.append(str(input("Enter email:")))
        if i==3:
            dip.append(str(input("Enter date of birth:")))
        if i==4:
            dip.append(str(input("Enter category:")))
    phone_book.append(dip)
    return phone_book

def remove_contact(phone_book):
        query = str(input("Enter the name of your contact you want to delete: "))
        temp=0
        for i in range(len(phone_book)):
            if query==phone_book[i][0]:
                temp+=1
                print(phone_book.pop(i))
                print("Contact deleted succesfully!")
                return phone_book
                if temp==0:
                    print("Contact not found!")
        return phone_book
    
def delete_all(phone_book):
    phone_book.clear()
    print("All contacts deleted!")
    return phone_book

def search_contact(phone_book):
    query = str(input("Enter the name or number to search:"))
    temp=[]
    check =-1
    for i in range(len(phone_book)):
        if query==phone_book[i][0] or query==str(phone_book[i][1]):
            temp.append(phone_book[i])
            check+=1
            if check==1:
                print("Contact found:")
                print(temp)
                return phone_book
            
def display_contacts(phone_book):
    if not phone_book:
        print("No contacts to display!")
    else:
        for i in range(len(phone_book)):
            print(phone_book[i])
    return phone_book

def thanks():
    print("Thank you for using the phone book application. Goodbye!")



ch=1
pb=initial_phonebook()
while ch!=5:
    if ch==1:
        pb=add_contact(pb)
    elif ch==2:
        pb=search_contact(pb)
    elif ch==3:
        pb=display_contacts(pb)
    elif ch==4:
        pb=remove_contact(pb)
    elif ch==5:
           pb=delete_all(pb)
    elif ch==6:
        thanks()
    else:
        print("Invalid choice. Please try again.")
    ch=menu()   
        
