# 🍯 Ghost-Entry Honeypot & Sniffer

Bu proje, siber güvenlik eğitim süreçleri için geliştirilmiş, ağ üzerindeki yetkisiz giriş denemelerini yakalayan ve analiz eden bir **Bal Tuzağı (Honeypot)** sistemidir.

## ✨ Özellikler
- **Credential Sniffing:** Sahte bir login paneli üzerinden saldırganın denediği kullanıcı adı ve şifreleri anlık olarak yakalar.
- **Forensic Logging:** Tüm aktiviteleri (IP, Zaman, Eylem) `honeypot_logs.txt` dosyasına adli bilişim standartlarında kaydeder.
- **Security First:** Varsayılan olarak `localhost (127.0.0.1)` üzerinde çalışarak güvenli bir test ortamı sunar.

## 🛡️ Güvenlik ve Korunma Notu
Bu araç tamamen **eğitim ve araştırma** amaçlıdır. 
- Kodun `HOST` ayarını değiştirmeden önce yerel ağ güvenliğinizden emin olun.
- Gerçek sistemlerde "Phishing" amacıyla kullanılması yasal sorumluluk doğurabilir.
- Her zaman izole edilmiş (Sandbox/VM) ortamlarda test yapılması önerilir.
