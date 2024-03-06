#!/usr/bin/env python
# coding: utf-8

# In[1]:


#admin function
#admin function requirements: 
#    1. add/remove categories
#    2. add/remove/modify products

def admin_func(cat2_df, cat_admin):

    action = int(input("Enter 1 to modify product categories. Enter 2 to modify products. Enter 3 to quit. "))

    looper = 1

    while looper == 1:

        if action == 1:
            secondary_a = int(input("Enter 1 to add new category. Enter 2 to delete existing category. Enter 3 to quit. "))

            if secondary_a == 1:
                newcat = input("Enter new category name. ")

                looper2 = 1
                while looper2 == 1:
                    newcatID = int(input(f"Enter category ID for category {newcat}. "))
                    if newcatID in cat_admin.values():
                        print("Category ID in use. Please enter a new category ID number. ")
                    else:
                        looper2 = 2

                cat_admin[newcat] = newcatID
                print("Category and category ID saved. ")
                print(cat_admin)
                looper = 2

            elif secondary_a == 2:
                print(cat_admin.keys())

                looper2 = 1
                while looper2 == 1:
                    delcat = input("Enter name of category for deletion. ")
                    if delcat in cat_admin.keys():
                        looper2 = 2
                    else:
                        print("Category not in use. Try again. ")

                del cat_admin[delcat]
                print(f"Category {delcat} deleted. ")
                print(cat_admin)
                looper = 2

            elif secondary_a == 3: 
                print("Quitting. ")
                looper = 2

            else:
                print("Response not recognized. Please try again. ")

        elif action == 2:
            secondary_a = int(input("Enter 1 to add a new product. Enter 2 to remove an existing product. Enter 3 to quit. "))

            looper2 = 1
            while looper2 == 1:
                if secondary_a == 1:
                    new_prod = input("Enter new product name. ")
                    new_prod_ID = float(input(f"Enter product id for {new_prod}. "))

                    npID_checker = cat2_df['prodID'].tolist()
                    looper3 = 1
                    while looper3 == 1:
                        if new_prod_ID in npID_checker:
                            print("Product ID already in use. Please try again. ")
                        else:
                            looper3 = 2


                    new_cat_ID = int(input(f"Enter category ID for {new_prod}. "))

                    looper3 = 1
                    while looper3 == 1:
                        if new_cat_ID in cat_admin.values():
                            looper3 = 2
                        else:
                            print("Category ID not in current category ID list. Please try again. ")
                            print(cat_admin)

                    new_price = int(input(f"Enter price for {new_prod}. "))

                    new_row = [new_prod, new_prod_ID, new_cat_ID, new_price]
                    df_new_row = pd.DataFrame([new_row])
                    df_new_row.columns = cat2_df.columns.tolist()
                    cat2_df = cat2_df.append(df_new_row, ignore_index = True)

                    looper2 = 2

                elif secondary_a == 2:
                    del_prod = input("Enter product for deletion. ")
                    if del_prod in cat2_df['product'].values:
                        cat2_df = cat2_df[cat2_df['product'] != del_prod]          
                        looper2 = 2      
                    else:          
                        print("Product name is not in current available products. ")


                elif secondary_a == 3:
                    print("Quitting. ")
                    looper2 = 2
                    looper = 2
                else:
                    print("Response not recognized. Please try again. ")                          

        elif action == 3:
            print("Quitting admin function. ")
            looper = 2


        else:
            print("Response not recognized. Please try again. ")


# In[2]:


#welcome statement
#requirement: establishment of welcome statement

def welcmsg():
    
    w_mess = """\t\t\t****************************************\n
    \t\t\t****Welcome to the demo marketplace!****\n
    \t\t\t****************************************"""

    print(w_mess)


# In[3]:


#login
#requirement: login for admin and public. note that there isn't a requirement for generating a new uid!

def login_func():
    
    login_inf ={'admin': 'admin_pw',
               'howard': 'howard_pw',
               'jimbo': '1234',
               'captainbob123': 'password',
               'liz': 'jimbo1234'}

    var = login_inf.keys()

    looper = 1

    while looper == 1:
        login = input("Enter username to log in. ")
        login_pw = input("Please enter your password. ")

        try: 
            if login_inf[login] == login_pw:
                print("Login successful. ")
                looper = 2
            else:
                print("Username or credentials not recognized. ") 
        except KeyError:
            print("Username or credentials not recognized. ")

    return login


# In[4]:


#generating catalog matrix and product ID dictionary
#requirements: four columns of information AW specced products for viewing/updating by admin and public

def data_func():

    prod_name = ["boot1","boot2", "coat1", "coat2", "jacket1", "jacket2", "cap1", "cap2"]
    prod_ID = [1.1,1.2,2.1,2.2,3.1,3.2,4.1,4.2]
    cat_ID = [1,1,2,2,3,3,4,4]
    price = [100,110,125,135,75,80,30,35]

    cat2 = {'product': prod_name,
           'prodID': prod_ID,
           'catID': cat_ID,
           'price': price}

    cat2_df = pd.DataFrame(cat2)

    cat_admin = {"boots": 1,
                "coats": 2,
                "jackets": 3,
                "caps": 4}
    
    return cat2_df, cat_admin


# In[5]:


#public/purchasing function

def pubfunc(cat2_df,cat_admin):

    pub_order = {"product": [],
             "quantity": []}

    po_df = pd.DataFrame(pub_order)

    looper = 1

    while looper == 1:
        action = input("Enter product name to add to cart.\nPress 1 to go to cart.\nPress 2 to quit. ")

        test = cat2_df['product'].tolist()

        if action in test:
            try: 
                quant = int(input(f"Enter the quanty of {action} to add to cart. "))

                if quant <= 0: 
                    print("Invalid quantity. ")
                else: 
                    newrow = [action, quant]
                    po_df = po_df.append(pd.Series(newrow, index=po_df.columns), ignore_index=True)           

            except ValueError:
                print("Invalid quantity. ")

        elif action == "1":
            cart_func(po_df, cat2_df)
          
            looper = 2
        elif action == "2":
            print("Thanks for shopping at demo marketplace! ")
            looper = 2
        else:
            print("Input not recognized. Please try again. ")


# In[15]:


#cart function

def cart_func(po_df, cat2_df):
    
    #cat2_df
    
    #cat_admin_df = pd.DataFrame.from_dict(cat_admin, orient='index', columns='price')
    #cat_admin_df.index.name = "Item"

    agg_func = {"quantity": "sum"}
    po_df = po_df.groupby("product").aggregate(agg_func) 
    po_df = pd.merge(po_df, cat2_df, on="product", how="left") 

    looper = 1

    while looper == 1:

        modify_cart = input("Enter 1 to modify items in the cart; press 2 to continue. ")

        if modify_cart == "1":
            print(po_df)
            try: 
                rowmod = int(input("Enter row number of item for modification. "))
                item_quant = input(f"Enter new quantity for {po_df.index[rowmod]}. ")

                #item_quant = input(f"Enter new quantity for {po_df.iloc[int(rowmod),0]}. ")
                #how do i properly reference the row name rath
                po_df.at[po_df.index[rowmod], 'Quantity'] = item_quant
                po_df
            except (ValueError, IndexError):
                print("Input not recognized. Please try again. ")

        elif modify_cart == "2":
            tot_cost = (po_df['quantity'] * po_df['price']).sum()
            print(f"Total price is ${tot_cost}. Checking out. ")
            payup(tot_cost)
            looper = 2
        else:
            print("Input not recognized. Please try again. ")


# In[16]:


#payment function

def payup(tot_cost):
    
    payment = tot_cost
           
    p_type = input(f"""For payment of ${payment}, enter 1 for credit card 
    \nor 2 for direct payment from checking account. """)

    if p_type == "1":
        looper = 1

        while looper == 1:
            try:
                ccnum = input("Enter 16-digit credit card number without dashes. ")
                ccexp = input("Enter expiration in MMYYYY format without dashes. ")
                sec_code = input("Enter three-digit card verification code. ")
            except ValueError:
                print("Error: does not match specified format. Please try again. ")

            cond1 = len(ccnum) == 16
            cond2 = len(ccexp) == 6
            cond3 =  len(sec_code) == 3

            if cond1 and cond2 and cond3:
                looper = 2
                done = input("Press1 to submit payment and proceed or 2 to cancel. ")
                if done == "1":
                    print("Thank you for your purchase! ")
                elif done == "2":
                    print("Cancelling purchase. ")
                else:             
                    print("Input not recognized. Please try again. ")

    elif p_type == "2":
        looper = 1

        while looper == 1:             
            r_num = input("Enter bank routing number. ")
            a_num = input("Enter bank account number. ")
            done = input(f"""\nBank routing number: {r_num}
                Bank account number: {a_num}
                \nPress 1 to submit payment and proceed or 2 to revise. """)

            if done == "1": 
                looper = 2
                print("Thank you for your purchase! ")
            elif done == "2":
                print("Revising. ")
            else:
                print("Input not recognized. Please try again. ")
    


# In[17]:


import pandas as pd
import numpy as np


# In[ ]:


welcmsg()
login = login_func()
cat2_df, cat_admin = data_func()

#requirement: public cannot use admin actions, vice versa

if login == "admin":
    admin_func(cat2_df, cat_admin)
else:
    pubfunc(cat2_df, cat_admin)


# In[ ]:




