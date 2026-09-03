"""สมองเป็นเด็กแต่ตัวเป็นผู้ใหญ่"""
# รับข้อความต้นฉบับ และจำนวนตำแหน่ง k
plain_text = input().strip()
k = int(input().strip())

cipher_text = []

for char in plain_text:
    if 'a' <= char <= 'z':
        # แปลงเป็นลำดับ 0-25 -> เลื่อนไปข้างหน้า k ตำแหน่ง -> วนรอบด้วย % 26 -> แปลงกลับเป็นอักขระ
        new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        cipher_text.append(new_char)
    else:
        cipher_text.append(char)

# แสดงผลลัพธ์ข้อความที่เข้ารหัสแล้ว
print("".join(cipher_text))