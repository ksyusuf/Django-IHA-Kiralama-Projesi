# context_processors.py

from datetime import datetime


def footer_context(request):
    # her sayfada bulunan footer'a ilgili tarihi göndermek için oluşturulmuş fonksiyon.
    # settings.py dosyasına TEMPLATES değişkenine bu fonksiyonun vardlığı bildirilmiştir.
    # bu bildirim sayesinde herhangi bir html sayfasına current_year değişkenine erişilebilir.
    current_year = datetime.now().year
    return {'current_year': current_year}
