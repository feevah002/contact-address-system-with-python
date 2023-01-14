#Group 14 Project

from tkinter import *
import sqlite3

# create window
window = Tk()
window.title("Contact List")
window.geometry("500x500")

# create database
conn = sqlite3.connect("AddressBook.db")
c = conn.cursor()
'''
c.execute("""CREATE TABLE contactlist(
first_name text,
surname text,
contact_No text,
address text,
email text,
city text,
country text
)""")
'''

def edit():
    editor = Tk()
    editor.title("Update")
    editor.geometry("400x400")

    #add labels
    first_name_editor_label = Label(editor, text="First Name")
    first_name_editor_label.grid(row=0, column=0)

    surname_editor_label = Label(editor, text="Surname")
    surname_editor_label.grid(row=1, column=0)

    contact_editor_no_label = Label(editor, text="Contact No.")
    contact_editor_no_label.grid(row=2, column=0)

    address_editor_label = Label(editor, text="Address")
    address_editor_label.grid(row=3, column=0)

    email_editor_label = Label(editor, text="Email")
    email_editor_label.grid(row=4, column=0)

    city_editor_label = Label(editor, text="City")
    city_editor_label.grid(row=5, column=0)

    country_editor_label = Label(editor, text="Cuntry")
    country_editor_label.grid(row=6, column=0)


    # add text-fields
    first_name_editor = Entry(editor, width=38)
    first_name_editor.grid(row=0, column=1, padx=20)

    surname_editor = Entry(editor, width=38)
    surname_editor.grid(row=1, column=1, padx=20)

    contact_no_editor = Entry(editor, width=38)
    contact_no_editor.grid(row=2, column=1, padx=20)

    address_editor = Entry(editor, width=38)
    address_editor.grid(row=3, column=1, padx=20)

    email_editor = Entry(editor, width=38)
    email_editor.grid(row=4, column=1, padx=20)

    city_editor = Entry(editor, width=38)
    city_editor.grid(row=5, column=1, padx=20)

    country_editor = Entry(editor, width=38)
    country_editor.grid(row=6, column=1, padx=20)

  


    #connect database for new app
    conn = sqlite3.connect("AddressBook.db")
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("SELECT * FROM contactlist WHERE oid = "+record_id)
    records = c.fetchall()


    show=''
    for record in records[0:]:
        show+=str(record)+"\t"+"\n"
        #Create global variable for text boxes name
        first_name_editor.insert(0, record[0])
        surname_editor.insert(0, record[1])
        contact_no_editor.insert(0, record[2])
        address_editor.insert(0, record[3])
        email_editor.insert(0, record[4])
        city_editor.insert(0, record[5])
        country_editor.insert(0, record[6])

    # update function has to be in the edit-form function in order to retrieve the form's data
    def update():
        conn = sqlite3.connect("AddressBook.db")
        c = conn.cursor()
        record_id=delete_box.get()

        #change data in table

        c.execute('''UPDATE contactlist SET
                first_name = :first_name,
                surname = :surname,
                contact_No = :contact_No,
                address = :address,
                email = :email,
                city = :city,
                country = :country
                WHERE oid = :oid''',
                {
                    'first_name':  first_name_editor.get(),
                    'surname': surname_editor.get(),
                    'contact_No': contact_no_editor.get(),
                    'address': address_editor.get(),
                    'email': email_editor.get(),
                    'city': city_editor.get(),
                    'country': country_editor.get(),
                    'oid': record_id

                }
                )
        conn.commit()
        conn.close()
    
    # dropped below the update function to avoid referenced before assignment error
    show_btn_editor = Button(editor, text="Save record", command=update)
    show_btn_editor.grid(row=12, column=0, columnspan=2, pady=10, ipadx=108)
    
def show():
    search = Tk()
    search.title("show a record")
    search.geometry("400x400")
    conn = sqlite3.connect("AddressBook.db")
    c = conn.cursor()
    record_id = delete_box.get()
    # show query
    c.execute("SELECT * FROM contactlist WHERE oid = "+record_id)
    records = c.fetchall()
    
    print_records = ''
    for record in records:
        
        
        print_records += "id: "+record[0] + " \nfirstame: " + (record[0]) + " \nsurname: " + (record[1]) + " \ncontact No: " + (
            record[2]) + " \nAddress: " + (record[3]) + " \nEmail: " + (record[4]) + " \nCity: " + (record[5]) + " \nCountry: " + (
            record[6]) + "\n\n"

    search_label = Label(search, text=print_records)
    search_label.grid(row=11, column=0, columnspan=2)

def submit():
    conn = sqlite3.connect("AddressBook.db")
    c = conn.cursor()

    # insert data into table

    c.execute("INSERT INTO contactlist VALUES(:first_name,:surname,:contact_No,:address,:email,:city,:country)",
              {

                  'first_name': first_name.get(),
                  'surname': surname.get(),
                  'contact_No': contact_no.get(),
                  'address': address.get(),
                  'email': email.get(),
                  'city': city.get(),
                  'country': country.get()
              })

    conn.commit()
    conn.close()

    first_name.delete(0, END)
    surname.delete(0, END)
    contact_no.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)
    city.delete(0, END)
    country.delete(0, END)

def allData():
    show = Tk()
    show.title("all Records")
    show.geometry("400x400")
    conn = sqlite3.connect("AddressBook.db")
    c = conn.cursor()

    # show query
    c.execute("SELECT *, oid FROM contactlist")
    records = c.fetchall()
    # loop through and display on GUI
    print_records = ''

    for record in records:
        print_records += "id: "+str(record[7]) + " \nfirstame: " + str(record[0]) + " \nsurname: " + str(record[1]) + " \ncontact No: " + str(
            record[2]) + " \nAddress: " + str(record[3]) + " \nEmail: " + str(record[4]) + " \nCity: " + str(record[5]) + " \nCountry: " + str(
            record[6]) + "\n\n"

    show_label = Label(show, text=print_records)
    show_label.grid(row=11, column=0, columnspan=2)

def delete():
    conn = sqlite3.connect("AddressBook.db")
    c = conn.cursor()

    c.execute("DELETE from contactlist WHERE oid = " + delete_box.get())

    conn.commit()
    conn.close()

# add labels

first_name_label = Label(window, text="First Name")
first_name_label.grid(row=0, column=0)

surname_label = Label(window, text="Surname")
surname_label.grid(row=1, column=0)

contact_no_label = Label(window, text="Contact No.")
contact_no_label.grid(row=2, column=0)

address_label = Label(window, text="Address")
address_label.grid(row=3, column=0)

email_label = Label(window, text="Email")
email_label.grid(row=4, column=0)

city_label = Label(window, text="City")
city_label.grid(row=5, column=0)

country_label = Label(window, text="Country")
country_label.grid(row=6, column=0)

delete_box_label = Label(window, text="Record ID")
delete_box_label.grid(row=9, column=0)


# add text-fields

first_name = Entry(window, width=38)
first_name.grid(row=0, column=1, padx=20)

surname = Entry(window, width=38)
surname.grid(row=1, column=1, padx=20)

contact_no = Entry(window, width=38)
contact_no.grid(row=2, column=1, padx=20)

address = Entry(window, width=38)
address.grid(row=3, column=1, padx=20)

email = Entry(window, width=38)
email.grid(row=4, column=1, padx=20)

city = Entry(window, width=38)
city.grid(row=5, column=1, padx=20)

country = Entry(window, width=38)
country.grid(row=6, column=1, padx=20)

delete_box = Entry(window, width=38)
delete_box.grid(row=9, column=1, padx=20)
# add command button
submit_btn = Button(window, text="Add record", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, ipadx=100)

# show allData button
show_btn = Button(window, text="Show record", command=allData)
show_btn.grid(row=8, column=0, columnspan=2, pady=10, ipadx=100)

# show for a particular record
show_btn = Button(window, text="Show a record", command=show)
show_btn.grid(row=13, column=0, columnspan=2, pady=10, ipadx=100)

# delete button
show_btn = Button(window, text="Delete record", command=delete)
show_btn.grid(row=10, column=0, columnspan=2, pady=10, ipadx=100)

# edit button
show_btn = Button(window, text="Edit record", command=edit)
show_btn.grid(row=16, column=0, columnspan=2, pady=10, ipadx=108)

window.mainloop()
