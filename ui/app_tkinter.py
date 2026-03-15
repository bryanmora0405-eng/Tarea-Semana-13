# ui/app_tkinter.py
import tkinter as tk
from tkinter import ttk, messagebox
from modelos.vehiculo import Vehiculo

class GarajeApp:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Gestión de Garaje - UEA")
        self.root.geometry("600x500")

        # Título
        tk.Label(self.root, text="Sistema de Gestión de Garaje", font=("Arial", 14, "bold")).pack(pady=10)

        # Formulario
        frame_form = tk.LabelFrame(self.root, text=" Registro de Vehículo ", padx=10, pady=10)
        frame_form.pack(pady=10, padx=20, fill="x")

        tk.Label(frame_form, text="Placa:").grid(row=0, column=0, sticky="e", pady=5)
        self.entry_placa = tk.Entry(frame_form)
        self.entry_placa.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Marca:").grid(row=1, column=0, sticky="e", pady=5)
        self.entry_marca = tk.Entry(frame_form)
        self.entry_marca.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(frame_form, text="Propietario:").grid(row=2, column=0, sticky="e", pady=5)
        self.entry_propietario = tk.Entry(frame_form)
        self.entry_propietario.grid(row=2, column=1, pady=5, padx=5)

        # Botones
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="Agregar Vehículo", command=self.registrar, bg="#28a745", fg="white", width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="Limpiar", command=self.limpiar_campos, bg="#ffc107", width=15).pack(side=tk.LEFT, padx=5)

        # Tabla
        self.tabla = ttk.Treeview(self.root, columns=("Placa", "Marca", "Propietario"), show="headings")
        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")
        self.tabla.pack(pady=10, padx=20, fill="both", expand=True)

    def registrar(self):
        p = self.entry_placa.get().strip()
        m = self.entry_marca.get().strip()
        pr = self.entry_propietario.get().strip()

        if p and m and pr:
            nuevo = Vehiculo(p, m, pr)
            self.servicio.agregar_vehiculo(nuevo)
            self.actualizar_tabla()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", "Vehículo registrado")
        else:
            messagebox.showwarning("Error", "Llene todos los campos")

    def actualizar_tabla(self):
        # Borrar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        # Cargar de nuevo
        for v in self.servicio.obtener_vehiculos():
            self.tabla.insert("", tk.END, values=(v.placa, v.marca, v.propietario))

    def limpiar_campos(self):
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)
        self.entry_placa.focus()