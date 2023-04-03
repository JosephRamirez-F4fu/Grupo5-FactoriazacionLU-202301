import tkinter
import customtkinter  # <- import the CustomTkinter module
import TkinterModule.Creditos
import TkinterModule.Inicio

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("1080x720")
            self.title("Factorizacion LU")
            self.toplevel_window = None
            self.font=customtkinter.CTkFont(family="Courier",size=50,weight="bold",underline=True)

            #Tiulo del proyecto
            self.NameProject=tkinter.StringVar(value="Factorización LU")
            self.LabelNameProject=customtkinter.CTkLabel(self,textvariable= self.NameProject,font=self.font, corner_radius=8)
            self.LabelNameProject.pack(side="top", padx=200,pady=100)

            #Grupo nombre y Salon Frame
            self.NameGroup=tkinter.StringVar(value="Grupo 5")
            self.NameClass=tkinter.StringVar(value="Algebra Lineal CC52")
            
            #Creando label y Frame
            self.FrameGroupClass=customtkinter.CTkFrame(self)
            self.LabelNameGroup=customtkinter.CTkLabel(self.FrameGroupClass,textvariable=self.NameGroup)
            self.LabelNameClass=customtkinter.CTkLabel(self.FrameGroupClass,textvariable=self.NameClass)
            
            #fuentes para Labels

            fontLabels=customtkinter.CTkFont(family="Courier",size=24)
            self.LabelNameGroup.configure(font=fontLabels)
            self.LabelNameClass.configure(font=fontLabels)

            #Empaquetando Frame Class Group 
            self.LabelNameGroup.pack(side="left",ipadx=15)
            self.LabelNameClass.pack(side="right",ipadx=20)
            self.FrameGroupClass.pack(ipadx=70,ipady=40)
            
            #nombre boton inicio
            self.NameInicio=tkinter.StringVar(value="Iniciar")

            #Creando boton inicio
            self.ButtonInicio=customtkinter.CTkButton(self,textvariable=self.NameInicio,command=self.open_inicio)
            self.ButtonInicio.configure(font=fontLabels)
            self.ButtonInicio.pack(pady=80,fill="x",ipady=60)

            #creando boton Creditos y copy
            self.NameCredits=tkinter.StringVar(value="Creditos")
            self.NameCopy=tkinter.StringVar(value="copyright © 2023")

            #creando label y frame
            self.FrameCreditsCopy=customtkinter.CTkFrame(self)
            self.ButtonCredits=customtkinter.CTkButton(self.FrameCreditsCopy,textvariable=self.NameCredits,command=self.open_creditos)
            self.LabelCopyirght=customtkinter.CTkLabel(self.FrameCreditsCopy,textvariable=self.NameCopy)

            #Empaquetando Frame Copy Credits
            self.ButtonCredits.pack(side="left",padx="40")
            self.LabelCopyirght.pack(side="right",padx="40")
            self.FrameCreditsCopy.pack(side="bottom",fill="x")
            

    def open_creditos(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TkinterModule.Creditos.Creditos(self)
        else:
            self.toplevel_window.focus()
    
    def open_inicio(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TkinterModule.Inicio.Inicio(self)
        else:
            self.toplevel_window.focus()
