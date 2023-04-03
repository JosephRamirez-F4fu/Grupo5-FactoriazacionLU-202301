import customtkinter
import tkinter
import TkinterModule.Matrix
class Inicio(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1080x720")
        #Frame ingreso Valor
        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(side="left",padx=25,ipadx=25,pady=100,ipady=100)
        #MatrixFrames
        self.FrameMatrix=customtkinter.CTkFrame(self)
        self.FrameMatrix.pack(side="left",ipadx=315,fill='y')
        self.FrameMatrixA=None
        self.FrameMatrixL=None
        self.FrameMatrixU=None
        self.FrameMatrixPt=None
        
        # Crear el cuadro de texto
        self.text_box = customtkinter.CTkTextbox(self.frame,width=70,height=10)        
        self.text_box.pack(pady=50,ipady=20,ipadx=15)

        self.button_Inicio = customtkinter.CTkButton(self.frame,text="Inicio")
        self.button_Inicio.pack(pady=15,ipady=15)

        self.button_Clear = customtkinter.CTkButton(self.frame,text="clear")
        self.button_Clear.pack(pady=15,ipady=15)





        
    def MatrixFrame(self,datos:list):
        frameM=customtkinter.CTkFrame(self)
        for i in range(len(datos)):
            fila = []
            for j in range(len(datos)):
                dato = tkinter.StringVar(value=datos[i][j])
                fila.append(dato)
                label = customtkinter.CTkLabel(self.frameM, textvariable=dato)
                label.grid(row=i, column=j,ipadx=10,ipady=5)
        return frameM

