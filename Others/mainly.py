from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class InterfazHotel:
    """Clase que permite la gestión de las habitaciones de un hotel"""
    def __init__(self):
        # Window SetUp
        self.window = Tk()
        self.window.config(pady=10, padx=10, bg='#d64747')
        self.window.title("Hotel Manager")
        self.window.resizable(False, False)
        # BBDD
        self.conn = sqlite3.connect('IMDB_Films.db')
        print("Conexión realizada con éxito")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE if not exists HotelManager(id integer PRIMARY KEY, nombre text, "
                       "camas text, banera integer, coste integer, disponibilidad integer, tele integer)")
        self.conn.commit()
        # Tree Widget SetUp
        self.tree = ttk.Treeview(style="mystyle.Treeview", selectmode=BROWSE)
        self.tree.grid(row=0, column=0, columnspan=2, sticky=EW)
        self.tree['columns'] = ('Nombre', 'Nº camas', 'Bañera', 'Coste', 'Disponibilidad', 'Televisión')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('Nombre', width=200, minwidth=200, anchor=CENTER)
        self.tree.column('Nº camas', width=150, minwidth=100, anchor=CENTER)
        self.tree.column('Bañera', width=100, minwidth=100, anchor=CENTER)
        self.tree.column('Coste', width=100, minwidth=100, anchor=CENTER)
        self.tree.column('Disponibilidad', width=100, minwidth=100, anchor=CENTER)
        self.tree.column('Televisión', width=100, minwidth=100, anchor=CENTER)
        # Set up the headings of the tree
        self.tree.heading('#0', text='', anchor=CENTER)
        self.tree.heading('Nombre', text='Nombre', anchor=CENTER)
        self.tree.heading('Nº camas', text='Nº camas', anchor=CENTER)
        self.tree.heading('Bañera', text='Bañera', anchor=CENTER)
        self.tree.heading('Coste', text='Coste', anchor=CENTER)
        self.tree.heading('Disponibilidad', text='Disponibilidad', anchor=CENTER)
        self.tree.heading('Televisión', text='Televisión', anchor=CENTER)
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        # Labels, Entries and Combo Boxes
        self.nombre_lbl = Label(text="Nombre", font=('Helvetica', 15, 'bold'), bg='#d64747')
        self.nombre_lbl.grid(row=1, column=0, sticky=E)
        self.camas_lbl = Label(text="Nº camas", font=('Helvetica', 15, 'bold'), bg='#d64747')
        self.camas_lbl.grid(row=2, column=0, sticky=E)
        self.banera_lbl = Label(text="Bañera", font=('Helvetica', 15, 'bold'), bg='#d64747')
        self.banera_lbl.grid(row=3, column=0, sticky=E)
        self.coste_lbl = Label(text="Coste", font=('Helvetica', 15, 'bold'), bg='#d64747')
        self.coste_lbl.grid(row=4, column=0, sticky=E)
        self.disp_lbl = Label(text="Disponibilidad", font=('Helvetica', 15, 'bold'), bg='#d64747')
        self.disp_lbl.grid(row=5, column=0, sticky=E)
        self.tele_lbl = Label(text="Televisión", font=('Helvetica', 15, 'bold'), bg='#d64747')
        self.tele_lbl.grid(row=6, column=0, sticky=E)
        self.nombre_entry = Entry(font=('Helvetica', 15, 'bold'))
        self.nombre_entry.grid(row=1, column=1, pady=10, sticky=W, padx=10)
        self.camas_entry = Entry(font=('Helvetica', 15, 'bold'))
        self.camas_entry.grid(row=2, column=1, pady=10, sticky=W, padx=10)
        self.banera_combo = ttk.Combobox(font=('Helvetica', 15, 'bold'), values=["True", "False"], state='readonly')
        self.banera_combo.grid(row=3, column=1, pady=10, sticky=W, padx=10)
        self.coste_entry = Entry(font=('Helvetica', 15, 'bold'))
        self.coste_entry.grid(row=4, column=1, pady=10, sticky=W, padx=10)
        self.disp_combo = ttk.Combobox(font=('Helvetica', 15, 'bold'), values=["True", "False"], state='readonly')
        self.disp_combo.grid(row=5, column=1, pady=10, sticky=W, padx=10)
        self.tele_combo = ttk.Combobox(font=('Helvetica', 15, 'bold'), values=["True", "False"], state='readonly')
        self.tele_combo.grid(row=6, column=1, pady=10, sticky=W, padx=10)
        # Buttons
        self.anadir_btn = Button(text="Añadir habitación", font=('Helvetica', 13, 'bold'), command=self.anadir,
                                 bg='#5e1414', fg='#cc6a6a')
        self.anadir_btn.grid(row=7, column=1, sticky=W)
        self.reser_btn = Button(text="Reservar", font=('Helvetica', 13, 'bold'), command=self.reservar,
                                bg='#5e1414', fg='#cc6a6a')
        self.reser_btn.grid(row=8, column=1, sticky=W)
        self.listar_dis_btn = Button(text="Listar Disponibles", font=('Helvetica', 13, 'bold'),
                                     command=self.listar_disponibles, bg='#5e1414', fg='#cc6a6a')
        self.listar_dis_btn.grid(row=9, column=1, sticky=W)
        self.listar_todas_btn = Button(text="Listar Todas", font=('Helvetica', 13, 'bold'),
                                     command=self.listar, bg='#5e1414', fg='#cc6a6a')
        self.listar_todas_btn.grid(row=10, column=1, sticky=W)
        self.borrar_btn = Button(text="Borrar registro", font=('Helvetica', 13, 'bold'),
                                     command=self.delete, bg='#5e1414', fg='#cc6a6a')
        self.borrar_btn.grid(row=11, column=1, sticky=W)
        self.mod_btn = Button(text="Modificar registro", font=('Helvetica', 13, 'bold'),
                                     command=self.update, bg='#5e1414', fg='#cc6a6a')
        self.mod_btn.grid(row=12, column=1, sticky=W)
        self.listar()

        self.window.mainloop()
        self.conn.close()
        print("Conexión finalizada.")

    def renew(self):
        """Función que renueva el contenido del TreeView"""
        curItem = self.tree.focus()
        item = self.tree.item(curItem)
        self.nombre_entry.delete(0, "end")
        self.camas_entry.delete(0, "end")
        self.banera_combo.delete(0, "end")
        self.coste_entry.delete(0, "end")
        self.disp_combo.delete(0, "end")
        self.tele_combo.delete(0, END)
        self.nombre_entry.insert(0, item['values'][0])
        self.camas_entry.insert(0, item['values'][1])
        self.banera_combo.set(item['values'][2])
        self.coste_entry.insert(0, item['values'][3])
        self.disp_combo.set(item['values'][4])
        self.tele_combo.set(item['values'][5])

    def OnDoubleClick(self, event):
        """Función que muestra la información de un registro del TreeView cuando se hace
         doble click sobre él"""
        curItem = self.tree.focus()
        item = self.tree.item(curItem)
        self.renew()
        messagebox.showinfo(title=f"{item['values'][1]}, {item['values'][2]}", message=f"""
        Nombre: {item['values'][0]}
        Nº Camas: {item['values'][1]}
        Bañera: {item['values'][2]}
        Coste: {item['values'][3]}
        Disponibilidad: {item['values'][4]}
        Televisión: {item['values'][5]}""")

    def listar(self):
        """Función que lista en el TreeView, todo el contenido de la BBDD"""
        self.tree.delete(*self.tree.get_children())
        self.c.execute("SELECT nombre, camas, banera, coste, disponibilidad, tele FROM HotelManager")
        rows = self.c.fetchall()
        [self.tree.insert("", END, values=row) for row in rows]

    def anadir(self):
        """Función que permite añadir registros a la BBDD"""
        nombre = self.nombre_entry.get()
        camas = self.camas_entry.get()
        banera = self.banera_combo.get()
        coste = self.coste_entry.get()
        disponible = self.disp_combo.get()
        tele = self.tele_combo.get()
        try:
            self.c.execute(f"""INSERT INTO HotelManager(nombre, camas, banera,
                                                        coste, disponibilidad, tele) VALUES(?,?,?,?,?,?);""",
                           (str(nombre), str(camas),
                            str(banera), int(coste),
                            str(disponible), str(tele))),
        except ValueError:
            messagebox.showwarning(title="Atención!", message="Debes introducir los campos correctamente.")
        self.listar()
        self.conn.commit()

    def reservar(self):
        """Función que permite reservar habitaciones, cambiando su disponibilidad a False"""
        try:
            curItem = self.tree.focus()
            item = self.tree.item(curItem)
            mb = messagebox.askyesno(title="Atención!", message=f"¿Seguro que quieres reservar la habitación "
                                                                f"{str(item['values'][0])}")
        except IndexError:
            messagebox.showwarning(title="Atención!", message="Debes seleccionar un registro para reservar.")
        else:
            if mb:
                self.c.execute(f"""UPDATE HotelManager SET disponibilidad = ? where nombre = ?;""",
                               ("False", str(item["values"][0])))
                self.conn.commit()
                self.listar()

    def listar_disponibles(self):
        """Función que lista solo las habitaciones disponibles"""
        self.tree.delete(*self.tree.get_children())
        self.c.execute("""SELECT nombre, camas, banera, coste, disponibilidad,
         tele FROM HotelManager WHERE disponibilidad = ?;""",
                       ("True",))
        rows = self.c.fetchall()
        [self.tree.insert("", END, values=row) for row in rows]

    def delete(self):
        """Función que permite borrar registros de la BBDD"""
        try:
            curItem = self.tree.focus()
            item = self.tree.item(curItem)
            ask = messagebox.askyesno(title='Atención', message="¿Seguro que quieres borrar el registro?")
            if ask:
                self.c.execute(f'DELETE FROM HotelManager where nombre = ? and coste = ?;', (str(item["values"][0]),
                                                                                             int(item["values"][3]),))
        except IndexError:
            messagebox.showinfo(title='Info', message='Debes seleccionar un registro')
            print("Index Error")

        self.conn.commit()
        self.tree.delete(*self.tree.get_children())
        self.listar()

    def update(self):
        """Función que permite actualizar registros de la BBDD"""
        try:
            if self.nombre_entry.get().isspace() or self.nombre_entry.get() == "" or self.camas_entry.get().isspace() or self.camas_entry.get() == "" or self.coste_entry.get().isspace() or self.coste_entry.get() == "" or self.banera_combo.get().isspace() or self.banera_combo.get() == "" or self.disp_combo.get().isspace() or self.disp_combo.get() == "" or self.tele_combo.get().isspace() or self.tele_combo.get() == "":
                messagebox.showwarning(title="Atención", message="Debes escribir algo")
            else:
                ask = messagebox.askyesno(title='Atención', message="¿Seguro que quieres modificar el registro?")
                if ask:
                    curItem = self.tree.focus()
                    item = self.tree.item(curItem)
                    self.c.execute(f"""UPDATE HotelManager SET nombre = ?, camas = ?, banera = ?,
                     coste = ?, disponibilidad = ?, tele = ? where nombre = ? and coste = ?;""",
                    (str(self.nombre_entry.get()), str(self.camas_entry.get()), str(self.banera_combo.get()),
                        int(self.coste_entry.get()),
                        str(self.disp_combo.get()), str(self.tele_combo.get()), str(item["values"][0]),
                     int(item["values"][3]),))
        except IndexError:
            messagebox.showinfo(title='Info', message='Debes seleccionar un registro')
            print("Index Error")
        except ValueError:
            messagebox.showinfo(title='Info', message='Debes introducir un registro válido.')
            print("Value Error")
        self.conn.commit()
        self.tree.delete(*self.tree.get_children())
        self.listar()


if __name__ == "__main__":
    inte = InterfazHotel()