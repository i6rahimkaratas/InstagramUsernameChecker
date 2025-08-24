import requests
import time
import datetime
from playsound import playsound
import tkinter as tk
from tkinter import messagebox
import os

TARGET_USERNAME = "i6rahimkaratas" 
CHECK_INTERVAL_SECONDS = 3600 

def check_username_availability(username):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            return "✅ Alınabilir"
        elif response.status_code == 200:
            return "❌ Alınmış"
        else:
            return f"❓ Kontrol edilemedi (Durum Kodu: {response.status_code})"
    except requests.exceptions.RequestException:
        return "Hata: İnternet bağlantısı kontrol edilemedi."

def play_alert_sound():
    try:
        if os.path.exists("alert.mp3"):
            print("🔊 Uyarı sesi çalınıyor...")
            playsound("alert.mp3")
        else:
            print("⚠️ Uyarı: 'alert.mp3' ses dosyası bulunamadı!")
    except Exception as e:
        print(f"Ses çalınırken bir hata oluştu: {e}")

def show_visual_alert(username):
    print("🖥️ Görsel bildirim gösteriliyor...")
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showinfo(
        "Kullanıcı Adı Müsait!",
        f"Harika haber!\n\n'{username}' adlı kullanıcı adı artık alınabilir durumda!\n\nHemen al!"
    )
    root.destroy()

if __name__ == "__main__":
    print("="*50)
    print("Instagram Kullanıcı Adı Otomatik Takip Programı Başlatıldı")
    print(f"🎯 Hedef Kullanıcı Adı: {TARGET_USERNAME}")
    print(f"⏰ Kontrol Aralığı: {CHECK_INTERVAL_SECONDS / 60} dakika ({CHECK_INTERVAL_SECONDS} saniye)")
    print("Programı durdurmak için CTRL+C tuşlarına basın.")
    print("="*50)

    try:
        while True:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = check_username_availability(TARGET_USERNAME)
            print(f"[{current_time}] '{TARGET_USERNAME}' kontrol ediliyor... Sonuç: {result}")
            if result == "✅ Alınabilir":
                print("\n" + "!"*50)
                print(f"🎉 MÜJDE! '{TARGET_USERNAME}' KULLANICI ADI BOŞA DÜŞTÜ! 🎉")
                print("!"*50 + "\n")
                play_alert_sound()
                show_visual_alert(TARGET_USERNAME)
                print("Program görevini tamamladı ve durduruluyor.")
                break
            time.sleep(CHECK_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nProgram kullanıcı tarafından durduruldu. Hoşça kalın!")
