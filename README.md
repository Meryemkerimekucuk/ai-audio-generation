# 🎙️ Audio AI Studio

Python ve Streamlit kullanılarak geliştirilen yapay zekâ destekli bir ses uygulamasıdır. Ses tanıma, sesli komutlarla etkileşim, ses çevirisi ve metni sese dönüştürme özelliklerini tek bir uygulama altında bir araya getirir.

Proje kapsamında farklı AI servisleri ve Python kütüphaneleri kullanılarak ses işleme uygulamalarının geliştirilmesi hedeflenmiştir.

## ✨ Özellikler

### 🎧 Speech to Text (Sesten Metne)
- MP3, WAV ve M4A formatlarında ses dosyası yükleme.
- AssemblyAI kullanarak sesleri metne dönüştürme.
- Oluşturulan transkripsiyonu görüntüleme.
- Transkripsiyonu TXT dosyası olarak indirme.

### 🎤 Voice Commands (Sesli Komutlar)
- Uygulama üzerinden mikrofonla ses kaydı yapma.
- AssemblyAI ile konuşmayı metne dönüştürme.
- Google Gemini ile sesli komutları analiz etme.
- Kullanıcının komutuna uygun AI yanıtları oluşturma.

### 🌍 Audio Translator (Ses Çevirisi)
- Ses dosyası yükleme ve transkripsiyon oluşturma.
- Google Gemini kullanarak metni seçilen dile çevirme.
- Orijinal metni ve çeviriyi görüntüleme.
- Çeviri sonucunu TXT dosyası olarak indirme.

### 🔊 Text to Speech (Metinden Sese)
- Girilen metni sese dönüştürme.
- Sistemde bulunan ses seçenekleri arasından seçim yapma.
- Konuşma hızını ayarlama.
- pyttsx3 kullanarak yerel ortamda ses üretme.

## 🛠️ Kullanılan Teknolojiler

- **Python:** Uygulama geliştirme dili
- **Streamlit:** Web uygulaması arayüzü
- **AssemblyAI API:** Ses tanıma ve transkripsiyon
- **Google Gemini API:** Metin üretimi, sesli komut analizi ve çeviri
- **pyttsx3:** Metinden sese dönüştürme
- **python-dotenv:** Ortam değişkenlerinin yönetimi

## 📁 Proje Yapısı

```text
audio-ai-studio/
│
├── app.py
├── config.py
├── utils.py
├── requirements.txt
├── .env
├── .gitignore
│
└── features/
    ├── __init__.py
    ├── speech_to_text.py
    ├── voice_commands.py
    ├── audio_translator.py
    └── text_to_speech.py
```

## 🚀 Kurulum

### 1. Repoyu klonlayın

```bash
git clone REPOSITORY_URL
```

Proje klasörüne geçin:

```bash
cd audio-ai-studio
```

### 2. Sanal ortam oluşturun

```bash
python -m venv .venv
```

Sanal ortamı aktifleştirin.

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Bağımlılıkları yükleyin

```bash
pip install -r requirements.txt
```

### 4. API anahtarlarını yapılandırın

Proje ana dizininde `.env` adında bir dosya oluşturun ve API anahtarlarınızı ekleyin:

```env
ASSEMBLYAI_API_KEY=assemblyai_api_keyiniz
GEMINI_API_KEY=gemini_api_keyiniz
```

### 5. Uygulamayı çalıştırın

```bash
streamlit run app.py
```

Uygulama tarayıcınızda açılacaktır.

## 🔑 Ortam Değişkenleri

| Değişken | Açıklama |
|---|---|
| `ASSEMBLYAI_API_KEY` | Ses transkripsiyonu için AssemblyAI API anahtarı |
| `GEMINI_API_KEY` | Google Gemini API anahtarı |

> API anahtarlarınızı içeren `.env` dosyasını GitHub'a yüklemeyin.

## 📌 Kullanım

1. Uygulamayı çalıştırın.
2. Kullanmak istediğiniz ses aracını seçin.
3. Seçilen özelliğe göre ses dosyası yükleyin veya mikrofonla kayıt yapın.
4. Sesinizi ilgili AI servisiyle işleyin.
5. Oluşturulan sonuçları görüntüleyin ve mevcut indirme seçeneklerini kullanın.

## 🎯 Projenin Amacı

Bu proje ile Python kullanarak AI servislerinin uygulamalara entegrasyonu, ses verilerinin işlenmesi, modüler uygulama yapısı oluşturulması ve yapay zekâ destekli ses işleme araçlarının geliştirilmesi üzerine pratik kazanılması amaçlanmıştır.

---

*Python ve yapay zekâ teknolojilerini öğrenme ve uygulama sürecinde geliştirilmiştir.*
