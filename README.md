# Assignment 1: OpenAI SDK Pipeline & Context Injection

Repository ini berisi penyelesaian tugas Assignment 1 untuk mengimplementasikan fitur dasar Large Language Model (LLM) menggunakan OpenAI SDK di Python. Studi kasus yang digunakan diadaptasi dari skenario operasional **Gerakan Baik Berdampak (GBB)**.

## 📂 Isi Repository

- **Case 1: Simple Chatbot (`01_chatbot.py`)**
  Chatbot interaktif berbasis terminal bernama "Minbe". Program ini menerapkan teknik *Context Injection* (System Prompt) yang berisi informasi mengenai profil, program beswan, dan infrastruktur GBB. Chatbot ini juga dilengkapi dengan *looping memory* sehingga dapat mengingat konteks percakapan sebelumnya.

- **Case 2: 3-Step Data Pipeline (`02_pipeline.py`)**
  Simulasi alur pemrosesan data otomatis (*Multiple Shot*) untuk menangani pesan konfirmasi donatur. Pipeline ini terdiri dari 3 tahapan:
  1. **Get Raw Data:** Menerima teks pesan konfirmasi donasi yang tidak beraturan dari lapangan/WhatsApp.
  2. **Summarize:** Menggunakan *Standard Completion* untuk merangkum pesan mentah menjadi laporan operasional formal.
  3. **Structured Output:** Menggunakan fitur `.parse()` dan Pydantic untuk mengekstrak laporan tersebut menjadi format JSON/Dictionary yang terstruktur dan siap dimasukkan ke dalam *database* donatur.

## 🚀 Cara Menjalankan

1. Clone repository ini.
2. Buat file `.env` di *root directory* dan tambahkan *credentials* API:
   ```env
   SUMOPOD_BASE_URL=url_api_kamu
   SUMOPOD_API_KEY=key_api_kamu
3. Jalankan script melalui terminal:
uv add openai pydantic python-dotenv

python 01_chatbot.py
# atau
python 02_pipeline.py