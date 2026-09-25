# =====================================================================
# Module: Smart File Organizer
# Description: Automatically sorts files in a target directory by extension.
# =====================================================================

import os
import shutil

# Extension mapping categories
DIRECTORY_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".sql", ".cpp", ".java"],
    "Media": [".mp4", ".mkv", ".mp3", ".wav"],
}

def run_file_organizer():
    print("\n--- SMART FILE ORGANIZER ---")
    target_dir = input("Enter the path of the directory to organize (leave blank for current dir): ").strip()
    
    if not target_dir:
        target_dir = "."
        
    if not os.path.exists(target_dir):
        print(f"\n[!] Error: Directory '{target_dir}' does not exist.")
        return
        
    print(f"\n[i] Organizing files in: {os.path.abspath(target_dir)}")
    files_moved = 0
    
    try:
        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            
            # Skip directories, only process files
            if os.path.isdir(file_path):
                continue
                
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            
            for category, extensions in DIRECTORY_MAP.items():
                if file_ext in extensions:
                    category_dir = os.path.join(target_dir, category)
                    os.makedirs(category_dir, exist_ok=True)
                    
                    shutil.move(file_path, os.path.join(category_dir, filename))
                    print(f" -> Moved '{filename}' to '{category}/'")
                    files_moved += 1
                    moved = True
                    break
                    
            if not moved and file_ext:
                # Handle other/misc files
                other_dir = os.path.join(target_dir, "Others")
                os.makedirs(other_dir, exist_ok=True)
                shutil.move(file_path, os.path.join(other_dir, filename))
                print(f" -> Moved '{filename}' to 'Others/'")
                files_moved += 1
                
        print(f"\n[+] Organization complete! Total files sorted: {files_moved}")
        
    except Exception as e:
        print(f"\n[!] An error occurred during file organization: {e}")
                  
