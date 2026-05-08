import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()
SUMOPOD_BASE_URL= os.getenv("SUMOPOD_BASE_URL")
SUMOPOD_API_KEY= os.getenv("SUMOPOD_API_KEY")

client = OpenAI(base_url=SUMOPOD_BASE_URL,api_key=SUMOPOD_API_KEY)

# pydantic model
class DonationData(BaseModel):
    nama_donatur: str
    nominal: int
    tanggal_transfer: str
    metode_pembayaran: str
    peruntukan_dana: str


def step1_get_raw_donation() -> str:
    """Simulasi menerima pesan konfirmasi donasi yang tidak beraturan."""
    print("[Step 1] Menerima pesan konfirmasi donasi mentah...")
    
    raw_message = """
    Halo GBB, saya Arin tadi pagi jam 9 sudah transfer ya 
    buat bantu program Beswan. Saya kirim 1.000.000 lewat Bank Mandiri. 
    Semoga berkah dan bermanfaat buat adik-adik beasiswa.
    """
    return raw_message

def step2_summarize_donation(raw_data: str) -> str:
    """Merangkum pesan konfirmasi menjadi laporan internal yang rapi."""
    print("[Step 2] Merangkum konfirmasi donasi menjadi laporan formal...")
    
    completion = client.chat.completions.create(
        model="kimi-k2.6",
        messages=[
            {
                "role": "system", 
                "content": "Anda adalah Admin Admin Database Gerakan Baik Berdampak. Ubah pesan konfirmasi donatur menjadi laporan ringkas dan formal."
            },
            {
                "role": "user", 
                "content": f"Rangkum konfirmasi ini:\n{raw_data}"
            }
        ],
        temperature=0.3
    )
    
    summary = completion.choices[0].message.content or ""
    return summary

def step3_extract_to_database(summary_text: str) -> DonationData:
    """Mengekstrak teks menjadi objek data terstruktur untuk input database."""
    print("[Step 3] Mengekstrak data ke format terstruktur (JSON)...")
    
    completion = client.chat.completions.parse(
        model="kimi-k2.6",
        messages=[
            {
                "role": "system", 
                "content": "Ekstrak detail donasi. Ubah nominal menjadi angka integer saja (tanpa titik/Rp). Jika peruntukan dana menyebut Beswan atau Beasiswa, kategorikan sebagai 'Program Beasiswa'."
            },
            {
                "role": "user", 
                "content": summary_text
            }
        ],
        response_format=DonationData,
        temperature=0.1
    )
    
    parsed_data = completion.choices[0].message.parsed
    assert parsed_data is not None, "Gagal memproses data donasi!"
    
    return parsed_data

if __name__ == "__main__":
    print("=== PIPELINE DONASI GERAKAN BAIK BERDAMPAK ===\n")
    
    # Step 1
    raw_msg = step1_get_raw_donation()
    print(f"Pesan Mentah:\n{raw_msg.strip()}\n")
    
    # Step 2
    formal_report = step2_summarize_donation(raw_msg)
    print(f"Laporan Formal:\n{formal_report}\n")
    
    # Step 3
    final_data = step3_extract_to_database(formal_report)
    print("Data Siap Masuk Database:")
    print(final_data.model_dump())
    
    print("\n=== PIPELINE SELESAI ===")