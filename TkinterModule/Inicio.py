import customtkinter
import tkinter
import TkinterModule.Matrix
class Inicio(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1216x720")
        #Frame ingreso Valor
        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(side="left",padx=25,ipadx=25,pady=100,ipady=100)
        #MatrixFrames
        self.FrameMatrix=customtkinter.CTkScrollableFrame(self)
        self.FrameMatrix.pack(side="left",ipadx=380,fill='y',)
        self.FrameFactorizacion=customtkinter.CTkFrame(self.FrameMatrix)
        self.FrameMatrixA=None
        self.FrameMatrixL=None
        self.FrameMatrixU=None
        self.FrameMatrixPt=None
        
        # Crear el cuadro de texto
        self.Entrybox = customtkinter.CTkEntry(self.frame,width=70,height=10)        
        self.Entrybox.pack(pady=50,ipady=20,ipadx=15)

        self.button_Inicio = customtkinter.CTkButton(self.frame,text="Inicio",command=self.Do_MatrixFrames)
        self.button_Inicio.pack(pady=15,ipady=15)

        self.button_Clear = customtkinter.CTkButton(self.frame,text="clear",command=self.reset_all)
        self.button_Clear.pack(pady=15,ipady=15)
    
    def Do_MatrixFrames(self):
        self.cath_nMatrix()
        self.FrameMatrixA=self.MatrixFrame(self.Do_Matrix(),self.FrameMatrix)
        self.FrameMatrixL=self.MatrixFrame(self.Do_Matrix(),self.FrameFactorizacion)
        self.FrameMatrixU=self.MatrixFrame(self.Do_Matrix(),self.FrameFactorizacion)
        self.FrameMatrixPt=self.MatrixFrame(self.Do_Matrix(),self.FrameFactorizacion)
        self.FrameMatrixA.pack(side='left',padx=15,pady=30)
        self.FrameFactorizacion.pack(side='left',padx=20,ipadx=15,ipady=10,pady=30)
        self.FrameMatrixL.pack(padx=15,pady=10)
        self.FrameMatrixU.pack(padx=15,pady=10)
        self.FrameMatrixPt.pack(padx=15,pady=10)


    def cath_nMatrix(self):
        self.nMatrix=int(self.Entrybox.get())
        print(self.nMatrix)

    def Do_Matrix(self):
        datos=[ [ _ for _ in range(self.nMatrix)] for _ in range(self.nMatrix)]
        print(datos)
        return datos 

    def reset_all(self):
        self.Entrybox.delete(0)
        self.nMatrix=None
        try:
            self.FrameMatrixA.destroy()
            self.FrameMatrixL.destroy()
            self.FrameMatrixU.destroy()
            self.FrameFactorizacion.destroy()
        except:
            pass
        try:
            self.FrameMatrixPt.destroy()
        except:
            pass
        self.FrameMatrixA=None
        self.FrameMatrixL=None
        self.FrameMatrixU=None
        self.FrameMatrixPt=None
        self.FrameFactorizacion=customtkinter.CTkFrame(self.FrameMatrix)
        

        
    def MatrixFrame(self,datos:list,Frame):
        frameM=customtkinter.CTkFrame(Frame)
        for i in range(len(datos)):
            fila = []
            for j in range(len(datos)):
                dato = tkinter.StringVar(value=datos[i][j])
                fila.append(dato)
                label = customtkinter.CTkLabel(frameM, textvariable=dato)
                label.grid(row=i, column=j,ipadx=6,ipady=3,padx=4,pady=2)
        return frameM

