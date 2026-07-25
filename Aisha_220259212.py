#203,Aisha Husam Mahmoud Jawanah _220259212 & 201,Dima Mohammed Omer Balousha_220252459
# # Address Book System


contact=[]    # empty list to store contacts


while True:   # loop to keep the program running until the user decides to exit
    print('Welcome to our Address book ,please to find what you want')
    print('1.Add new contact\n2.Search by name\n3.Search by number\n4.Delete contact by name\n5.Delete contact by number\n6.Show all contacts\n7.Exit')
    choice=(int(input('Please to enter your choice: ')))  # asking the user to enter their choice as integer

# user chooses to add a new contact
    if choice==1:
        name=(input('Enter contact name: '))       # enter the contact's name that will be added
        type=(input('Enter contact type: '))       # enter the contact's type that will be added
        number=(input('Enter contact number: '))   # enter the contact's number that will be added


        allow_type=['Family' , 'Personal' , 'Work' ,'Other']   # the types rhat can be used for the contact



        if type not in allow_type:           # if the user enter a type that is not in the allowed types
          print('Note:Invalid type.It will be considered as others.')
          type='others'          # if the user enter a new type it will be considered as Other


        is_reserved=False        #assume  the number is not in the system


        for c in contact :       # loop through the contact list to check if the number is already reserved  
           if c[2]==number:
              is_reserved=True
              break
           

        if is_reserved:          # if the number is reserved
            print('Error:This number is already reserved.Process rejected.')
        else:                 # if the number is not reserved
            contact.append([name,type,number])
            print('Process is success:Contact added.')


# user chooses to search for a contact by name
    elif choice==2:
        search_name=input('Enter name to the search: ')
        found=False


        for c in contact:
          if search_name in c[0]:
             print('found',c)
             found=True

        if found==False:
           print('Not found')
        print('Process is success:Search completedn.') 

# user chooses to search for a contact by number
    elif choice==3:
        found=False

        search_number=input("Enter number to the search: ")
        for c in contact:      # loop through the contact list to find the number
           if search_number== c[2]:   # if the number is found in the contact list
               print("contact is found", c ) 
               print("Process is success: Search completed. ")
               found=True
               break 
        else :       # if the number is not found in the contact list
            print("Not found")


# user chooses to delete a contact by name
    elif choice==4:
       delete_name=input("Enter the contact's name to delete: ")  
       remove_list = []             #variable holds the contact we want to keep   
       for c in contact:
          if c[0] == delete_name:
              remove_list.append(c) 
       for r in remove_list:
          contact.remove(r)
       if remove_list != []: 
          print("Process is success: delete completed.")
          print(len(remove_list),'contact(s)delete')
       else:
          print("Not found")


# user chooses to delete a contact by number
    elif choice==5:
       delete_number=input("Enter the contact's number to delete: ")
       found = False
       for num in contact:
          if delete_number==num[2]:
              contact.remove(num)    
              print('Process Success: delete completed.')
              found = True   
              break
       if not found:     
          print('Not found')


# user chooses to show all contacts
    elif choice==6:
       if contact != []:
          for c in contact:
             print( c[0], c[1], c[2] )
          print("Process is success: Show completed.")
       else:
          print('No contacts to show')
    
    
# user chooses to exit the program
    elif choice==7:
       print('Exiting...')
       break
    

    else:
       print("Error:Invalid choice")