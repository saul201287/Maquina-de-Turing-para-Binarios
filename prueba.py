import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape) + ['□'] 
        self.head = 0  
        self.state = 'q0' 
        self.current_number = ''  
        self.sum_result = 0 

    def step(self):
        """Realiza un paso de la máquina basado en el estado y el símbolo bajo el cabezal."""
        symbol = self.tape[self.head]

        if self.state == 'q0':
            if symbol == '1':
                self.current_number += symbol
                self.head += 1
                self.state = 'q1'
            else:
                self.state = 'qe'  

        elif self.state == 'q1':
            if symbol == '0':
                self.current_number += symbol
                self.head += 1
                self.state = 'q2'
            else:
                self.state = 'qe'

        elif self.state == 'q2':
            if symbol in ('0', '1'):
                self.current_number += symbol
                self.head += 1
            elif symbol == '+':
                self.sum_result += int(self.current_number, 2)
                self.current_number = ''
                self.head += 1
                self.state = 'q3'
            else:
                self.state = 'qe'

        elif self.state == 'q3':
            if symbol in ('0', '1'):
                self.current_number += symbol
                self.head += 1
                self.state = 'q4'
            else:
                self.state = 'qe'

        elif self.state == 'q4':
            if symbol in ('0', '1'):
                self.current_number += symbol
                self.head += 1
            elif symbol == '+':
                self.sum_result += int(self.current_number, 2)
                self.current_number = ''
                self.head += 1
                self.state = 'q3'
            elif symbol == '=':
                self.sum_result += int(self.current_number, 2)
                self.state = 'q_accept'
            else:
                self.state = 'qe'

    def run(self):
        """Corre la máquina hasta que alcance el estado de aceptación o de error."""
        while self.state not in ('q_accept', 'qe'):
            self.step()

        if self.state == 'q_accept':
            return bin(self.sum_result)[2:]  
        else:
            return None

def evaluate_turing_machine():
    tape = input_entry.get()
    machine = TuringMachine(tape)
    result = machine.run()

    if result:
        messagebox.showinfo("Resultado", f"Cadena válida.\nResultado de la suma en binario: {result}")
    else:
        messagebox.showerror("Error", "La cadena no es válida y no pudo ser evaluada.")

root = tk.Tk()
root.title("Máquina de Turing - Suma Binaria")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Ingrese la cadena binaria que contenga como inicio el binario 10 -> ejemplo '10+11='")
label.grid(row=0, column=0, sticky="w")

input_entry = tk.Entry(frame, width=30)
input_entry.grid(row=1, column=0)

evaluate_button = tk.Button(frame, text="Evaluar", command=evaluate_turing_machine)
evaluate_button.grid(row=2, column=0, pady=10)

root.mainloop()
