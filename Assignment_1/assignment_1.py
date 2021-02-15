import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from math import sqrt


def isprime(n):
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
 
    return True

  
def mobius_calc(n) : 
    if (n == 1) : 
        return 1
    p = 0
    for i in range(1, n + 1) : 
        if (n % i == 0 and isprime(i)) :
            if (n % (i * i) == 0) : 
                return 0
            else :
                p = p + 1
    if(p % 2 != 0) : 
        return -1
    else : 
        return 1
  


def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a)
 
def euler_totient_calc(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 
  




def submit():
    global n_input
    global mobius_output
    global euler_output
    mobius = mobius_output.get()
    euler = euler_output.get()
    mobius_output.delete(0, len(mobius))
    euler_output.delete(0, len(euler))
    try:
        n = int(n_input.get())
        mobius_output.insert(0, mobius_calc(n))
        euler_output.insert(0, euler_totient_calc(n))
    except Exception as e:
        print("Error : ",e)



root = Tk()
root.geometry("600x300")
root.title("Mobius and Euler-Totient Calculator")
n_value = Label(root, text = "Enter value of N : ").place(x = 40, y = 60)
n_input = Entry(root, width = 30)
n_input.place(x = 160, y = 60)
submit_button = Button(root, text = "Submit", command=submit).place(x = 200, y = 100)
mobius_str = Label(root, text = "Mobius Function Value = ").place(x = 40, y = 180)
mobius_output = Entry(root,width=30)
mobius_output.place(x = 250, y = 180)
euler_str = Label(root, text = "Euler Totient Function Value = ").place(x = 40, y = 230)
euler_output = Entry(root,width=30)
euler_output.place(x = 250, y = 230)

root.mainloop()

