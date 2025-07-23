import customtkinter as tk

labes_mass_object = []

def AddObjectToWidget(objec):
    global labes_mass_object
    labes_mass_object.append(objec)

def LoadGui():
    app = tk.CTk()
    app.geometry("640x480")
    app.title('YaTtg Bot')
    app.resizable(False, False)

    tk.set_appearance_mode("Dark")

    body_frame = tk.CTkScrollableFrame(master=app, border_width=2, orientation="vertical",width=680, height=380)
    body_frame.pack(expand=True,anchor='nw')

    for labes in labes_mass_object:
        ctk_label_tmp = tk.CTkLabel(master=body_frame,text=labes,text_color="#1dc497")
        ctk_label_tmp.pack(expand=True,anchor='w',padx=2,pady=2)

    bottom_frame = tk.CTkFrame(master=app)
    bottom_frame.pack(expand=True)

    start_btn = tk.CTkButton(master=bottom_frame, text="Start Bot").grid(row=0,column=1,padx=20)
    exit_btn = tk.CTkButton(master=bottom_frame, text="Stop Bot").grid(row=0,column=0,padx=20)
    restart_btn = tk.CTkButton(master=bottom_frame,text='Restart Bot').grid(row=0,column=2,padx=20)

    app.mainloop()
    while True:
        UploadBodyFrame(bo)