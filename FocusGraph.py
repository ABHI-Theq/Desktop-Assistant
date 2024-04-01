import matplotlib.pyplot as pt

def focus_graph():
    with open("focus.txt","r") as f:
        content=f.read()
    content=content.split(",")
    x1=[]
    for i in range(0,len(content)):
        content[i]=float(content[i])
        x1.append(i)

    print(content)
    y1=content

    pt.plot(x1,y1,color="red",marker="o")
    pt.title("YOur focused time",fontsize = 16)
    pt.xlabel("Times",fontsize=14)
    pt.ylabel("Focus Time",fontsize=14)
    pt.grid()
    pt.show()



        #current time=12:00
        #stop time= 12:30

        #focus timer=00:30 change in float 00.30