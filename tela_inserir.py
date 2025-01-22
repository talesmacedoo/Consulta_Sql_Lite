from bs4 import BeautifulSoup
from time import sleep   
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import*
from tkinter import messagebox
import os
import threading
from tkinter import filedialog
import customtkinter
import pandas as pd
from tkinter.ttk import *  
import requests



customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"




class Janela(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("LuzirSoftware.py")
        self.geometry(f"{490}x{610}")
        self.resizable(False,False)

        # configure grid layout (4x4)
        #self.grid_columnconfigure(1, weight=0)
     #   self.grid_columnconfigure((2, 3), weight=0)
     #   self.grid_rowconfigure((0, 1, 2), weight=1)
                            

        #Campanha     
        self.detalhamento_frame = customtkinter.CTkFrame(self)
        self.detalhamento_frame.grid(row=0, column=1, padx=10, pady=17, sticky="nsew")
        self.label_campanha = customtkinter.CTkLabel(master=self.detalhamento_frame, text="INSERIR BASE", font=("Roboto", 14))
        self.label_campanha.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="n")         
        #self.nomeCam = customtkinter.CTkEntry(master=self.detalhamento_frame, placeholder_text="Nome da Campanha:", width=350)
        #self.nomeCam.grid(row=1, column=0, padx=10, pady=20)       
        self.caminho_arquivo = customtkinter.CTkLabel(master=self.detalhamento_frame, text="Arquivo")
        self.caminho_arquivo.grid(row=3, column=0, padx=0, pady=0)
        self.browse_file = customtkinter.CTkButton(master=self.detalhamento_frame, command=self.browseFilesTel, text="Arquivo")
        self.browse_file.grid(row=4, column=0, padx=0, pady=0)  
        self.textbox_arquivo = customtkinter.CTkTextbox(master=self.detalhamento_frame, width=260, height=150)
        self.textbox_arquivo.grid(row=5, column=0, padx=20, pady=10)                 

     #Envio
        self.envio_frame = customtkinter.CTkFrame(self)
        self.envio_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=0, sticky="nsew")
        self.btn_iniciar = customtkinter.CTkButton(master=self.envio_frame, command=self.validador, text="Iniciar")
        self.btn_iniciar.grid(row=0, column=0, padx=110,pady=10, sticky="nsew")        
        self.btn_sair = customtkinter.CTkButton(master=self.envio_frame, command=self.destroy, text="Sair", fg_color="red")
        self.btn_sair.grid(row=1, column=0, padx=110,pady=10, sticky="nsew")

     #Configurações  
        self.textbox_arquivo.configure(state="disabled") 

    def mudanca_aparencia(self, new_appearance_mode: str):
        """
        Método para alterar a aparência da tela de login  
        """        
        customtkinter.set_appearance_mode(new_appearance_mode)

    def browseFilesTel(self):
        """
        Método para abrir o filebrowser e pesquisar pelo arquivo de telefones
        """        
        self.filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.xlsx*"),
                                                        ("all files",
                                                            "*.*")))
        
        # Change label contents
        self.caminho_arquivo.configure(text=self.filename)
        dados =  pd.read_excel(self.filename)
        self.textbox_arquivo.configure(state="normal")
        self.textbox_arquivo.delete("0.0",'end-1c')
        self.textbox_arquivo.insert("0.0",str(dados))
        #self.geometry(f"{90}x{510}")

    def validador(self):
        """
        Método para validar se os campos foram preenchidos 
        """
        if self.nomeCam.get() == "":
             messagebox.showerror(title="Erro", message="Preencha nome da campanha")
        else:
            self.loteCpf = self.filename
            self.nomeDaCampanha = self.nomeCam.get()
            #t1 = threading.Thread(target=)
            #t2 = threading.Thread(target=)

            #t2.start()
            #t2.join()
            
            #t1.start()
            #t1.join()
            
    def tela_consulta(self):
        self.detalhamento_frame.destroy()
        self.envio_frame.destroy()
        self.geometry(f"{490}x{710}")
        self.consulta_frame = customtkinter.CTkFrame(self)
        self.consulta_frame.grid(row=0, column=1, padx=10, pady=17, sticky="nsew")
        self.textbox_consulta = customtkinter.CTkTextbox(master=self.consulta_frame, width=460, height=350)
        self.textbox_consulta.grid(row=0, column=0, padx=0, pady=0) 

        


if __name__ == "__main__":
    janela = Janela()
    janela.mainloop()
