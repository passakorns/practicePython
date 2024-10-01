from tkinter import *

window = Tk()
window.geometry("600x400")
window.configure(background='#FFF6DC')
window.title('My Restaurant')

no_of_person = StringVar()
txtLabel = StringVar()
txtTotal = StringVar()

# ---------------------------------------------------------------
def pick_menu_1():
    n_person = no_of_person.get()
    price = 499 * int(n_person)

    text = B1.cget('text') + ' for ' +  n_person + ' person\n'
    text += 'Total : ' + str( '{:,}'.format(price)  ) +  ' Bath'
    txtLabel.set(text)

    
# ---------------------------------------------------------------

def pick_menu_2():
    n_person = no_of_person.get()
    price = 899 * int(n_person)

    #อ่านค่า property ของ widget button ด้วย cget()
    text = B2.cget('text') + ' for ' +  n_person + ' person\n'
    text += 'Total : ' + str( '{:,}'.format(price)  ) +  ' Bath'
    #กำหหนดค่า widget property textvaritable 
    txtLabel.set(text)
   
 
# ---------------------------------------------------------------

L1 = Label( window ,
            bg = '#FFF6DC' ,
            text = 'Enter Person : ',
            font = ('Tahoma', 15)
            )
L1.grid(row = 0 , column = 0, pady=20, padx=20, sticky=(E))


E1 = Entry( window, 
            fg = 'black',
            textvariable = no_of_person,
            width = 10,
            font = ('Tahoma', 15)
            )
E1.grid(row = 0 , column = 1)

L2 = Label( window,
            bg = '#FFF6DC' ,
            text = 'person',
            font = ('Tahoma', 15)
            )
L2.grid(row = 0 , column = 2, pady=20, padx=20)

L3 = Label( window ,
            bg = '#FFF6DC' ,
            text = 'Menu : ',
            font = ('Tahoma', 15)
            )
L3.grid(row = 1 , column = 0, pady=20, padx=20, sticky=(E))

B1 = Button( window,
              bg = '#FFC6AC' , 
              width=15, height=3 , 
              text = 'Buffet 499',
              font = ('Tahoma', 16),
              command = pick_menu_1
            )
B1.grid(row = 1, column = 1)

B2 = Button( window,
              bg = '#FFC6AC' , 
              width=15, height=3 , 
              text = 'Buffet 899',
              font = ('Tahoma', 16),
              command = pick_menu_2
            )
B2.grid(row = 1, column = 2)

L4 = Label( window, 
                bg = '#FFF6DC' ,
                textvariable = txtLabel,
                font = ('Tahoma', 18, 'bold'))
L4.grid(row = 2, column = 0, columnspan=3, pady=30)


window.mainloop()