# **kwargs 

#   def sup(dude, bro):
#    print("Hey, " +dude+".","Sup, "+bro)
#    sup(dude="dude",bro="brah?")

def demigod(**pjo):
    print("Did you know that Percy's real name is Perseus? ",end="")
    for key,value in pjo.items():
        print(value,end=" ")


demigod(title="Naturally,", first="only his enemies or ", middle="close friends call him ", last="like that.")