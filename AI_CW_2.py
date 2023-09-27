import csv 
import operator 
import tkinter as tk

DataSet = open('Solar_Flares_Dataset.csv','r')

CSV = csv.reader(DataSet,delimiter=',') 
next(CSV)

FlaresType = sorted(CSV,key=operator.itemgetter(12))

headers = ("modified Zurich class ", "largest spot size ","spot distribution ", "Activity ","Evolution  ","Previous 24 hour flare activity code ", "Historically-complex ", "Area ", "Area of the largest spot ", "C-Class Flares", "M-Class Flares", "X-Class Flares")

from tkinter import filedialog
canvas = tk.Canvas(root, width = 1200, height = 500, bg = 'white', relief = 'raised')
canvas.pack()
root= tk.Tk()
root.title("Solar Flares") 



def EntireDataSet():
    print(headers) 
    for line in FlaresType:
        print(line)
        
def Xflares(): 
    print(headers) 
    for line in FlaresType:
        if int(line[12]) >= 1:
            print(line)
            
def Mflares():
    print(headers)
    for line in FlaresType:
        if int(line[11]) >= 1:
            print(line)
            
def Cflares():
    print(headers)
    for line in FlaresType:
        if int(line[10]) >= 1:
            print(line)
            
def CheckFlareType():
    
    Activity = tk.StringVar()
    name_label = tk.Label(root, text = "Where was the activity?", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 150, window=name_label)

    global ActivityV
    
    ActivityV = tk.IntVar()
    A1 = tk.Radiobutton(root, text="1", variable=ActivityV, value=1)
    canvas.create_window(330, 150, window=A1)

    A2 = tk.Radiobutton(root, text="2", variable=ActivityV, value=2)
    canvas.create_window(380, 150, window=A2)

    Evolution = tk.StringVar()
    name_label = tk.Label(root, text = "How quick was the evolution?", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 180, window=name_label)

    global EvolutionV
    
    EvolutionV = tk.IntVar()
    E1 = tk.Radiobutton(root, text="1", variable=EvolutionV, value=1)
    canvas.create_window(330, 180, window=E1)

    E2 = tk.Radiobutton(root, text="2", variable=EvolutionV, value=2)
    canvas.create_window(380, 180, window=E2)

    E3 = tk.Radiobutton(root, text="3", variable=EvolutionV, value=3)
    canvas.create_window(430, 180, window=E3)
    
    Previous = tk.StringVar()
    name_label = tk.Label(root, text = "Previous 24 hour flare activity code", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 210, window=name_label)

    global PreviousV
    
    PreviousV = tk.IntVar()
    P1 = tk.Radiobutton(root, text="1", variable=PreviousV, value=1)
    canvas.create_window(330, 210, window=P1)

    P2 = tk.Radiobutton(root, text="2", variable=PreviousV, value=2)
    canvas.create_window(380, 210, window=P2)

    P3 = tk.Radiobutton(root, text="3", variable=PreviousV, value=3)
    canvas.create_window(430, 210, window=P3)

    Historically_complex1 = tk.StringVar()
    name_label = tk.Label(root, text = "historically complex", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 240, window=name_label)

    global Historically_complex1V
    
    Historically_complex1V = tk.IntVar()
    HC11 = tk.Radiobutton(root, text="1", variable=Historically_complex1V, value=1)
    canvas.create_window(330, 240, window=HC11)

    HC12 = tk.Radiobutton(root, text="2", variable=Historically_complex1V, value=2)
    canvas.create_window(380, 240, window=HC12)

    Historically_complex = tk.StringVar()
    name_label = tk.Label(root, text = "Did region become historically complex \non this pass across the sun's disk?", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 277, window=name_label)

    global Historically_complexV
    
    Historically_complexV = tk.IntVar()
    HC1 = tk.Radiobutton(root, text="1", variable=Historically_complexV, value=1)
    canvas.create_window(330, 277, window=HC1)

    HC2 = tk.Radiobutton(root, text="2", variable=Historically_complexV, value=2)
    canvas.create_window(380, 277, window=HC2)

    Area = tk.StringVar()
    name_label = tk.Label(root, text = "Which area did the flare start?", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 315, window=name_label)

    global AreaV
    
    AreaV = tk.IntVar()
    Ar1 = tk.Radiobutton(root, text="1", variable=AreaV, value=1)
    canvas.create_window(330, 315, window=Ar1)

    Ar2 = tk.Radiobutton(root, text="2", variable=AreaV, value=2)
    canvas.create_window(380, 315, window=Ar2)

    MClass = tk.StringVar()
    name_label = tk.Label(root, text = "modified Zurich class", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 345, window=name_label)

    global MClassV
    
    MClassV = tk.IntVar()
    MC1 = tk.Radiobutton(root, text="B", variable=MClassV, value=1)
    canvas.create_window(330, 345, window=MC1)

    MC2 = tk.Radiobutton(root, text="C", variable=MClassV, value=2)
    canvas.create_window(380, 345, window=MC2)
    
    MC3 = tk.Radiobutton(root, text="D", variable=MClassV, value=3)
    canvas.create_window(430, 345, window=MC3)

    MC4 = tk.Radiobutton(root, text="E", variable=MClassV, value=4)
    canvas.create_window(480, 345, window=MC4)
    
    MC5 = tk.Radiobutton(root, text="F", variable=MClassV, value=5)
    canvas.create_window(530, 345, window=MC5)

    MC6 = tk.Radiobutton(root, text="H", variable=MClassV, value=6)
    canvas.create_window(580, 345, window=MC6)

    LSSize = tk.StringVar()
    name_label = tk.Label(root, text = "What was the largest spot size", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 375, window=name_label)

    global LSSizeV
    
    LSSizeV = tk.IntVar()
    LS1 = tk.Radiobutton(root, text="A", variable=LSSizeV, value=1)
    canvas.create_window(330, 375, window=LS1)

    LS2 = tk.Radiobutton(root, text="H", variable=LSSizeV, value=2)
    canvas.create_window(380, 375, window=LS2)
    
    LS3 = tk.Radiobutton(root, text="K", variable=LSSizeV, value=3)
    canvas.create_window(430, 375, window=LS3)

    LS4 = tk.Radiobutton(root, text="R", variable=LSSizeV, value=4)
    canvas.create_window(480, 375, window=LS4)
    
    LS5 = tk.Radiobutton(root, text="S", variable=LSSizeV, value=5)
    canvas.create_window(530, 375, window=LS5)

    LS6 = tk.Radiobutton(root, text="X", variable=LSSizeV, value=6)
    canvas.create_window(580, 375, window=LS6)

    Spot_distribution = tk.StringVar()
    name_label = tk.Label(root, text = "Spot distribution", font=('calibre', 10, 'bold')) 
    canvas.create_window(150, 405, window=name_label)

    global Spot_distributionV
    
    Spot_distributionV = tk.IntVar()
    SD1 = tk.Radiobutton(root, text="C", variable=Spot_distributionV, value=1)
    canvas.create_window(330, 405, window=SD1)

    SD2 = tk.Radiobutton(root, text="I", variable=Spot_distributionV, value=2)
    canvas.create_window(380, 405, window=SD2)
    
    SD3 = tk.Radiobutton(root, text="O", variable=Spot_distributionV, value=3)
    canvas.create_window(430, 405, window=SD3)

    SD4 = tk.Radiobutton(root, text="X", variable=Spot_distributionV, value=4)
    canvas.create_window(480, 405, window=SD4)

    global sub_btn1

    sub_btn1=tk.Button(root,text = 'Check flare type', command=result) 
    canvas.create_window(380,440,window=sub_btn1)
                                                  
def result():

    global answer1
   
    none = "The flare was neither of the specified flares"
    CFlare = "The flare type is C-Flare"
    MFlare = "The flare type is M-Flare"
    XFlare = "The flare type is X-Flare"

    if((LSSizeV.get() ==3) | (LSSizeV.get() == 1)) & ((EvolutionV.get() ==2) | (EvolutionV.get() ==3)) & ((PreviousV.get() ==1) | (PreviousV.get() ==3)) & ((Spot_distributionV.get() ==1) | (Spot_distributionV.get() ==2)) & ((MClassV.get() ==3) | (MClassV.get() ==4) | (MClassV.get() ==5))  & (Historically_complexV.get() ==2) & (Historically_complex1V.get() ==2) & ((ActivityV.get() ==2) | (ActivityV.get() ==1)) & ((AreaV.get() ==1) | (AreaV.get() == 2)):
        answer1 = tk.Label(root, text=XFlare, font=('calibre', 12, 'bold'), bg="green")
        canvas.create_window(200, 480, window=answer1)

    elif ((EvolutionV.get() ==1) | (EvolutionV.get() ==2) | (EvolutionV.get() ==3)) & ((PreviousV.get() ==1) | (PreviousV.get() ==2) | (PreviousV.get() ==3)) & ((Historically_complexV.get() ==1) | (Historically_complexV.get() ==2)) & ((Historically_complex1V.get() ==1) | (Historically_complex1V.get() ==2)) & ((ActivityV.get() ==2) | (ActivityV.get() ==1)) & ((AreaV.get() ==1) | (AreaV.get() == 2)):
        answer1 = tk.Label(root, text=CFlare, font=('calibre', 12, 'bold'), bg="green")
        canvas.create_window(200, 480, window=answer1)

    elif ((LSSizeV.get() == 1) | (LSSizeV.get() == 3) | (LSSizeV.get() == 4) | (LSSizeV.get() == 5)) & (EvolutionV.get() ==3) & (PreviousV.get() ==1) & ((Spot_distributionV.get() ==1) | (Spot_distributionV.get() ==2) | (Spot_distributionV.get() ==3)) & ((MClassV.get() ==3) | (MClassV.get() ==4)) & (Historically_complexV.get() ==2) | (Historically_complex1V.get() ==2) & ((ActivityV.get() ==2) | (ActivityV.get() ==1)) & (AreaV.get() ==1):
        answer1 = tk.Label(root, text=MFlare, font=('calibre', 12, 'bold'), bg="green")
        canvas.create_window(200, 480, window=answer1)

    else:
        answer1 = tk.Label(root, text=none, font=('calibre', 12, 'bold'), bg="green")
        canvas.create_window(200, 480, window=answer1)
    
    sub_btn1['state'] = "disabled"
    
    global Ref_btn1
    Ref_btn1=tk.Button(root,text = "Refresh", command=deleteResult)
    canvas.create_window(470,440,window=Ref_btn1)

def deleteResult():
    answer1.destroy()
    sub_btn1['state'] = "normal"
    Ref_btn1.destroy()    

def predicting():

    BuildUp = tk.StringVar()
    name_label = tk.Label(root, text = "Are satellites showing a build up of \nmagnetic energy on the sun?", font=('calibre', 10, 'bold')) 
    canvas.create_window(800, 150, window=name_label)

    global BuildUpV
    
    BuildUpV = tk.IntVar()
    BU1 = tk.Radiobutton(root, text="No", variable=BuildUpV, value=1)
    canvas.create_window(1000, 150, window=BU1)

    BU2 = tk.Radiobutton(root, text="Yes", variable=BuildUpV, value=2)
    canvas.create_window(1050, 150, window=BU2)

    Strength = tk.StringVar()
    name_label = tk.Label(root, text = "What is the strength of the magnetic instability?\nOn a scale of 1 - 5(1 being the weakest)", font=('calibre', 10, 'bold')) 
    canvas.create_window(800, 200, window=name_label)

    global StrengthV
    
    StrengthV = tk.IntVar()
    ST1 = tk.Radiobutton(root, text="1", variable=StrengthV, value=1)
    canvas.create_window(1000, 200, window=ST1)

    ST2 = tk.Radiobutton(root, text="2", variable=StrengthV, value=2)
    canvas.create_window(1040, 200, window=ST2)

    ST3 = tk.Radiobutton(root, text="3", variable=StrengthV, value=3)
    canvas.create_window(1080, 200, window=ST3)

    ST4 = tk.Radiobutton(root, text="4", variable=StrengthV, value=4)
    canvas.create_window(1120, 200, window=ST4)

    ST5 = tk.Radiobutton(root, text="5", variable=StrengthV, value=5)
    canvas.create_window(1160, 200, window=ST5)

    Direction = tk.StringVar()
    name_label = tk.Label(root, text = "Is the flare facing the direction of earth?", font=('calibre', 10, 'bold')) 
    canvas.create_window(800, 250, window=name_label)

    global DirectionV
    
    DirectionV = tk.IntVar()
    D1 = tk.Radiobutton(root, text="No", variable=DirectionV, value=1)
    canvas.create_window(1000, 250, window=D1)

    D2 = tk.Radiobutton(root, text="Yes", variable=DirectionV, value=2)
    canvas.create_window(1050, 250, window=D2)

    global sub_btn2
    
    sub_btn2=tk.Button(root,text = "Predict flare", command=result2) 
    canvas.create_window(1000,300,window=sub_btn2)

def result2():

    global answer
    No_flare = "There is no sign of a flare"
    Yes_flare = "These are signs of a flare\n"

    C_Flare = "The flare type is most likely to be an C-class flare\n"
    C_SatY = "The flare could impact satellites around earth however \nthis is less likely to happen"
    C_SatN = "This is less likely to impact satellites around earth"

    M_Flare = "The flare type is most likely to be an M-class flare\n"
    M_SatY = "The flare could impact satellites around earth"
    M_SatN = "This is less likely to impact satellites around earth"

    X_Flare = "The flare type is most likely to be an X-class flare\n"
    X_SatY = "There is a high chance that the flare could impact\n satellites around earth"
    X_SatN = "This is less likely to impact satellites around earth"    

    if(BuildUpV.get() ==1):
        answer = tk.Label(root, text=No_flare, font=('calibre', 12, 'bold'), bg="green")
        canvas.create_window(950, 370, window=answer)


    if(BuildUpV.get() ==2) & ((StrengthV.get() == 1) | (StrengthV.get() ==2)):
        if(DirectionV.get() ==2):
            answer = tk.Label(root, text=Yes_flare + C_Flare + C_SatY, font=('calibre', 12, 'bold'), bg="green")
            canvas.create_window(950, 370, window=answer)

        elif(DirectionV.get() ==1):
            answer = tk.Label(root, text=Yes_flare + C_Flare + C_SatN , font=('calibre', 12, 'bold'), bg="green")
            canvas.create_window(950, 370, window=answer)

    if(BuildUpV.get() ==2) & (StrengthV.get() == 3):
        if(DirectionV.get() ==2):
            answer = tk.Label(root, text=Yes_flare + M_Flare + M_SatY, font=('calibre', 12, 'bold'), bg="green")
            canvas.create_window(950, 370, window=answer)

        elif(DirectionV.get() ==1):
            answer = tk.Label(root, text=Yes_flare + M_Flare + M_SatN , font=('calibre', 12, 'bold'), bg="green")
            canvas.create_window(950, 370, window=answer)

    if(BuildUpV.get() ==2) & ((StrengthV.get() == 4) | (StrengthV.get() == 5)):
        if(DirectionV.get() ==2):
            answer = tk.Label(root, text=Yes_flare + X_Flare + X_SatY, font=('calibre', 12, 'bold'), bg="green")
            canvas.create_window(950, 370, window=answer)

        elif(DirectionV.get() ==1):
            answer = tk.Label(root, text=Yes_flare + X_Flare + X_SatN , font=('calibre', 12, 'bold'), bg="green")
            canvas.create_window(950, 370, window=answer)

    sub_btn2['state'] = "disabled"

    global Ref_btn2
    Ref_btn2=tk.Button(root,text = "Refresh", command=deleteResult2)
    canvas.create_window(1100,300,window=Ref_btn2)

def deleteResult2():
    answer.destroy()
    sub_btn2['state'] = "normal"
    Ref_btn2.destroy()
    
def main(): 
    
    EntireDatasetButton = browseButton_CSV = tk.Button(text="See Entire Dataset", command=EntireDataSet, bg='blue', fg='black', font=('Times New Roman', 15, 'bold'))
    canvas.create_window(100, 50, window=browseButton_CSV)
    
    Xflaresbutton = browseButton_CSV = tk.Button(text="          X flares         ", command=Xflares, bg='blue', fg='black', font=('Times New Roman', 15, 'bold'))
    canvas.create_window(300, 50, window=browseButton_CSV)

    Mflaresbutton = browseButton_CSV = tk.Button(text="         M flares         "  , command=Mflares, bg='blue', fg='black', font=('Times New Roman', 15, 'bold'))
    canvas.create_window(500, 50, window=browseButton_CSV)

    Cflaresbutton = browseButton_CSV = tk.Button(text="          C flares        ", command=Cflares, bg='blue', fg='black', font=('Times New Roman', 15, 'bold'))
    canvas.create_window(700, 50, window=browseButton_CSV)

    CheckFlareTypebutton = browseButton_CSV = tk.Button(text=" Check Flare Type "  , command=CheckFlareType, bg='blue', fg='black', font=('Times New Roman', 15, 'bold'))
    canvas.create_window(900, 50, window=browseButton_CSV)

    PredictingFlare = browseButton_CSV = tk.Button(text="Predict Solar Flare"  , command=predicting, bg='blue', fg='black', font=('Times New Roman', 15, 'bold'))
    canvas.create_window(1100, 50, window=browseButton_CSV)
    
main()

