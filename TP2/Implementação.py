import tkinter as tk
from tkinter import scrolledtext
import random

def read (pentity,sentity):
	error= ""
	if Universidade[pentity][0] > Universidade[sentity][0]:
		error = "Não tem permissão."
	#print("read")
	return error


def write (pentity,sentity):
	error= ""
	if Universidade[pentity][0] < Universidade[sentity][0]:
		error = "Não tem permissão."
	else:
		random_int = random.randint(1, 10)
		file = "Universidade"+"\\"+Universidade[sentity][1]+"\\"+sentity+ str(random_int)+ ".txt"
		print(file)
		with open(file, 'w') as ficheiro:
			ficheiro.write("Um "+pentity +" manipulou este ficheiro.")

	#print("write")
	return error

Universidade = {"Reitor": (0,"SC"), 
"Serviços Académicos": (1,"SC\\AS"), 
"Investigador Principal": (1,"SC\\ScS"), 
"Professor": (2,"C"), 
"Aluno": (3,"C\\AS"), 
"Investigador": (3,"C\\ScS"),
"Bibliotecario": (4,"P\\ScS"),
"Funcionário de Limpeza": (5,"P\\Empty")}

#print(Universidade)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Modelo Bell-LaPadula numa Universidade")
        self.root.geometry("500x500")

        self.primary_entity = None
        self.secondary_entity = None

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)
        
        self.text_box = scrolledtext.ScrolledText(root, height=5, width=60)
        self.text_box.pack(pady=10)
        
        self.show_entity_buttons()
    
    def show_entity_buttons(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Escolha o primeiro grupo:").pack()
        for entity in list(Universidade.keys()):
            tk.Button(self.main_frame, text=entity, command=lambda e=entity: self.set_primary_entity(e)).pack(pady=2)
    
    def set_primary_entity(self, entity):
        self.primary_entity = entity
        self.show_secondary_entity_buttons()
    
    def show_secondary_entity_buttons(self):
        self.clear_frame()
        tk.Label(self.main_frame, text=f"{self.primary_entity} -> \nEscolha o segundo grupo:").pack()
        for entity in list(Universidade.keys()):
            tk.Button(self.main_frame, text=entity, command=lambda e=entity: self.set_secondary_entity(e)).pack(pady=2)
    
    def set_secondary_entity(self, entity):
        self.secondary_entity = entity
        self.show_action_buttons()
    
    def show_action_buttons(self):
        self.clear_frame()
        label_text = f"{self.primary_entity} -> {self.secondary_entity} \n Escolha uma ação:"
        
        tk.Label(self.main_frame, text=label_text).pack()
        
        tk.Button(self.main_frame, text="Read", command=lambda: self.log_action("Read")).pack(pady=2)
        tk.Button(self.main_frame, text="Write", command=lambda: self.log_action("Write")).pack(pady=2)
        
        tk.Button(self.main_frame, text="Voltar", command=self.show_entity_buttons).pack(pady=5)
    
    def log_action(self, action):
        # correr read ou write dependendo da action
        self.text_box.insert(tk.END, f"{self.primary_entity} -> {self.secondary_entity}: {action}\n")
        if action == "Read":
            error = read(self.primary_entity,self.secondary_entity)
        if action == "Write":
            error = write(self.primary_entity,self.secondary_entity)
        if error != "":
            self.text_box.insert(tk.END, f"Erro: {error}\n")
        self.text_box.see(tk.END)
        self.primary_entity = None
        self.secondary_entity = None
        self.show_entity_buttons()
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

root = tk.Tk()
app = App(root)
root.mainloop()