import json
import os

parent_dir = "C:\\Users\\athkr\\Downloads\\"

# Buka file json
try:
    f = open("./format.json")
    x = json.load(f)
except FileNotFoundError:
    print("File format.json tidak ditemukan.")
    exit()

for category in x['file_format']:
    # --- LEVEL 1: Cek Folder Kategori (misal: Images, Documents) ---
    category_path = os.path.join(parent_dir, category)
    
    if not os.path.exists(category_path):
        os.mkdir(category_path)
        print(f"[BUAT] Folder Kategori: {category}")
    else:
        print(f"[SKIP] Folder Kategori: {category} (Sudah ada)")

    # --- LEVEL 2: Cek Subfolder Ekstensi (misal: .jpg, .pdf) ---
    for ext in x['file_format'][category]:
        # Gabungkan path: Downloads/Images/.jpg
        sub_path = os.path.join(category_path, ext)
        
        if not os.path.exists(sub_path):
            os.mkdir(sub_path)
            print(f"   -> [BUAT SUB] {ext}")
        else:
            # Kalau sudah ada, pass (skip)
            pass 

print("Selesai pengecekan dan pembuatan folder.")