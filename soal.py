import tkinter as tk
from tkinter import ttk

def prediksi():
    win = tk.Toplevel(root, bg="#00d2ff")
    win.geometry("320x100")
    tk.Label(win, text="Prediksi Prodi: Teknologi Informasi", font=("Arial", 11, "bold"), fg="#00e5ff", bg="#1a2540").pack(fill="both", expand=True, padx=3, pady=3)

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x580")
root.configure(bg="#141c30")

box = tk.Frame(root, bg="#1f2c4c", highlightthickness=2, highlightbackground="#00d2ff", highlightcolor="#00d2ff")
box.pack(padx=15, pady=15, fill="both", expand=True)

tk.Label(root, text="Tkinter | Praktikum Pemrograman Multiplatform", font=("Arial", 8), fg="#7082a6", bg="#141c30").pack(side="bottom", pady=5)

tk.Label(box, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 13, "bold"), fg="white", bg="#1f2c4c").pack(pady=10)

form = tk.Frame(box, bg="#1f2c4c")
form.pack()
for i in range(1, 11):
    tk.Label(form, text=f"Nilai Mata Pelajaran {i}:", font=("Arial", 9), fg="#d2dcf0", bg="#1f2c4c", width=18, anchor="w").grid(row=i, column=0, pady=2)
    tk.Entry(form, font=("Arial", 9), width=16, bg="#2d3d63", fg="white", relief="solid", bd=1).grid(row=i, column=1, pady=2)

tk.Label(box, text="Pilihan Jurusan Anda:", font=("Arial", 9, "bold"), fg="#00e5ff", bg="#1f2c4c").pack(pady=(10, 2))
prodi = ttk.Combobox(box, values=["Teknologi Informasi", "Teknik Informatika", "Sistem Informasi", "Kedokteran"], state="readonly", width=20)
prodi.set("Teknologi Informasi")
prodi.pack(pady=(0, 10))

tk.Button(box, text="Hasil Prediksi", command=prediksi, font=("Arial", 9, "bold"), bg="#e6ecf5", relief="groove").pack()

root.bind("<Return>", lambda event: prediksi())

root.mainloop()