import customtkinter
import tkinter
from PIL import Image

class Creditos(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1080x720")
        self.title("Creditos")
        fontTitulo=customtkinter.CTkFont(family="Courier",size=64,underline=True)
        LabelEstudiantes=customtkinter.CTkLabel(self,text="Estudiantes",font=fontTitulo)
        LabelEstudiantes.pack(pady=50)

        #Frame donde se muestran los nombres y codigos de los Estudiantes

        Estudiantes = [ {"nombre":"Joseph Ramirez Sarmiento","codigo":"U20211C828"},
                       {"nombre":"Diego Alexander Huaman Sirio","codigo":"U20211F983"},
                       {"nombre":"Sara Gabriela Estrada Fernández","codigo":"U20211A109"},
                       {"nombre":"Jhamil Brijan Peña Cardenas","codigo":"U201714492 "},
                       {"nombre":"César Augusto Torres Paniagua ","codigo":"U201615124 "}]
        
        frameEstudiantes=customtkinter.CTkFrame(self)
        frameEstudiantes.pack(pady=50)

        FontEstudiantes=customtkinter.CTkFont(family="Courier",size=24)

        labels=[]
        for i in Estudiantes:
            strName=tkinter.StringVar(value=i["nombre"])
            strCodigo=tkinter.StringVar(value=i["codigo"])
            labelName=customtkinter.CTkLabel(frameEstudiantes,textvariable=strName,font=FontEstudiantes)
            labelCodigo=customtkinter.CTkLabel(frameEstudiantes,textvariable=strCodigo,font=FontEstudiantes)
            labels.append([labelName,labelCodigo])
        
        for i in range(5):
            for j in range(2):
                labels[i][j].grid(row=i,column=j,padx=15,pady=5)

        my_image = customtkinter.CTkImage(light_image=Image.open("img\git-cat.png"),
                                          dark_image=Image.open("img\git-cat.png"),size=(240,240))

        LabelCat = customtkinter.CTkLabel(self, image=my_image,text="")
        LabelCat.pack()