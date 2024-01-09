from tkinter import * # module for GUI
import speedtest     # module for internet speed

def speedcheck(): # function to check speed
    sp = speedtest.Speedtest() # speedtest module has class Speedtest
    sp.get_servers()     # for server
    down = str(round(sp.download()/(10**6),3))+ " Mbps"    # to check download speed , division to convert speed in mbps ,round for roundoff speed upto 3  
    up =   str(round(sp.upload()/(10**6),3))+ " Mbps"       # for upload speed                                          
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()      # to create window
sp.title( " Internet Speed Test ")   # title of window
sp.geometry("500x700")
sp.config(bg="Pink")

lab = Label(sp, text = "Internet Speed Test" , font = ("Time New Roman", 30,"bold"),bg="Blue",fg="White")
lab.place(x=60,y=40,height=50,width=380)  # for placement

lab = Label(sp, text = "Download Speed" , font = ("Time New Roman", 30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab_down = Label(sp, text = "00" , font = ("Time New Roman", 30,"bold"))
lab_down.place(x=60,y=200,height=50,width=380)

lab = Label(sp, text = "Upload Speed" , font = ("Time New Roman", 30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_up = Label(sp, text = "00" , font = ("Time New Roman", 30,"bold"))
lab_up.place(x=60,y=360,height=50,width=380)

button = Button(sp,text = "Check Speed",font = ("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=speedcheck()) # releif to give 3d impact to button
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()


