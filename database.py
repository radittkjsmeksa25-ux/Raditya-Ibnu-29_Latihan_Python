import gspread
from google.oauth2.service_account import Credentials

def get_sheet():
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file("credentials.json", scopes=scope)
        client = gspread.authorize(creds)
        sheet = client.open("database").sheet1
        if sheet.cell(1, 1).value == "":
            sheet.update("A1:B1", [["username", "password"]])
        return sheet
    except Exception as e:
        return None

def login_user(username, password):
    sheet = get_sheet()
    if not sheet:
        return False, "Gagal koneksi ke Google Sheets / file credentials.json tidak ada!"
    
    data = sheet.get_all_values()
    for baris in data[1:]:
        if len(baris) >= 2 and baris[0] == username and baris[1] == password:
            return True, f"Selamat datang, {username}!"
    return False, "Username atau password salah!"

def buat_akun_user(username, password):
    sheet = get_sheet()
    if not sheet:
        return False, "Gagal koneksi ke Google Sheets!"
    
    data = sheet.get_all_values()
    for baris in data[1:]:
        if len(baris) >= 1 and baris[0] == username:
            return False, "Username sudah digunakan!"
    
    sheet.append_row([username, password])
    return True, "Akun berhasil dibuat!"
