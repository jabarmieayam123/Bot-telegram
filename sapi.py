import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from imapclient import IMAPClient
import pyzmail

EMAIL_SENDER = ("bantuanjebolwangsep@gmail.com")
EMAIL_PASSWORD = ("lmkntdgbhlslscnq")
EMAIL_WHATSAPP = "support@whatsapp.com"
IMAP_SERVER = "imap.gmail.com"

def cek_balasan_nomor():
    nomor = input("Masukkan nomor WhatsApp (+62xxx): ").strip()

    with IMAPClient(IMAP_SERVER) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.select_folder('INBOX')

        messages = server.search(['FROM', 'support@whatsapp.com'])

        if not messages:
            print("\n❌ Tidak ada email dari WhatsApp")
            return

        for uid in reversed(messages):
            raw = server.fetch([uid], ['RFC822'])
            msg = pyzmail.PyzMessage.factory(raw[uid][b'RFC822'])

            body = ""
            if msg.text_part:
                body = msg.text_part.get_payload().decode(
                    msg.text_part.charset or "utf-8",
                    errors="ignore"
                )

            if nomor in body:
                print("\nDari    : support@whatsapp.com")
                print("Waktu  :", msg.get_decoded_header('date'))
                print("\nBalasan:")
                print("-" * 40)
                print(body.strip())
                print("-" * 40)
                return

        print("\n❌ Tidak ada nomor banding anda")
        
def send_email(subject, body):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_WHATSAPP
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)

        print("✅ berhasil banding, tunggu hingga 1-9 hours")

    except Exception as e:
        print(f"❌ Email gagal dikirim | Error: {e}")

number = input("██╗   ██╗███╗   ██╗██████╗  █████╗ ███╗   ██╗\n██║   ██║████╗  ██║██╔══██╗██╔══██╗████╗  ██║\n██║   ██║██╔██╗ ██║██████╔╝███████║██╔██╗ ██║\n██║   ██║██║╚██╗██║██╔══██╗██╔══██║██║╚██╗██║\n╚██████╔╝██║ ╚████║██████╔╝██║  ██║██║ ╚████║\n╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝\n\n\n tools name: Qaxer Unban\n made by: Fiona\n status: VVIP\n informasi: t.me/fionatestie56\n\n Masukkan nomor Whatsapp (contoh +6282737837337i): ").strip()

print("""
━━━━━━━━━━━━━━━━━━━━
📌 PILIH OPSI MENU
━━━━━━━━━━━━━━━━━━━━

1️⃣ 🚀 Unban Spam  
2️⃣ 🔓 Unban Permanent  
3️⃣ 🔧 Fix Login Red  
4️⃣ 🔪 Kill Whatsapp
5️⃣ 💌 check msg whatsapp
0️⃣ ❌ Exit

━━━━━━━━━━━━━━━━━━━━
Note: kalo ga jebol no lu ampas
""")



choice = input("⌨️ Masukkan pilihan (1–5): ").strip()

if choice == "1":
    subject = "Compte WhatsApp bloqué – Demande de réexamen"
    body = f"""Bonjour l’équipe WhatsApp,

Je vous écris pour demander la réactivation de mon numéro WhatsApp {number}, qui a été soudainement bloqué. Au moment du blocage, j’étais en pleine discussion professionnelle importante avec un client.

Je suis convaincu de n’avoir enfreint aucune règle. Si mon activité a été détectée comme du spam, il s’agit probablement d’un malentendu, car j’utilise régulièrement WhatsApp pour mes communications de travail.

WhatsApp est mon principal outil pour rester en contact avec mes clients et collègues. Sans cet accès, il m’est très difficile de poursuivre mes activités professionnelles.

Je vous prie donc de bien vouloir rétablir mon compte. Je m’engage à utiliser WhatsApp en respectant toujours vos conditions et politiques.

Merci beaucoup pour votre compréhension et votre aide.

Cordialement,
Fiona
"""
    send_email(subject, body)

elif choice == "2":
    subject = "Solicitud de revisión de cuenta bloquada"
    body = f"""Hola WhatsApp, somos del equipo de la empresa Marca y queremos expresar que mi cuenta ha sido bloqueada. Sé que he infringido las normas, pero no fui yo. Mis clientes están confundidos porque el servicio de atención al cliente muestra un solo tick. Por favor, WhatsApp, desbloquea esta cuenta lo antes posible.

Número de cuenta: {number}
Por favor, contáctenos pronto por WhatsApp.
"""
    send_email(subject, body)

elif choice == "3":
    subject = "Request for Review – Login Temporarily Unavailable"
    body = f"""Hello WhatsApp Support Team,

I am writing to request a review of my account associated with the phone number:
{number}

I recently received a message stating that login is temporarily unavailable for security reasons.
I believe this may be a mistake.

I kindly request a manual review of my account and reactivation if possible.

Best regards,
Fiona
"""
    send_email(subject, body)

elif choice == "4":
    print("""
===============================
    🚧 COMING SOON 🚧
Fitur sedang dalam pengembangan
===============================
""")
    

elif choice == "5":
    cek_balasan_nomor()

elif choice == "0":
    print("👋 EXIT QAXER UNBAN")
    exit()

else:
    print("❌ Pilihan tidak valid")
