import socket
import datetime
import urllib.parse

# 🛡️ GÜVENLİK HATIRLATMASI: 
# HOST = '127.0.0.1' yaparak tuzağı sadece kendi bilgisayarınla sınırlarsın.
# Eğer '0.0.0.0' yaparsan, aynı Wi-Fi ağındaki herkes bu portu görebilir. 
# Yeni başladığın için '127.0.0.1' en güvenlisidir.
HOST = '127.0.0.1' 
PORT = 8080

def log_activity(ip, data):
    """Saldırı girişimlerini güvenli bir şekilde dosyaya kaydeder."""
    try:
        with open("honeypot_logs.txt", "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] IP: {ip} | {data}\n")
    except Exception as e:
        print(f"Log yazma hatası: {e}")

def start_advanced_honeypot():
    # Soket oluşturma
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Hızlı yeniden başlatma için port meşguliyetini önle
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[*] Gelişmiş Honeypot aktif! Adres: http://{HOST}:{PORT}")
        print("[!] Güvenlik Notu: Sadece localhost üzerinden erişim açık.")
    except Exception as e:
        print(f"Sunucu başlatılamadı: {e}")
        return

    while True:
        client, addr = server.accept()
        try:
            # Gelen isteği oku
            request_bytes = client.recv(2048)
            if not request_bytes:
                continue
                
            request = request_bytes.decode('utf-8', errors='ignore')
            
            # 🔍 VERİ AYIKLAMA (Sniffing)
            if "user=" in request:
                first_line = request.split('\n')[0]
                # URL parametrelerini parçala
                url_parts = first_line.split(' ')
                if len(url_parts) > 1:
                    full_path = url_parts[1]
                    if '?' in full_path:
                        query_string = full_path.split('?')[1]
                        parsed_data = urllib.parse.parse_qs(query_string)
                        
                        user = parsed_data.get('user', ['?'])[0]
                        password = parsed_data.get('pass', ['?'])[0]
                        
                        print(f"\n[!!!] ŞİFRE YAKALANDI!")
                        print(f"Kaynak: {addr[0]} | Kullanıcı: {user} | Şifre: {password}")
                        log_activity(addr[0], f"Giriş Denemesi -> User: {user} | Pass: {password}")

            # 🎭 SAHTE ARAYÜZ (Tuzak)
            html_content = """
            <html>
            <head><title>Secure Admin Login</title></head>
            <body style="background-color:black; color:lime; font-family:monospace; text-align:center; padding-top:100px;">
                <h1 style="color:red;">🛡️ SİSTEM YÖNETİCİ PANELİ 🛡️</h1>
                <p>Kritik erişim için kimlik doğrulaması gereklidir.</p>
                <form action="/" method="GET">
                    Kullanıcı: <input type="text" name="user" style="background:#222; color:white; border:1px solid lime;"><br><br>
                    Şifre: <input type="password" name="pass" style="background:#222; color:white; border:1px solid lime;"><br><br>
                    <input type="submit" value="Giriş Yap" style="padding:10px 20px; cursor:pointer; background:red; color:white; border:none;">
                </form>
                <hr style="width:50%; border:0.5px solid #333;">
                <p style="font-size:10px; color:#555;">Unauthorized access is strictly prohibited.</p>
            </body>
            </html>
            """
            header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n"
            client.sendall((header + html_content).encode('utf-8'))
            
        except Exception as e:
            print(f"Bağlantı işleme hatası: {e}")
        finally:
            client.close()

if __name__ == "__main__":
    start_advanced_honeypot()