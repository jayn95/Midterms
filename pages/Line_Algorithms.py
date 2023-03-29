import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

def DDALine(x, y, xNew, yNew, color):
    dx = xNew - x
    dy = yNew - y

    steps = max(abs(dx), abs(dy))
   
    Xinc = int(dx / steps)
    Yinc = int(dy / steps)

    xInc = float(dx/steps)
    yInc = float(dy/steps)

    XmidVal = (x + xNew)/2
    YmidVal = (y + yNew)/2

    fig = plt.figure()
    for i in range(int(steps + 1)):
        plt.plot(int(x), int(y), color)
        x += xInc
        y += yInc
    
    plt.plot(int(XmidVal), int(YmidVal), "g.")
    plt.title("DDA Line Algorithm with MidPoint")
    st.pyplot(fig)

def BresenhamLine(x, y, xNew, yNew, color):
    dx = xNew - x
    dy = yNew - y

    steps = max(dx, dy)
    
    Xinc = int(dx / steps)
    Yinc = int(dy / steps)

    XmidVal = (x + xNew)/2
    YmidVal = (y + yNew)/2

    fig = plt.figure()
    for i in range(int(steps + 1)):
        plt.plot(int(x), int(y), color)
        x += Xinc
        y += Yinc
    
    #Plotting the midpoint for the bresenham
    plt.plot(int(XmidVal), int(YmidVal), "g.")
    plt.title("Bresenham Line with Mid Point")
    st.pyplot(fig)

def main():

    x0 = st.number_input("Enter the Starting x-Value: ", min_value=0.01)
    y0 = st.number_input("Enter the Starting y-Value: ", min_value=0.1)
    xNew1 = st.number_input("Enter the destination x-Value: ", min_value=0.01)
    yNew1 = st.number_input("Enter the destination y-Value: ", min_value=0.1)
    color = ".b"

    plt.figure()
    DDALine(x0, y0, xNew1, yNew1, color)
    BresenhamLine(x0, y0, xNew1, yNew1, color)

if __name__ == '__main__':
    main()