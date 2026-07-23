# บันทึกการแก้โจทย์

ไฟล์นี้ต้องเขียนโดยนักศึกษาด้วยคำพูดของตนเอง

ใช้ template นี้เฉพาะกับโจทย์ OJ ที่ถูกระบุว่าต้องส่ง learning log เท่านั้น

ห้ามให้ AI เขียนไฟล์นี้แทนคุณ AI อาจช่วยตรวจ grammar, formatting หรือความชัดเจนได้ หลังจากที่คุณเขียนเนื้อหาของตนเองแล้ว

ถ้าใช้ AI กับโจทย์ learning-log-required นี้ ต้องทำไฟล์ `ai_reflection.md` ด้วย

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3025 - Season
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
555041
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
30-60 minutes
```

เลือกหนึ่งข้อ:

```text
0-15 minutes
15-30 minutes
30-60 minutes
1-3 hours
3-6 hours
6-24 hours
1-3 days
4-7 days
1-4 weeks
More than 4 weeks
```

วิธีนับเวลา:

- นับเฉพาะเวลาที่ตั้งใจทำโจทย์นี้ด้วยตนเองจริง ๆ
- เริ่มนับตั้งแต่ตอนที่อ่านโจทย์ครั้งแรก
- ไม่นับเวลาพัก กินข้าว เรียน นอน เวลาที่ทำโจทย์อื่น หรือเวลาที่ไม่ได้ทำโจทย์นี้
- ถ้าใช้ AI ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อน prompt แรกที่ถาม AI
- ถ้าถามเพื่อน TA หรือผู้สอน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือครั้งแรก
- ถ้าใช้ทั้ง AI และความช่วยเหลือจากคน ให้นับเฉพาะเวลาที่ทำด้วยตนเองก่อนขอความช่วยเหลือจากภายนอกครั้งแรก ไม่ว่าจะเป็น AI หรือคน
- ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้นับเวลาถึงก่อนเขียน `submission.md`
- ประมาณเวลาได้ แต่ต้องซื่อสัตย์

---

## 2. ความเข้าใจโจทย์ของฉัน

เขียนโจทย์ด้วยคำพูดของตนเอง

ให้อธิบาย input, output และ constraints สำคัญด้วย

ถ้ายังไม่เข้าใจโจทย์ทั้งหมด ให้เขียนสิ่งที่เข้าใจในตอนนี้ ความเข้าใจอาจยังไม่ครบหรืออาจผิดได้ แต่ต้องพยายามอธิบายอย่างจริงใจ

```text
input:รับนำนวนเต็ม2ตัวบรรทัดแรกรับเดือน และบรรทัดสองรับวันที่

output: โปรแกรมจะพิมพ์มาตามที่โจทย์กำหนด สมมุติ รับค่าบรรทัด 1 = 1 และ 2 = 20 โปรแกรมจะแสดง winter

constraints:ในเดือนที่3หารลงตัว หลังจากวันที่21 ฤดูกาลจะเปลี่ยนไปเป็นอีกฤดู
```

---

## 3. แผนแรกของฉัน

เขียนแผนแรกก่อนรับความช่วยเหลือจาก AI เพื่อน TA ผู้สอน หรือก่อนสรุป code สุดท้าย

ถ้าใช้ AI ให้เขียนแผนที่มีอยู่ก่อน prompt แรกที่ถาม AI

ถ้าถามเพื่อน TA หรือผู้สอน ให้เขียนแผนที่มีอยู่ก่อนถาม

ถ้าไม่ได้ใช้ AI และไม่ได้ขอความช่วยเหลือจากคน ให้เขียนแผนที่มีอยู่ก่อนหรือระหว่างเริ่มเขียน code

แผนนี้เขียนแบบคร่าว ๆ ได้ อาจยังไม่สมบูรณ์หรืออาจต่างจากวิธีสุดท้าย

สามารถเขียนเป็น pseudocode, flowchart idea หรือขั้นตอนความคิดได้

```text
step1 รับค่าจำนวนเต็ม2ค่า
step2 ตรวจค่าแรกว่าตรงกับเดือนไหน
step3 ตรวจว่าใช่เดือนที่ 3 หารลงตัวไหม
step4 ถ้าใช่ ให้ดูว่าใช่วันที่ 21ไหม ถ้าใช่ ให้คำตอบเป็นเเดือนถัดไป

```

---

## 4. วิธีสุดท้ายที่ใช้จริง

อธิบายสั้น ๆ ว่า algorithm หรือวิธีสุดท้ายที่ใช้จริงใน code ที่ส่งคืออะไร

หัวข้อนี้ต่างจาก Section 3:

- Section 3 คือแผนแรกก่อนใช้ AI ก่อนรับความช่วยเหลือจากคน หรือก่อนเขียน code สุดท้าย
- Section 4 คือวิธีสุดท้ายที่ใช้ใน solution จริง
- ถ้าวิธีสุดท้ายเหมือนกับแผนแรก ให้เขียนว่าเหมือนกัน และอธิบายสั้น ๆ ว่าทำไม

ห้ามคัดลอกคำอธิบายจาก AI

ห้ามคัดลอกคำอธิบายจากคนอื่น

```text
เหมือนแผนแรก แค่ปรับแก้บัคนิดหน่อย
```

---

## 5. การทดสอบของฉัน

เขียน test cases อย่างน้อย 3 กรณีที่ลองเองหรือออกแบบเอง

พยายามเลือก test cases ที่แตกต่างกัน

แต่ละ test case ให้อธิบายว่าทำไมเลือกกรณีนั้น

ถ้า input หรือ output มีหลายบรรทัด ให้เขียนไว้ใน text blocks

### Test Case 1

ทำไมเลือก case นี้:

```text
'''season'''
month = input()
day = int(input())

if month == ('1','2'):
    print('winter')
elif month == '3':
    if day < 21:
        print('winter')
    elif day >= 21:
        print('spring')

if month == '4' or month == '5':
    print('spring')
elif month == '6':
    if day < 21:
        print('spring')
    elif day >= 21:
        print('summer')

if month == '7' or month == '8':
    print('summer')
elif month == '9':
    if day < 21:
        print('summer')
    elif day >= 21:
        print('fall')

if month == '10' or month == '11':
    print('fall')
elif month == '12':
    if day < 21:
        print('fall')
    elif day >= 21:
        print('winter')

ลองปรับให้โปรแกรมสั้นลง
```

Input:

```text
1
21
```

Expected output:

```text
winter
```

Actual output:

```text
ไม่มีอะไรออกมา
```

Result:

```text
Not Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
'''season'''
month = input()
day = int(input())

if month in ('1','2'):
    print('winter')
elif month == '3':
    if day < 21:
        print('winter')
    elif day >= 21:
        print('spring')

if month in ('3','4'):
    print('spring')
elif month == '6':
    if day < 21:
        print('spring')
    elif day >= 21:
        print('summer')

if month in ('7','8'):
    print('summer')
elif month == '9':
    if day < 21:
        print('summer')
    elif day >= 21:
        print('fall')

if month in ('9','10'):
    print('fall')
elif month == '12':
    if day < 21:
        print('fall')
    elif day >= 21:
        print('winter')

เป็นรอบสองที่ใส่แต่ใส่เลขผิดนิดหน่อย
```

Input:

```text
9
20
```

Expected output:

```text
summer
```

Actual output:

```text
fall
summer
```

Result:

```text
Not Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
'''season'''
month = input()
day = int(input())

if month in ('1','2'):
    print('winter')
elif month == '3':
    if day < 21:
        print('winter')
    elif day >= 21:
        print('spring')

if month in ('4','5'):
    print('spring')
elif month == '6':
    if day < 21:
        print('spring')
    elif day >= 21:
        print('summer')

if month in ('7','8'):
    print('summer')
elif month == '9':
    if day < 21:
        print('summer')
    elif day >= 21:
        print('fall')

if month in ('10','11'):
    print('fall')
elif month == '12':
    if day < 21:
        print('fall')
    elif day >= 21:
        print('winter')
เป็นคำตอบสุดท้าย

```

Input:

```text
3
21
```

Expected output:

```text
spring
```

Actual output:

```text
spring
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
No
```

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

ถ้าใช่ ให้อธิบายสั้น ๆ ว่าได้รับความช่วยเหลือแบบใด

ตัวอย่างที่อนุญาต:

- อธิบายความหมายของโจทย์
- อธิบาย concept การเขียนโปรแกรม
- ให้ hint เกี่ยวกับแนวทาง
- คุยเรื่อง debugging
- คุยเรื่อง test cases
- ช่วยอธิบาย error message

สิ่งที่ไม่อนุญาต:

- คัดลอก code ของผู้อื่น
- ส่ง solution ของผู้อื่น
- ขอให้ผู้อื่นเขียน solution ให้
- ใช้ OJ submission ของผู้อื่น
- ขอให้ผู้อื่นส่ง OJ แทน

ใครช่วยคุณ

```text

```

เขาช่วยอะไร

```text

```

คุณยังทำอะไรด้วยตนเอง

```text

```

คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |
