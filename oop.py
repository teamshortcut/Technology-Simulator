import time
import random

class Car(): #the cookie cutter or template

    def __init__(self, name, make):
        self.name = name
        self.make = make

    def getName(self):
        return self.name

    def getMake(self):
        return self.make

    def __str__(self):
        return "%s is a %s" % (self.name, self.make)

class Device():
    def __init__(self, device, age, price):
        self.device = device
        self.age = age
        self.price = price

    def button(self):
        print("Boop. You pushed the button. Do you feel the pure joy that comes from buttons! BUTTONS!")

    def complain(self):
        print("Yeah your device is awful... yeah you totally deserve a new one... yeah I'm totally interested in everything you have to say... yes of course... LOOK JUST BE HAPPY WITH THE DEVICE YOU HAVE OKAY RIGHT COOL BYE")

    def breakIt(self):
        print("YES KILL IT BREAK IT DESTROY IT IT WILL BE FUN")
        time.sleep(1)
        print("*breaks device*")
        time.sleep(1)
        print("Okay well that was fun wasn't it now what will we do-oh wait sna-")
        time.sleep(1)

    def disassemble(self):
        print("Okay, let's carefully remove the back...")
        time.sleep(1)
        print("Oops, lets make sure we're grounded... good...")
        time.sleep(1)
        print("Okay, here we go, we're in... ooh look at all the electronics...")
        time.sleep(1)
        print("Hmm, let's not touch too much though... I just want to know what this component does...")
        time.sleep(1)
        print("Oh, okay. That's not very interesting. Ooh but what does that one do?")
        time.sleep(1)
        print("AH, okay... almost broke it... but it's fine... let's just look at this one other part and then we're done...")
        time.sleep(1)
        print("Hmm, that's a fiddly wire... careful with it mate... careful, careful...")
        time.sleep(1)
        print("OOPS")
        time.sleep(1)
        print("AH NOT GOOD NOT GOOD... okay let's just put it back into place, I'm sure it's fine.")
        time.sleep(1)
        print("Quick put the cover back on, screw everything in, it all looks fine from the outside so it must all still work right?")
        time.sleep(1)
        print("It's not turning on... let me just plug it in, I think it was low on battery before, yeah that's definitely it.")
        time.sleep(1)
        print("Let me try now... no, okay, not working... maybe if I hold the button for a really long time...")
        time.sleep(5)
        print("DAMMMIT")

class Phone(Device):
    def __init__(self):
        self.device = "Phone"
        self.age = age
        self.price = price

    def maps(self):
        print("In 400 metres turn left...")
        time.sleep(2)
        print("Yep you're lost now. Okay bye! :-)")

    def camera(self):
        num = random.randint(0, 2)
        if num == 0:
            print("Nah that's a rubbish picture, very blurry. Don't post that anywhere!")
        elif num == 1:
            print("The quality's alright but what on earth is that face you're making?! Might want to do that one again mate.")
        elif num == 2:
            print("You've actually taken a decent picture! Quick, back it up, print it, post it, frame it, it may not happen again for another decade.")
        else:
            print("Look you've somehow broken the system but I'm sure your picture is lovely. Now go away so I can debug this.")

    def text(self):
        message = input("What would like to text? ")
        print("Text sent: "+message)

    def music(self):
        if int(price) <= 150:
            print("Enjoy your tinny music through these low quality speakers playing this low quality audio. Yay!")
        elif int(price) > 150 and int(price) <= 400:
            print("You have decent speakers. You have decent audio quality. You have a decent phone. Enjoy your music. Goodbye.")
        elif int(price) > 400:
            print("You have spent a lot (probably too much) money on this phone, so enjoy the marginally better audio quality you get out of it. Now go take a bath in your money or something.")
        else:
            print("You've broken my system again. Go listen to Let it Go on repeat for the rest of the day as punishment. Go on, shoo.")

    def update(self):
        if int(age) <= 1:
            print("You're actually up to date. Enjoy it while it lasts. Which won't be very long.")
        elif int(age) > 1 and int(age) <= 6:
            print("Yeah you need to update, but you expected that. It's normal. At least your device can still update at all!")
        elif int(age) > 6:
            print("You can't update anymore. Your phone is too old. Be sad. Or happy. Or hungry. Your choice. But you can't update anything anymore. Ah well.")
        else:
            print("Stop breaking my systems you jerk. Your device is probably fine. Now begone.")

    def shutDown(self):
        print("Goodbye...")
        time.sleep(2)

class Typewriter(Device):
    def __init__(self):
        self.device = "Typewriter"

    def write(self):
        text = input("What would you like to type?")
        time.sleep(10)
        print(text)

    def replace(self):
        print("Do you need to replace this? YES GOD YES GET LITERALLY ANYTHING ELSE PLEASE ALSO HANG ON TO THIS IT'LL PROBABLY BE WORTH A LOT OF MONEY BUT PLEASE STOP USING IT GET MICROSOFT OFFICE OR SOMETHING OR EVEN A FLIPPING PIECE OF PAPER AND A PEN JUST NOT A BLOODY TYPEWRITER")
        print("'kay cool bye.")

    def shutDown(self):
        input("Would you like to shut down your device? ")
        print("*smashes typewriter on the ground*")
        print("There. It's done. NOW GO BUY A PROPER DEVICE TO TYPE ON.")

class Computer(Device):
    def __init__(self, os):
        self.age = age
        self.os = os
        self.price = price
        self.device = "Computer"

    def error(self):
        if "windows" in os.lower():
            input = "Windows has detected you are unable to connect to the internet. Would you like to search online for a solution?"
            print("Waiting for internet connection...")
            time.sleep(10)
            print("Windows has detected you are unable to connect to the internet. Would you like to search online for a solution?")
            time.sleep(1)
            print("Windows has encountered an error.")
        elif "mac" in os.lower() or "osx" in os.lower():
            print("Just imagine that rainbow ball spinning forever. Now think about your life decisions and go buy a Windows device.")
        else:
            print("An error has been detected. Just clean install the OS, it'll be fine.")

    def cmd(self):
        input("Please enter a command: ")
        print("Oh yeah everything's broken now, let this a be a lesson to you, don't mess around with the Command Line because you will definitely break something!")

    def replace(self):
        if int(self.age) > 1:
            print("Your device is now completely antiquated, please buy another one immediately to fuel our fervent desire to make money at any cost.")
        else:
            print("You appear to have literally just bought this device, congratulations on its continued relevance. Enjoy it for the next 24 hours or so before we pressure you into buying a new one.")

    def textEditor(self):
        text = input("|")
        print(text)

    def shutDown(self):
        print("Shutting Down")
        time.sleep(2)

    def support(self):
        if "windows" in os.lower():
            print("Good news; there's lots of great support on forums and other support sites. Bad news; Microsoft is completely useless so you're at the mercy of the internet. Good luck.")
        elif "mac" in os.lower() or "osx" in os.lower():
            print("You've got a Mac, just buy another one. You'll probably have to pretty soon anyway, it's a lost cause, just buy the latest one. It's what Tim Cook would want you to do.")
        else:
            print("You've either got Linux, in which case you're very good at technology and you'll probably be completely fine, or you've done something very wrong, in which case you're a bit stupid.")
    def worth(self):
        if "windows" in os.lower():
            if int(self.price) <= 200:
                print("Yeah you got a reasonable deal, congratulations! Your device is probably a bit rubbish though...")
            if int(self.price) > 200 and int(self.price) <= 600:
                print("Ah well done, looks like you got a decent device for a decent price! Well done!")
            else:
                print("You've either spent way too much on a device, or bought a device that costs way too much. Yay?")
        elif "mac" in os.lower() or "osx" in os.lower():
            if int(self.price) <= 800:
                print("Wow. Well done, you actually got an Apple device for a reasonable price! That's quite the accomplishment, enjoy!")
            elif int(self.price) > 800 and int(self.price) <= 1200:
                print("You got an Apple device for about the normal price; you probably would have been better off with a Windows device, but sure. Apple is cool. I guess.")
            else:
                print("You're an absolute idiot with more money than sense. Go sit in the Naughty Corner and think about what you've done.")
        else:
            print("Look you're probably fine. So long as your device still works you probably got a pretty good deal.")
            print("...")
            print("Unless you bought a Chromebook in which case you are the worst and should be exiled forevermore.")

#now create a Car Object from the Class template
mycar = Car("astra","Vauxhall")
"""print(mycar.getName())
print(mycar.getMake())
print(mycar.__str__())"""

device = input("What is your device? (Computer, Phone, etc.) ")
age = input("How old is your device? ")
price = input("How much did your device cost? ")

deviceClass = Device(device, int(age), int(price))

if device == "Computer":
    os = input(("What OS is your device running? "))
    computer = Computer(os)
    run = True
    while run == True:
        command = input("What would you like to do? (type Help for a list of commands) ")
        if command.lower() == "help":
            print("Here is a list of possible commands:")
            print("Error")
            print("CMD")
            print("Replace")
            print("Shut Down")
            print("Text Editor")
            print("Support")
            print("Worth")
            print("Button")
            print("Complain")
            print("Break it")
            print("Disassemble")
        if command.lower() == "error":
            computer.error()
            run = False
        if command.lower() == "cmd":
            computer.cmd()
        if command.lower() == "replace":
            computer.replace()
        if command.lower() == "shut down":
            computer.shutDown()
            run = False
        if command.lower() == "text editor":
            computer.textEditor()
        if command.lower() == "support":
            computer.support()
        if command.lower() == "worth":
            computer.worth()
        if command.lower() == "button":
            computer.button()
        if command.lower() == "complain":
            computer.complain()
        if command.lower() == "break it":
            computer.breakIt()
            run = False
        if command.lower() == "disassemble":
            computer.disassemble()
            run = False
elif device == "Phone":
    phone = Phone()
    run = True
    while run == True:
        command = input("What would you like to do? (type Help for a list of commands) ")
        if command.lower() == "help":
            print("Here is a list of possible commands:")
            print("Text")
            print("Camera")
            print("Maps")
            print("Music")
            print("Update")
            print("Button")
            print("Complain")
            print("Break it")
            print("Disassemble")
            print("Shut Down")
        if command.lower() == "text":
            phone.text()
        if command.lower() == "camera":
            phone.camera()
        if command.lower() == "maps":
            phone.maps()
        if command.lower() == "music":
            phone.music()
        if command.lower() == "update":
            phone.update()
        if command.lower() == "shut down":
            phone.shutDown()
            run = False
        if command.lower() == "button":
            phone.button()
        if command.lower() == "complain":
            phone.complain()
        if command.lower() == "break it":
            phone.breakIt()
            run = False
        if command.lower() == "disassemble":
            phone.disassemble()
            run = False
elif device == "Typewriter":
    typewriter = Typewriter()
    run = True
    while run == True:
        command = input("What would you like to do? (type Help for a list of commands) ")
        if command.lower() == "help":
            print("Here is a list of possible commands:")
            print("Write")
            print("Replace")
            print("Button")
            print("Complain")
            print("Break it")
            print("Disassemble")
            print("Shut Down")
        if command.lower() == "write":
            typewriter.write()
        if command.lower() == "replace":
            typewriter.replace()
        if command.lower() == "shut down":
            typewriter.shutDown()
            run = False
        if command.lower() == "button":
            typewriter.button()
        if command.lower() == "complain":
            typewriter.complain()
        if command.lower() == "break it":
            typewriter.breakIt()
            run = False
        if command.lower() == "disassemble":
            typewriter.disassemble()
            run = False
else:
    print("We're not sure what device you're using, but it's either really cool or really rubbish. Yay?")