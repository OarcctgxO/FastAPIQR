from qrcode import QRCode
from fastapi import HTTPException, status
from qrcode.image.pure import PyPNGImage

from functools import lru_cache
from io import BytesIO

import settings


@lru_cache(maxsize=settings.cache_size)
def make_qr_code(text:str = ''):
    """
    Основная CPU-bound функция, генерирующая QR-код. Принимает текст в виде str-строки и возвращает байтовую строку с png файлом.
    """
    try:
        code = QRCode(
            version=1,
            error_correction=settings.correction,
            box_size=settings.picture_resolution_ratio,
            border=settings.border_size,
            image_factory=PyPNGImage
        )
        
        code.add_data(text)
        code.make(fit=True)
        img = code.make_image()
        
        buf = BytesIO()
        img.save(buf)
        return buf.getvalue()
    
    except Exception as er:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Не удалось создать QR-код: {str(er)}"
        )