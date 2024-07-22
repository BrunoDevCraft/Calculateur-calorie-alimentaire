import tkinter as tk

class AutocompleteEntry(tk.Entry):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.completion_list = []
        self._hits = []
        self.listbox = None
        self.scrollbar = None
        self.auto_update = True  # Variable pour contrôler la mise à jour automatique
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self.bind('<FocusOut>', self.handle_focusout)
        self.bind('<Button-1>', self.handle_click)
        self.bind('<ButtonRelease-1>', self.handle_click)

    def set_completion_list(self, completion_list):
        self.completion_list = sorted(completion_list)
        if self.auto_update:
            self.update_listbox()

    def update_listbox(self):
        if not self.completion_list:
            return

        if self.listbox is None:
            self.listbox = tk.Listbox(self.master, height=5)
            self.listbox.bind('<ButtonRelease-1>', self.select_suggestion)
            self.listbox.place_forget()

            self.scrollbar = tk.Scrollbar(self.master, orient="vertical", command=self.listbox.yview)
            self.listbox.config(yscrollcommand=self.scrollbar.set)
            self.scrollbar.place_forget()

        self.listbox.delete(0, tk.END)
        self._hits = [item for item in self.completion_list if item.lower().startswith(self.get().lower())]
        
        if self._hits:
            for item in self._hits:
                self.listbox.insert(tk.END, item)
            # Choisissez vos propres valeurs pour x_offset et y_offset
            self.update_listbox_position(x_offset=-12, y_offset=-25)
            self.listbox.lift()
            self.scrollbar.lift()
        else:
            self.listbox.place_forget()
            self.scrollbar.place_forget()

    def update_listbox_position(self, x_offset=0, y_offset=0):
        x = self.winfo_x() + x_offset
        y = self.winfo_y() + self.winfo_height() + y_offset
        listbox_height = self.listbox.winfo_reqheight()

        # Vérifiez si la listbox dépasse le cadre de la fenêtre
        if y + listbox_height > self.master.winfo_height():
            y = self.winfo_y() - listbox_height + y_offset

        self.listbox.place(x=x, y=y, width=self.winfo_width())
        self.scrollbar.place(x=x + self.winfo_width(), y=y, height=self.listbox.winfo_height())

    def handle_keyrelease(self, event):
        if event.keysym in ('BackSpace', 'Left', 'Right', 'Up', 'Down', 'Shift', 'Control', 'Tab'):
            return
        
        current_text = self.get()
        if len(current_text) > 0 and not current_text[0].isupper():
            current_text = current_text[0].upper() + current_text[1:]
            self.delete(0, tk.END)
            self.insert(0, current_text)
            self.icursor(tk.END)
        
        if self.auto_update:
            self.update_listbox()

    def handle_focusout(self, event):
        self.after(100, self.listbox.place_forget)
        self.after(100, self.scrollbar.place_forget())

    def handle_click(self, event):
        if self.auto_update:
            self.update_listbox()

    def select_suggestion(self, event):
        if self.listbox:
            selected_index = self.listbox.curselection()
            if selected_index:
                selection = self.listbox.get(selected_index[0])
                if selection:
                    self.delete(0, tk.END)
                    self.insert(0, selection)
                    self.icursor(tk.END)
                    self.listbox.place_forget()
                    self.scrollbar.place_forget()
                    self.focus_set()

# Exemple d'utilisation
#root = tk.Tk()
#entry = AutocompleteEntry(root)
#entry.set_completion_list(['Apple', 'Apricot', 'Avocado', 'Banana', 'Blackberry', 'Blueberry', 'Cherry', 'Coconut', 'Cranberry', 'Date', 'Fig', 'Grape', 'Kiwi', 'Lemon', 'Lime', 'Mango', 'Melon', 'Nectarine', 'Orange', 'Papaya', 'Peach', 'Pear', 'Pineapple', 'Plum', 'Pomegranate', 'Raspberry', 'Strawberry', 'Watermelon'])
#entry.pack()
#root.mainloop()
