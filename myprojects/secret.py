
def createSecret(msg):
    code = []
    for i in msg:
        code.append(ord(i))
    return code      

def findoutmessage(msg):
    print ("We need your help, Agent A!")
    print ("Someone hacked into our computer, and stole high-secured information.")
    print ("He left some clues of his identity and we need your help!")
    print ("Agent A! Can you break this code?")
    print (createSecret(msg))

def hints1():
    try:
        yn = input("Do you need a hint? (y or no): ").lower()
    except:
        print ("Invalid input. Bye.")
        return False
    else:
        if yn == 'y':
            print ("The message looks like the language called \"Unicode\" spoken in computers country.")
        else:
            print ("Ok. Try your best!") 
            return False

msg = input("Secret message?: ")
findoutmessage(msg)
hints1()