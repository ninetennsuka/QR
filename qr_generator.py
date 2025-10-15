
"""
QR-код генератор и декодер
Создает QR-коды из текста и декодирует их обратно
"""

import qrcode
from PIL import Image
import io
import base64

def generate_qr_code(data, size=10, border=4):
    """Генерирует QR-код из текста"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr_code(data, filename):
    """Сохраняет QR-код в файл"""
    img = generate_qr_code(data)
    img.save(filename)
    print(f"✅ QR-код сохранен: {filename}")

def qr_to_ascii(data, char='█'):
    """Создает ASCII представление QR-кода"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    matrix = qr.get_matrix()
    ascii_qr = []
    
    for row in matrix:
        ascii_row = ""
        for cell in row:
            ascii_row += char + char if cell else "  "
        ascii_qr.append(ascii_row)
    
    return "\n".join(ascii_qr)

def main():
    print("=== QR-КОД ГЕНЕРАТОР ===\n")
    
    while True:
        print("1. Создать QR-код (текст)")
        print("2. Создать QR-код (ссылка)")
        print("3. ASCII QR-код")
        print("4. Выход")
        
        choice = input("\nВыберите действие: ")
        
        if choice == "1":
            text = input("Введите текст: ")
            if text:
                filename = input("Имя файла (с .png): ") or "qr_code.png"
                save_qr_code(text, filename)
                
        elif choice == "2":
            url = input("Введите URL: ")
            if url:
                if not url.startswith(('http://', 'https://')):
                    url = 'https://' + url
                filename = input("Имя файла (с .png): ") or "qr_url.png"
                save_qr_code(url, filename)
                
        elif choice == "3":
            text = input("Введите текст для ASCII QR: ")
            if text:
                ascii_qr = qr_to_ascii(text)
                print("\n" + ascii_qr)
                save_ascii = input("\nСохранить в файл? (y/n): ")
                if save_ascii.lower() == 'y':
                    with open("ascii_qr.txt", "w", encoding="utf-8") as f:
                        f.write(ascii_qr)
                    print("✅ ASCII QR сохранен в ascii_qr.txt")
                
        elif choice == "4":
            break
            
        print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("❌ Требуется установка: pip install qrcode[pil]")
