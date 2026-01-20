from pdf2image import convert_from_path
import os

# แปลง PDF เป็นรูปภาพ
pdf_path = "Commissions.pdf"
print(f"กำลังแปลง {pdf_path}...")

try:
    # แปลง PDF เป็นรูปภาพ (DPI สูงเพื่อคุณภาพดี)
    images = convert_from_path(pdf_path, dpi=300)
    
    print(f"พบ {len(images)} หน้า")
    
    # บันทึกแต่ละหน้าเป็นไฟล์รูปภาพ
    for i, image in enumerate(images, start=1):
        output_path = f"image{i}.jpg"
        image.save(output_path, 'JPEG', quality=95, optimize=True)
        print(f"✓ บันทึก {output_path}")
    
    print(f"\n✨ แปลงเสร็จแล้ว! ได้ {len(images)} รูป")
    
except Exception as e:
    print(f"❌ เกิดข้อผิดพลาด: {e}")
    print("\nหากเจอ error ให้ลองติดตั้ง poppler:")
    print("  macOS: brew install poppler")
