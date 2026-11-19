import os
import tempfile
from contextlib import contextmanager


def get_error_message(error):
    error_text = str(error).lower()

    if "429" in error_text or "resource_exhausted" in error_text:
        return "API kullanım limitine ulaşıldı. Lütfen biraz bekleyip tekrar deneyin."

    elif "401" in error_text or "unauthorized" in error_text:
        return "API kimlik doğrulaması başarısız. API anahtarınızı kontrol edin."

    elif "403" in error_text or "permission denied" in error_text:
        return "Bu işlem için API erişim izniniz bulunmuyor."

    elif "503" in error_text or "unavailable" in error_text:
        return "AI servisi şu anda yoğun. Biraz sonra tekrar deneyin."

    elif "connection" in error_text or "timeout" in error_text:
        return "Bağlantı kurulamadı. İnternetinizi kontrol edip tekrar deneyin."

    else:
        return "Beklenmeyen bir hata oluştu. Lütfen tekrar deneyin."


@contextmanager
def temporary_audio_file(audio_bytes, suffix):
    temp_audio_path = None

    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:
            temp_file.write(audio_bytes)
            temp_audio_path = temp_file.name

        yield temp_audio_path

    finally:
        if temp_audio_path and os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)