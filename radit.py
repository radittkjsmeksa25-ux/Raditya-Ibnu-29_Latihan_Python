import tkinter as tk
from tkinter import ttk, messagebox

# Import modul milik Radit (Sesuaikan dengan nama file di sidebar: modulbangunandatar)
import modulmath
import modulbangunandatar

class AppRadit:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Matematika & Bangun Datar - Radit")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")

        self.layar_utama()

    def layar_utama(self):
        tk.Label(self.root, text="Aplikasi Matematika & Geometri", font=("Arial", 14, "bold"), fg="white", bg="#2c3e50").pack(pady=10)

        notebook = ttk.Notebook(self.root)
        notebook.pack(padx=10, pady=5, fill="both", expand=True)

        tab1 = tk.Frame(notebook, bg="#ecf0f1")
        tab2 = tk.Frame(notebook, bg="#ecf0f1")

        notebook.add(tab1, text="Matematika")
        notebook.add(tab2, text="Bangun Datar")

        # --- TAB 1: MATEMATIKA ---
        tk.Label(tab1, text="Perhitungan Matematika", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(pady=10)
        
        tk.Label(tab1, text="Masukkan Angka 1 / Ganjil Genap:", bg="#ecf0f1").pack(anchor="w", padx=15)
        self.in_m1 = tk.Entry(tab1, font=("Arial", 10))
        self.in_m1.pack(pady=5, padx=15, fill="x")

        tk.Label(tab1, text="Masukkan Angka 2 (Khusus Kali/Bagi):", bg="#ecf0f1").pack(anchor="w", padx=15)
        self.in_m2 = tk.Entry(tab1, font=("Arial", 10))
        self.in_m2.pack(pady=5, padx=15, fill="x")

        f_btn1 = tk.Frame(tab1, bg="#ecf0f1")
        f_btn1.pack(pady=15)
        tk.Button(f_btn1, text="Ganjil/Genap", bg="#3498db", fg="white", command=self.hit_gg).grid(row=0, column=0, padx=3)
        tk.Button(f_btn1, text="Perkalian", bg="#2ecc71", fg="white", command=self.hit_kali).grid(row=0, column=1, padx=3)
        tk.Button(f_btn1, text="Pembagian", bg="#e67e22", fg="white", command=self.hit_bagi).grid(row=0, column=2, padx=3)

        self.lbl_m = tk.Label(tab1, text="Hasil: -", font=("Arial", 11, "bold"), bg="#ecf0f1", fg="#2c3e50")
        self.lbl_m.pack(pady=15)

        # --- TAB 2: BANGUN DATAR ---
        tk.Label(tab2, text="Hitung Bangun Datar", font=("Arial", 11, "bold"), bg="#ecf0f1").pack(pady=10)
        
        tk.Label(tab2, text="Panjang / Alas:", bg="#ecf0f1").pack(anchor="w", padx=15)
        self.in_b1 = tk.Entry(tab2, font=("Arial", 10))
        self.in_b1.pack(pady=5, padx=15, fill="x")

        tk.Label(tab2, text="Lebar / Tinggi:", bg="#ecf0f1").pack(anchor="w", padx=15)
        self.in_b2 = tk.Entry(tab2, font=("Arial", 10))
        self.in_b2.pack(pady=5, padx=15, fill="x")

        f_btn2 = tk.Frame(tab2, bg="#ecf0f1")
        f_btn2.pack(pady=15)
        tk.Button(f_btn2, text="Luas PP", bg="#1abc9c", fg="white", command=self.hit_luas_pp).grid(row=0, column=0, padx=3)
        tk.Button(f_btn2, text="Keliling PP", bg="#9b59b6", fg="white", command=self.hit_kel_pp).grid(row=0, column=1, padx=3)
        tk.Button(f_btn2, text="Luas Jajar Genjang", bg="#34495e", fg="white", command=self.hit_luas_jg).grid(row=0, column=2, padx=3)

        self.lbl_b = tk.Label(tab2, text="Hasil: -", font=("Arial", 11, "bold"), bg="#ecf0f1", fg="#2c3e50")
        self.lbl_b.pack(pady=15)

    # --- PANGGIL FUNGSI MODUL RADIT ---
    def hit_gg(self):
        try:
            val = int(self.in_m1.get())
            res = modulmath.ganjil_genap(val)
            self.lbl_m.config(text=f"Hasil: {res}")
        except Exception:
            messagebox.showerror("Error", "Masukkan angka bulat di kolom 1!")

    def hit_kali(self):
        try:
            a, b = float(self.in_m1.get()), float(self.in_m2.get())
            res = modulmath.perkalian(a, b)
            self.lbl_m.config(text=f"Hasil: {a} x {b} = {res}")
        except Exception:
            messagebox.showerror("Error", "Masukkan Angka 1 & Angka 2!")

    def hit_bagi(self):
        try:
            a, b = float(self.in_m1.get()), float(self.in_m2.get())
            res = modulmath.pembagian(a, b)
            self.lbl_m.config(text=f"Hasil: {a} / {b} = {res}")
        except Exception:
            messagebox.showerror("Error", "Masukkan Angka 1 & Angka 2!")

    def hit_luas_pp(self):
        try:
            p, l = float(self.in_b1.get()), float(self.in_b2.get())
            res = modulbangunandatar.hitung_luas_persegi_panjang(p, l)
            self.lbl_b.config(text=f"Hasil: {res}")
        except Exception:
            messagebox.showerror("Error", "Masukkan Panjang & Lebar!")

    def hit_kel_pp(self):
        try:
            p, l = float(self.in_b1.get()), float(self.in_b2.get())
            res = modulbangunandatar.hitung_keliling_persegi_panjang(p, l)
            self.lbl_b.config(text=f"Hasil: {res}")
        except Exception:
            messagebox.showerror("Error", "Masukkan Panjang & Lebar!")

    def hit_luas_jg(self):
        try:
            a, t = float(self.in_b1.get()), float(self.in_b2.get())
            res = modulbangunandatar.hitung_luas_jajar_genjang(a, t)
            self.lbl_b.config(text=f"Hasil: {res}")
        except Exception:
            messagebox.showerror("Error", "Masukkan Alas & Tinggi!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppRadit(root)
    root.mainloop()
