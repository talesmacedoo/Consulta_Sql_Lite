import os
import threading

import customtkinter
import pandas as pd
from tkinter import*
from tkinter import messagebox
#import tkinter.messagebox
from tkinter.ttk import *  

from consulta import Consulta



customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"




class Janela(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Consulta Retorno")
        self.geometry(f"{390}x{460}")
        self.resizable(False,False)

        # configure grid layout (4x4)
        #self.grid_columnconfigure(1, weight=0)
     #   self.grid_columnconfigure((2, 3), weight=0)
     #   self.grid_rowconfigure((0, 1, 2), weight=1)

        #Consulta    
        self.consulta_frame = customtkinter.CTkFrame(self)
        self.consulta_frame.grid(row=0, column=1, padx=10, pady=17, sticky="nsew")
        self.label_campanha = customtkinter.CTkLabel(master=self.consulta_frame, text="C O N S U L T A", font=("Roboto", 14))
        self.label_campanha.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="n")         
        self.campo_telefone = customtkinter.CTkEntry(master=self.consulta_frame, placeholder_text="Telefone com DDD", width=350)
        self.campo_telefone.grid(row=1, column=0, padx=10, pady=20)       

        self.textbox_consulta = customtkinter.CTkTextbox(master=self.consulta_frame, width=260, height=150)
        self.textbox_consulta.grid(row=5, column=0, padx=20, pady=10)                 


        #inicio
        self.envio_frame = customtkinter.CTkFrame(self)
        self.envio_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=0, sticky="nsew")
        self.btn_consultar = customtkinter.CTkButton(master=self.envio_frame, command=self.validador, text="Consultar")
        self.btn_consultar.grid(row=0, column=0, padx=110,pady=10, sticky="nsew")        
        self.btn_sair = customtkinter.CTkButton(master=self.envio_frame, command=self.destroy, text="Sair", fg_color="red")
        self.btn_sair.grid(row=1, column=0, padx=110,pady=10, sticky="nsew")

     #Configurações  
        self.textbox_consulta.configure(font=("Arial",13))
        self.campo_telefone.configure(font=("Arial",14))  
        self.textbox_consulta.configure(state="disable")
        #self.textbox_consulta.configure(state="disabled") 



    def validador(self):
        """
        Método para validar se os campos foram preenchidos 
        """
        telefone  = self.campo_telefone.get()
        telefone = telefone.replace("\n","")
        telefone = telefone.replace(" ","")
        telefone = telefone.replace("(","")
        telefone = telefone.replace(")","")
        telefone = telefone.replace("-","")

        if telefone == "":
            messagebox.showerror(title="Erro", message="Preencha telefone")
        elif len(telefone) < 11:
            messagebox.showerror(title="Erro", message="Insira um nome de telefone válido")
        
        else:
            #telefone  = self.campo_telefone.get()
            self.consultar(telefone)
            
    def tela_consulta(self):
        self.detalhamento_frame.destroy()
        self.envio_frame.destroy()
        self.geometry(f"{490}x{710}")
        self.consulta_frame = customtkinter.CTkFrame(self)
        self.consulta_frame.grid(row=0, column=1, padx=10, pady=17, sticky="nsew")
        self.textbox_consulta = customtkinter.CTkTextbox(master=self.consulta_frame, width=460, height=350)
        self.textbox_consulta.grid(row=0, column=0, padx=0, pady=0) 


    def consultar(self, telefone):
        self.textbox_consulta.configure(state="normal")
        self.textbox_consulta.delete("0.0", "end")

        c1 = Consulta(telefone)
        dados = c1.consultar()
        dados  = c1.tratar_dados(dados)

        self.textbox_consulta.insert("0.0", str(dados))
        self.textbox_consulta.configure(state="disable")




if __name__ == "__main__":
    janela = Janela()
    janela.mainloop()
