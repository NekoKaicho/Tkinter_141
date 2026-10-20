import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("420x580")
root.configure(bg="#141c30")

box = tk.Frame(root, bg="#1f2c4c", highlightthickness=2, highlightbackground="#00d2ff", highlightcolor="#00d2ff")
box.pack(padx=15, pady=15, fill="both", expand=True)

tk.Label(box, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 13, "bold"), fg="white", bg="#1f2c4c").pack(pady=10)

form = tk.Frame(box, bg="#1f2c4c")
form.pack()
for i in range(1, 11):
    tk.Label(form, text=f"Nilai Mata Pelajaran {i}:", font=("Arial", 9), fg="#d2dcf0", bg="#1f2c4c", width=18, anchor="w").grid(row=i, column=0, pady=2)
    tk.Entry(form, font=("Arial", 9), width=16, bg="#2d3d63", fg="white", relief="solid", bd=1).grid(row=i, column=1, pady=2)
root.mainloop()