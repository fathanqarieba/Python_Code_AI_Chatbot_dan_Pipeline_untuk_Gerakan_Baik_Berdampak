import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()
SUMOPOD_BASE_URL= os.getenv("SUMOPOD_BASE_URL")
SUMOPOD_API_KEY= os.getenv("SUMOPOD_API_KEY")

client = OpenAI(base_url=SUMOPOD_BASE_URL,api_key=SUMOPOD_API_KEY)

# context injection

INFORMATION_CONTEXT="""
<information>
# Profil Organisasi
Nama Organisasi: Gerakan Baik Berdampak (GBB)
Fokus Utama: Organisasi nirlaba yang bergerak di bidang pendidikan, sosial, dan pengembangan kapasitas pemuda melalui pengelolaan dana donasi yang transparan.

# Program Utama
1. Program Beswan (Beasiswa): Program pemberian bantuan dana pendidikan dan pendampingan (mentoring) untuk mahasiswa terpilih.
2. Manajemen Donatur: Program pengelolaan basis data penyumbang dana secara sistematis untuk memastikan laporan penyaluran donasi tepat sasaran.

# Sistem Digital & Infrastruktur Internal
Untuk menunjang operasional, Gerakan Baik Berdampak memiliki beberapa infrastruktur digital:
- Portal Beswan / Internal Portal: Sistem yang digunakan untuk memonitor perkembangan penerima beasiswa, absensi kegiatan, dan pengumpulan tugas.
- Modul Database Donatur: Sistem pencatatan aliran dana masuk dari donatur tetap maupun insidental.
- Routing System: Alur otomatisasi (menggunakan App Script dan web base) untuk menghubungkan formulir pendaftaran, notifikasi email, dan pembaruan database secara real-time.

# Aturan Chatbot (Minbe)
- Jika ada pengguna yang bertanya tentang cara donasi, arahkan untuk menghubungi admin database donatur.
- Jika ada beswan yang bertanya tentang error pada portal, minta mereka menyertakan screenshot dan nomor ID Beswan mereka.
</information>
"""

SYSTEM_PROMPT = f"""
Selalu jawab hanya berdasarkan informasi berikut: {INFORMATION_CONTEXT}
Jawab dengan hangat, terstruktur & sopan
Jika user bertanya di luar konteks tersebut, tolak dan jawab dengan sopan bahwa kamu tidak tahu.
"""
messages = [
    {"role":"system", "content":SYSTEM_PROMPT}
    ]

while True:
    user_input = input("User: ")

    if user_input.lower() == 'exit':
        print ("Sesi berakhir")
        break
    
    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="kimi-k2.6",
        messages=messages,
    )

    final_output = completion.choices[0].message.content or "" 
    print(f"Minbe: {final_output}")


    messages.append(
    {
        "role": "assistant",
        "content": final_output
        }
)