import tkinter as tk


#本館ページ
def HKp():
    HKp = tk.Toplevel(root)
    HKp.geometry("1980x1080")
    HKp.title("本館")




    back_button = tk.Button(HKp,text="戻る",font=("MSゴシック", "50"),activeforeground="blue",command=HKp.destroy)
    back_button.place(x=20,y=20)
    fst_bt = tk.Button(HKp,text="1年生", font=("MSゴシック", "150"),activeforeground="blue",command=fst)
    fst_bt.place(x=100,y=200)
    sst_bt = tk.Button(HKp,text="2年生", font=("MSゴシック", "150"),activeforeground="blue",command=sst)
    sst_bt.place(x=700,y=200)
    lst_bt = tk.Button(HKp,text="3年生", font=("MSゴシック", "150"),activeforeground="blue",command=lst)
    lst_bt.place(x=100,y=500)




#電気科ページ
def Ep():
    Ep = tk.Toplevel(root)
    Ep.geometry("1980x1080")
    Ep.title("電気科")




    back_button = tk.Button(Ep,text="戻る",font=("MSゴシック", "50"),activeforeground="blue",command=Ep.destroy)
    back_button.place(x=20,y=20)


#電子機械科ページ
def Sp():
    Sp = tk.Toplevel(root)
    Sp.geometry("1980x1080")
    Sp.title("電子機械科")




    back_button = tk.Button(Sp,text="戻る",font=("MSゴシック", "50"),activeforeground="blue",command=Sp.destroy)
    back_button.place(x=20,y=20)


#機械科ページ
def Mp():
    Mp = tk.Toplevel(root)
    Mp.geometry("1980x1080")
    Mp.title("機械科")




    back_button = tk.Button(Mp,text="戻る",font=("MSゴシック", "50"),activeforeground="blue",command=Mp.destroy)
    back_button.place(x=20,y=20)


#電子科ページ
def Dp():
    Dp = tk.Toplevel(root)
    Dp.geometry("1980x1080")
    Dp.title("電子科")


    label_d1 = tk.Label(Dp,text="一階",font=("MSゴシック", "100"))
    label_d1.place(x=110,y=720)
    canvas_d1 = tk.Canvas(Dp,width=1300,height=50,bg="gray")
    canvas_d1.place(x=400,y=820)
    button_d1_1 = tk.Button(Dp,text="職員室",width=10,font=("MSゴシック", "60"),activeforeground="blue")
    button_d1_1.place(x=600,y=700)
    button_d1_2 = tk.Button(Dp,text="作業室",width=10,font=("MSゴシック", "60"),activeforeground="blue")
    button_d1_2.place(x=600,y=870)
    button_d1_3 = tk.Button(Dp,text="作業室",width=5,font=("MSゴシック", "60"),activeforeground="blue")
    button_d1_3.place(x=1200,y=700)
    button_d1_4 = tk.Button(Dp,text="作業室",height=2,font=("MSゴシック", "60"),activeforeground="blue")
    button_d1_4.place(x=1550,y=720)


    label_d2 = tk.Label(Dp,text="二階",font=("MSゴシック", "100"))
    label_d2.place(x=110,y=450)
    canvas_d2 = tk.Canvas(Dp,width=1300,height=50,bg="gray")
    canvas_d2.place(x=400,y=500)
    button_d2_1 = tk.Button(Dp,text="作業室",width=10,font=("MSゴシック", "60"),activeforeground="blue")
    button_d2_1.place(x=600,y=380)
    button_d2_2 = tk.Button(Dp,text="作業室",width=10,font=("MSゴシック", "60"),activeforeground="blue")
    button_d2_2.place(x=600,y=550)
    button_d2_3 = tk.Button(Dp,text="作業室",width=5,font=("MSゴシック", "60"),activeforeground="blue")
    button_d2_3.place(x=1200,y=380)
    button_d2_4 = tk.Button(Dp,text="作業室",height=2,font=("MSゴシック", "60"),activeforeground="blue")
    button_d2_4.place(x=1550,y=400)


    label_d3 = tk.Label(Dp,text="三階",font=("MSゴシック", "100"))
    label_d3.place(x=110,y=150)
    canvas_d3 = tk.Canvas(Dp,width=1300,height=50,bg="gray")
    canvas_d3.place(x=400,y=170)
    button_d3_1 = tk.Button(Dp,text="作業室",width=10,font=("MSゴシック", "60"),activeforeground="blue")
    button_d3_1.place(x=600,y=50)
    button_d3_2 = tk.Button(Dp,text="作業室",width=10,font=("MSゴシック", "60"),activeforeground="blue")
    button_d3_2.place(x=600,y=220)
    button_d3_3 = tk.Button(Dp,text="作業室",width=5,font=("MSゴシック", "60"),activeforeground="blue")
    button_d3_3.place(x=1200,y=50)
    button_d3_4 = tk.Button(Dp,text="作業室",height=2,font=("MSゴシック", "60"),activeforeground="blue")
    button_d3_4.place(x=1550,y=70)


    canvas_d4 = tk.Canvas(Dp,width=1980,height=5,bg="yellow")
    canvas_d4.place(x=0,y=360)
    canvas_d5 = tk.Canvas(Dp,width=1980,height=5,bg="yellow")
    canvas_d5.place(x=0,y=680)


    back_button = tk.Button(Dp,text="戻る",font=("MSゴシック", "50"),activeforeground="blue",command=Dp.destroy)
    back_button.place(x=20,y=20)




#メインウィンドウ
root=tk.Tk()
root.geometry("1980x1080")
root.title("Python")






def fnc_do_1(event):
    print('本館')
def fnc_do_2(event):
    print('電気科')
def fnc_do_3(event):
    print('電子機械科')
def fnc_do_4(event):
    print('機械科')
def fnc_do_5(event):
    print('電子科')




button1 = tk.Button(root, text="本館", font=("MSゴシック", "150"),activeforeground="blue",command=HKp)
button1.place(x=200,y=100)
button2=tk.Button(root,text="電気科",font=("MSゴシック", "150"),activeforeground="blue",command=Ep)
button2.place(x=1000,y=100)
button3=tk.Button(root,text="電子機械科",font=("MSゴシック", "150"),activeforeground="blue",command=Sp)
button3.place(x=200,y=700)
button4=tk.Button(root,text="機械科",font=("MSゴシック", "150"),activeforeground="blue",command=Mp)
button4.place(x=200,y=400)
button5=tk.Button(root,text="電子科",font=("MSゴシック", "150"),activeforeground="blue",command=Dp)
button5.place(x=1000,y=400)


button1.bind("<Button-1>", fnc_do_1)
button2.bind("<Button-1>", fnc_do_2)
button3.bind("<Button-1>", fnc_do_3)
button4.bind("<Button-1>", fnc_do_4)
button5.bind("<Button-1>", fnc_do_5)


root.mainloop()