from qrcode import QRCode
import qrcode.constants
from qrcode.image.pure import PyPNGImage

from functools import lru_cache
from io import BytesIO


@lru_cache(maxsize=255)
def make_qr_code(text:str = ''):
    """
    Основная CPU-bound функция, генерирующая QR-код. Принимает текст в виде str-строки и возвращает байтовую строку с png файлом.
    """
    
    code = QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=0,
        image_factory=PyPNGImage
    )
    
    code.add_data(text)
    code.make(fit=True)
    img = code.make_image()
    
    buf = BytesIO()
    img.save(buf)
    return buf.getvalue()