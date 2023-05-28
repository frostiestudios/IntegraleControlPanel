from appJar import gui
import os
import webbrowser
import subprocess
import threading
from datetime import date

today = date.today()
print("DATE:", today)
print("Starting Initial Loading")
print("LOG1")
print("LOG2")
print("LOG3")
print("LOG4")
print("History Avail Below")
print("______________")
def wui(btn):
    print("WEB UI")
    webbrowser.open_new_tab("http://192.168.1.12:5150/")
def fair(btn):
    print("opening")
    webbrowser.open_new_tab(f"https://fareharbor.com/flightdeck1/dashboard/bookings/grid/{today}/")
def xampp(btn):
    if btn=="XAMPPStart":
        print("opening XAMPP")
        os.startfile("C:/XAMPP/xampp-control.exe")
        print("xampp")
        os.startfile("C:/XAMPP/apache_start.bat")
        print("apache")
        os.startfile("C:/XAMPP/mysql_start.bat")
        print("mysql")
        app.infoBox("Success", "Apache and MySQL servers started!")
def lc(btn):
    print("Lounge Control")
    if btn=="LCOpen":
        print("Lounge Control Is Running")
        os.startfile("C:/LoungeControl/LoungeControl-Server/LoungeControl-Server.exe")
    if btn=="LCStop":
        print("Lounge Control Is Closed")
        os.stopfile("C:/LoungeControl/LoungeControl-Server/LoungeControl-Server.exe")
def lcs(btn):
    if btn=="Remote Launcher":
        webbrowser.open_new("https://192.168.1.12:6001/ACLauncherControl")
        print("RemLauncher")
    if btn=="Leaderboard Control":
        webbrowser.open_new("https://192.168.1.12:6001/RemoteViewSettings")
        print("Remote View Leaderboard")
    if btn=="New Car":
        webbrowser.open_new("https://192.168.1.12:6001/Cars/Create")
        print("Cars")
    if btn=="New Track":
        webbrowser.open_new("https://192.168.1.12:6001/Tracks/Create")
        print("Tracks")
def ms(btn):    
    print("MultiServer")
    if btn=="MSOpen":
        os.startfile("C:\LoungeControl\LoungeControl-ACMultiServer\LC-AC-MultiServer.exe")
def text():
    "text"
def sigma():
    print("Sigma Settings")

def dbo():
    print("DBO")
    with sqlite3.connect('data/rr.db') as db:
        SE


tools = ["Start", "Stop"]
app = gui("Command Center",useTtk=True)
app.startTabbedFrame("Tabs")
app.startTab("Home")
app.startLabelFrame("Welcome",0,1,3)
app.addLabel("W","Welcome to Rogue Racing",0,1)
app.addLabel("D",f"{today}",0,3)
app.stopLabelFrame()

app.startLabelFrame("XAMPP",1,1)
app.addButtons(["XAMPPStart","XAMPPStop"],xampp)
app.stopLabelFrame()

app.startLabelFrame("Lounge Control",1,2)
app.addButtons(["LCOpen","LCStop"],lc)
app.stopLabelFrame()

app.startLabelFrame("MultiServer",1,3)
app.addButtons(["MSOpen","MSStop"],ms)

app.stopLabelFrame()

app.startLabelFrame("Lounge Control Settigns",2,1,3)
app.addButtons(["Remote Launcher","Leaderboard Control"],lcs)
app.stopLabelFrame()

app.startLabelFrame("Content Settings",3,1,3)
app.addButtons(["New Car","New Track"],lcs)
app.stopLabelFrame()

app.startLabelFrame("FairHarbor Settings",4,1)
app.addButtons(["Open Fair Harbor"],fair)
app.stopLabelFrame()

app.startLabelFrame("WEB UI",4,2,2)
app.addButton("Open Web UI",wui)
app.stopLabelFrame()

app.startLabelFrame("Sigma Settings",5,1,3)
app.addButtons(["1","2",'3','4','5','6'],sigma)
app.stopLabelFrame()
app.stopTab()

#Sigma Settings
app.startTab("Sigma")
app.addDbTable("computers","data/rr.db","computers",action=dbo)
app.stopTab()
#Content
app.startTab("Content")
app.stopTab()

app.stopTabbedFrame()
app.go()
