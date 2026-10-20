import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x580")
root.configure(bg="#141c30")

box = tk.Frame(root, bg="#1f2c4c", highlightthickness=2, highlightbackground="#00d2ff", highlightcolor="#00d2ff")
box.pack(padx=15, pady=15, fill="both", expand=True)

root.mainloop()