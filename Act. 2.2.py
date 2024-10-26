import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape) + ['□'] 
        self.head = 0 
        self.state = 'q0'  
        self.binary_number = ''

    def step(self):
        """Realiza un paso de la máquina basado en el estado y el símbolo bajo el cabezal."""
        symbol = self.tape[self.head]

        if self.state == 'q0':
            if symbol == '1':
                self.binary_number += symbol  
                self.tape[self.head] = symbol  
                self.head += 1  
                self.state = 'q1'

        elif self.state == 'q1':
            if symbol == '0':
                self.binary_number += symbol
                self.tape[self.head] = symbol
                self.head += 1
                self.state = 'q2'

        elif self.state == 'q2':
            if symbol == '0' or symbol == '1':
                self.binary_number += symbol  
                self.tape[self.head] = symbol
                self.head += 1
            elif symbol == '□':
                self.tape[self.head] = '□'
                self.head += 1
                self.state = 'q3'  

    def run(self):
        """Corre la máquina hasta que alcance el estado de aceptación."""
        while self.state != 'q3':
            self.step()
        return int(self.binary_number, 2)

def run_machine():
    tape = input_entry.get() 

    if not tape.startswith("10") or any(char not in '01' for char in tape):
        messagebox.showerror("Error", "Cadena inválida. Asegúrese de que la cadena comience con '10' y solo contenga 0 y 1.")
        return

    machine = TuringMachine(tape)
    decimal_result = machine.run()

    result_label.config(text=f"Resultado en decimal: {decimal_result}")

window = tk.Tk()
window.title("Máquina de Turing para decimales")
window.geometry("300x200")

input_label = tk.Label(window, text="Ingrese una cadena binaria:")
input_label.pack(pady=10)
input_entry = tk.Entry(window)
input_entry.pack()

run_button = tk.Button(window, text="Ejecutar Máquina", command=run_machine)
run_button.pack(pady=10)
result_label = tk.Label(window, text="Resultado en decimal: ")
result_label.pack(pady=10)

window.mainloop()