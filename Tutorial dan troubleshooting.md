# Teman Makan Tangsel - AI Culinary Chatbot

Proyek Tugas Besar Mata Kuliah Kecerdasan Buatan
Institut Teknologi tangerang selatan

## Kelompok 13

1. Panji Arya Soma (1003240008)
2. Lintang Arif Setianda (1003240023)
3. Bayu Dwi H. (1003240004)

## Daftar Isi

1. [Deskripsi Proyek](#deskripsi-proyek)
2. [Spesifikasi Sistem](#spesifikasi-sistem)
3. [Struktur Proyek](#struktur-proyek)
4. [Panduan Instalasi](#panduan-instalasi)
5. [Cara Menjalankan](#cara-menjalankan)
6. [Troubleshooting](#troubleshooting)
7. [Fitur Sistem](#fitur-sistem)

## Deskripsi Proyek

Teman Makan Tangsel adalah sistem chatbot berbasis kecerdasan buatan yang dirancang untuk memberikan rekomendasi kuliner di wilayah Tangerang Selatan. Sistem ini mengintegrasikan basis data komprehensif yang mencakup 276 restoran dengan teknologi pemrosesan bahasa alami menggunakan model Gemma 3 4B melalui platform Ollama. Implementasi menggunakan pendekatan local-first computing untuk menjamin privasi data pengguna dan responsivitas sistem tanpa ketergantungan pada layanan cloud.

### Tujuan Proyek

1. Mengimplementasikan sistem rekomendasi kuliner berbasis conversational AI
2. Memanfaatkan model bahasa besar (LLM) dalam konteks lokal tanpa ketergantungan cloud
3. Mengembangkan antarmuka interaktif yang intuitif untuk pengguna umum
4. Mengevaluasi efektivitas model Gemma 3 4B dalam domain rekomendasi kuliner

### Teknologi yang Digunakan

- Bahasa Pemrograman: Python 3.10 atau lebih tinggi
- Model AI: Gemma 3 4B (parameter: 4 miliar)
- Runtime Model: Ollama
- Framework Web: Streamlit
- Format Database: JSON
- Library Tambahan: Pandas untuk manipulasi data

## Spesifikasi Sistem

### Persyaratan Minimum Hardware

- Processor: Intel Core i5 generasi ke-10 atau AMD Ryzen 5 series atau lebih tinggi
- RAM: Minimal 8GB (disarankan 16GB untuk performa optimal)
- Ruang Penyimpanan: Minimal 5GB kosong untuk model dan dependencies
- GPU: RTX Series atau GPU lain dengan Vram 4gb. bisa menggunakan CPU namun wajib ubah ke Gemma3:270m parameter 
serta mengubah pull ollama di script python dengan model yang ada

### Persyaratan Software

- Sistem Operasi: 
  - Windows 10/11 (64-bit)
  - Ubuntu 20.04 LTS atau lebih baru
  - MacOS 12 (Monterey) atau lebih baru
- Python: Versi 3.10, 3.11, atau 3.12
- Koneksi Internet: Diperlukan untuk instalasi awal, tidak diperlukan saat runtime

### Spesifikasi Model dan Database

- Model Gemma 3 4B: Ukuran sekitar 3.3GB
- Database Restoran: 276 entri dalam format JSON (124.3 KB untuk chatbot8.json, 182.0 KB untuk chatbot9.json)
- Total Ruang Aplikasi: Sekitar 50-100 MB (termasuk dependencies Python)

## Struktur Proyek
```
uas_bot_kuliner/
├── venv/                      # Virtual environment Python (7 items)
│   ├── bin/                   # Executables (Linux/Mac)
│   ├── Scripts/               # Executables (Windows)
│   ├── Lib/                   # Library Python
│   ├── Include/               # Header files
│   └── pyvenv.cfg             # Konfigurasi virtual environment
├── app.py                     # File utama aplikasi Streamlit (7.1 kB)
├── chatbot8.json              # Database restoran versi 8 (124.3 kB)
├── chatbot9.json              # Database restoran versi 9 (182.0 kB)
└── README.md                  # Dokumentasi proyek (file ini)
```

### Penjelasan File Utama

- app.py: File Python utama yang berisi logika aplikasi chatbot, integrasi Streamlit UI, dan koneksi ke Ollama
- chatbot8.json: Database restoran dalam format JSON versi 8
- chatbot9.json: Database restoran dalam format JSON versi 9 (versi terbaru dengan data lebih lengkap)
- venv/: Folder virtual environment yang mengisolasi dependencies proyek

## Panduan Instalasi

### Langkah 1: Instalasi Python

#### Windows

1. Kunjungi situs resmi Python di https://www.python.org/downloads/
2. Unduh installer Python 3.10 atau versi lebih baru untuk Windows
3. Jalankan file installer (.exe) yang telah diunduh
4. PENTING: Centang opsi "Add Python to PATH" pada halaman pertama installer
5. Pilih "Install Now" untuk instalasi standar
6. Tunggu hingga proses instalasi selesai
7. Klik "Close" setelah instalasi berhasil
8. Verifikasi instalasi dengan membuka Command Prompt (tekan Win+R, ketik cmd, Enter)
9. Ketik perintah berikut dan tekan Enter:
```bash
   python --version
```
10. Jika muncul versi Python (contoh: Python 3.10.0), instalasi berhasil

#### Ubuntu/Linux

1. Buka terminal (tekan Ctrl+Alt+T)
2. Update repository package terlebih dahulu:
```bash
   sudo apt update
```
3. Install Python 3.10 dan tools pendukung:
```bash
   sudo apt install python3.10 python3.10-venv python3-pip -y
```
4. Tunggu hingga instalasi selesai
5. Verifikasi instalasi dengan mengetik:
```bash
   python3 --version
```
6. Pastikan muncul versi Python 3.10 atau lebih tinggi

#### MacOS

1. Buka Terminal (Applications > Utilities > Terminal)
2. Install Homebrew jika belum terinstall dengan menjalankan:
```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Tunggu instalasi Homebrew selesai
4. Install Python menggunakan Homebrew:
```bash
   brew install python@3.10
```
5. Verifikasi instalasi:
```bash
   python3 --version
```
6. Pastikan versi yang muncul adalah 3.10 atau lebih tinggi

### Langkah 2: Instalasi Ollama

#### Windows

1. Buka browser dan kunjungi https://ollama.com/download
2. Klik tombol "Download for Windows"
3. Tunggu hingga file installer (.exe) selesai diunduh
4. Buka folder Downloads dan jalankan file OllamaSetup.exe
5. Ikuti wizard instalasi:
   - Klik "Next" pada welcome screen
   - Pilih lokasi instalasi (default: C:\Program Files\Ollama)
   - Klik "Install"
6. Tunggu hingga instalasi selesai
7. Klik "Finish" untuk menyelesaikan instalasi
8. Ollama akan berjalan otomatis di background (cek system tray)
9. Verifikasi instalasi dengan membuka Command Prompt dan ketik:
```bash
   ollama --version
```
10. Jika muncul versi Ollama, instalasi berhasil

#### Ubuntu/Linux

1. Buka terminal
2. Jalankan script instalasi otomatis dari Ollama:
```bash
   curl -fsSL https://ollama.com/install.sh | sh
```
3. Script akan otomatis:
   - Mendeteksi sistem operasi Anda
   - Mengunduh binary Ollama
   - Menginstall di lokasi yang sesuai
   - Mengatur systemd service
4. Tunggu hingga proses selesai (biasanya 1-2 menit)
5. Verifikasi instalasi:
```bash
   ollama --version
```
6. Start Ollama service:
```bash
   sudo systemctl start ollama
```
7. Atur agar Ollama berjalan otomatis saat boot:
```bash
   sudo systemctl enable ollama
```

#### MacOS

1. Buka browser dan kunjungi https://ollama.com/download
2. Klik "Download for Mac"
3. Tunggu file .dmg selesai diunduh
4. Buka file Ollama.dmg dari folder Downloads
5. Drag icon Ollama ke folder Applications
6. Buka Finder, masuk ke Applications
7. Klik kanan pada Ollama dan pilih "Open"
8. Klik "Open" pada dialog keamanan yang muncul
9. Ollama akan berjalan di menu bar (icon di atas)
10. Buka Terminal dan verifikasi:
```bash
    ollama --version
```

### Langkah 3: Unduh Model Gemma 3 4B

1. Buka terminal atau Command Prompt
2. Pastikan Ollama sudah berjalan (cek system tray/menu bar)
3. Jalankan perintah untuk mengunduh model Gemma 3 4B:
```bash
   ollama pull gemma3:4b
```
4. Proses download akan dimulai dengan tampilan seperti:
```
   pulling manifest
   pulling 8fa9b9f2a6a0... 100% ████████████ 2.5 GB
   pulling 8ab4849b038c... 100% ████████████ 573 B
   pulling 966de95ca8a6... 100% ████████████ 108 B
   pulling fcc5a6bb8e9e... 100% ████████████ 485 B
   verifying sha256 digest
   writing manifest
   success
```
5. Proses ini memerlukan:
   - Koneksi internet yang stabil
   - Waktu sekitar 5-15 menit tergantung kecepatan internet
   - Ruang kosong minimal 3GB
6. Setelah selesai, verifikasi model telah terunduh:
```bash
   ollama list
```
7. Anda akan melihat output seperti:
```
   NAME            ID              SIZE    MODIFIED
   gemma3:4b       abc123def456    2.5 GB  2 minutes ago
```
8. Test model dengan perintah:
```bash
   ollama run gemma3:4b "Hello, how are you?"
```
9. Jika model merespons dengan teks, instalasi berhasil
10. Ketik /bye untuk keluar dari mode chat Ollama


#### Download Manual

1. Download file ZIP proyek dari repository
2. Extract file ZIP ke lokasi yang diinginkan, misalnya:
   - Windows: C:\Users\NamaUser\Documents\uas_bot_kuliner
   - Linux: /home/namauser/Documents/uas_bot_kuliner
   - MacOS: /Users/namauser/Documents/uas_bot_kuliner
3. Buka terminal/Command Prompt
4. Navigasi ke folder proyek:
```bash
   cd path/to/uas_bot_kuliner
```

### Langkah 4: Membuat Virtual Environment

Virtual environment digunakan untuk mengisolasi dependencies proyek agar tidak bertabrakan dengan package Python global.

#### Windows

1. Buka Command Prompt atau PowerShell
2. Navigasi ke folder proyek:
```bash
   cd C:\Users\NamaUser\Documents\uas_bot_kuliner
```
3. Buat virtual environment:
```bash
   python -m venv venv
```
4. Tunggu hingga proses selesai (akan membuat folder venv)
5. Aktivasi virtual environment:
```bash
   .\venv\Scripts\activate
```
6. Jika muncul error "cannot be loaded because running scripts is disabled":
```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
7. Ulangi aktivasi:
```bash
   .\venv\Scripts\activate
```
8. Jika berhasil, Anda akan melihat (venv) di awal baris prompt:
```
   (venv) C:\Users\NamaUser\Documents\uas_bot_kuliner>
```

#### Ubuntu/Linux

1. Buka terminal
2. Navigasi ke folder proyek:
```bash
   cd /home/namauser/Documents/uas_bot_kuliner
```
3. Buat virtual environment:
```bash
   python3 -m venv venv
```
4. Aktivasi virtual environment:
```bash
   source venv/bin/activate
```
5. Jika berhasil, prompt akan berubah menjadi:
```
   (venv) namauser@hostname:~/Documents/uas_bot_kuliner$
```

#### MacOS

1. Buka Terminal
2. Navigasi ke folder proyek:
```bash
   cd /Users/namauser/Documents/uas_bot_kuliner
```
3. Buat virtual environment:
```bash
   python3 -m venv venv
```
4. Aktivasi virtual environment:
```bash
   source venv/bin/activate
```
5. Prompt akan berubah menjadi:
```
   (venv) namauser@MacBook-Air uas_bot_kuliner %
```

### Langkah 6: Instalasi Dependencies Python

Dengan virtual environment aktif (pastikan ada tanda (venv) di prompt):

1. Upgrade pip ke versi terbaru:
```bash
   pip install --upgrade pip
```

2. Install dependencies utama:
```bash
   pip install streamlit ollama pandas
```

3. Atau jika tersedia file requirements.txt:
```bash
   pip install -r requirements.txt
```

4. Tunggu hingga instalasi selesai, Anda akan melihat output seperti:
```
   Successfully installed streamlit-1.29.0 ollama-0.1.5 pandas-2.1.4 ...
```

5. Verifikasi instalasi dengan melihat daftar package:
```bash
   pip list
```

6. Pastikan package berikut terinstall:
   - streamlit (versi 1.29.0 atau lebih baru)
   - ollama (versi 0.1.0 atau lebih baru)
   - pandas (versi 2.0.0 atau lebih baru)

7. Anda juga bisa cek versi spesifik:
```bash
   streamlit --version
```

### Langkah 7: Verifikasi Struktur Proyek

Pastikan struktur folder dan file sudah benar:

1. Cek isi folder dengan perintah:
   - Windows: `dir`
   - Linux/Mac: `ls -la`

2. Pastikan file-file berikut ada:
   - app.py (file utama aplikasi)
   - chatbot8.json atau chatbot9.json (database restoran)
   - venv/ (folder virtual environment)

3. Jika file database (.json) tidak ada:
   - Pastikan Anda sudah mengunduh/menyalin file database
   - Letakkan di folder yang sama dengan app.py

4. Periksa isi file app.py (pastikan tidak corrupt):
   - Windows: `type app.py`
   - Linux/Mac: `cat app.py`

5. Verifikasi file JSON valid:
```bash
   python -m json.tool chatbot9.json
```
   Jika tidak ada error, file JSON valid.

## Cara Menjalankan

### Menjalankan Aplikasi Pertama Kali

1. Pastikan Ollama service sedang berjalan:
   - Windows: Cek system tray, ikon Ollama harus ada
   - Linux: `sudo systemctl status ollama`
   - MacOS: Cek menu bar untuk ikon Ollama

2. Jika Ollama belum berjalan:
   - Windows: Buka Ollama dari Start Menu
   - Linux: `sudo systemctl start ollama`
   - MacOS: Buka Ollama dari Applications

3. Buka terminal/Command Prompt

4. Navigasi ke folder proyek:
```bash
   cd path/to/uas_bot_kuliner
```

5. Aktivasi virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

6. Pastikan (venv) muncul di prompt

7. Jalankan aplikasi Streamlit:
```bash
   streamlit run app.py
```

8. Tunggu beberapa detik, Anda akan melihat output:
```
   You can now view your Streamlit app in your browser.

   Local URL: http://localhost:8501
   Network URL: http://192.168.x.x:8501
```

9. Browser akan otomatis terbuka menuju http://localhost:8501

10. Jika browser tidak terbuka otomatis:
    - Buka browser manual (Chrome, Firefox, Edge, Safari)
    - Ketik di address bar: http://localhost:8501
    - Tekan Enter

11. Aplikasi chatbot akan muncul di browser

12. Tunggu beberapa detik untuk loading model (first run biasanya lebih lama)

### Menggunakan Aplikasi

1. Pada interface chatbot, Anda akan melihat:
   - Judul aplikasi
   - Area chat history
   - Input box di bagian bawah

2. Ketik pertanyaan atau request di input box, contoh:
   - "Rekomendasikan restoran Jepang di BSD"
   - "Cari tempat makan untuk keluarga budget 100rb"
   - "Resto romantis untuk dinner"

3. Tekan Enter atau klik tombol kirim

4. Chatbot akan memproses request menggunakan model Gemma 3 4B

5. Response akan muncul dalam beberapa detik

6. Anda bisa terus bertanya dalam satu sesi chat

### Menghentikan Aplikasi

1. Untuk stop aplikasi Streamlit:
   - Kembali ke terminal/Command Prompt
   - Tekan Ctrl+C
   - Konfirmasi dengan Y jika diminta

2. Deactivate virtual environment:
```bash
   deactivate
```

3. Prompt akan kembali normal tanpa (venv)

4. Anda bisa menutup terminal

### Menjalankan Ulang Aplikasi (Hari Berikutnya)

Untuk menjalankan aplikasi setelah instalasi awal:

1. Pastikan Ollama berjalan (langkah 1-2 dari bagian sebelumnya)

2. Buka terminal/Command Prompt

3. Navigasi ke folder proyek:
```bash
   cd path/to/uas_bot_kuliner
```

4. Aktivasi virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

5. Jalankan aplikasi:
```bash
   streamlit run app.py
```

6. Aplikasi siap digunakan

### Mengakses dari Perangkat Lain di Jaringan yang Sama

1. Saat aplikasi berjalan, perhatikan output Network URL:
```
   Network URL: http://192.168.1.100:8501
```

2. Dari perangkat lain (HP, laptop lain) yang tersambung WiFi/jaringan yang sama:
   - Buka browser
   - Ketik Network URL tersebut
   - Aplikasi dapat diakses

3. Catatan: Firewall mungkin perlu dikonfigurasi untuk mengizinkan akses

## Troubleshooting

### 1. Ollama Tidak Ditemukan Setelah Instalasi

Gejala:
```
'ollama' is not recognized as an internal or external command
```

Solusi untuk Windows:
1. Restart Command Prompt/PowerShell
2. Jika masih error, restart komputer
3. Cek apakah Ollama terinstall di: C:\Program Files\Ollama
4. Tambahkan ke PATH manual:
   - Buka System Properties > Environment Variables
   - Edit PATH di User Variables
   - Tambahkan: C:\Program Files\Ollama
   - Klik OK dan restart Command Prompt

Solusi untuk Linux:
1. Cek service status:
```bash
   sudo systemctl status ollama
```
2. Jika inactive, start service:
```bash
   sudo systemctl start ollama
   sudo systemctl enable ollama
```
3. Verifikasi binary location:
```bash
   which ollama
```

Solusi untuk MacOS:
1. Pastikan Ollama ada di Applications
2. Jalankan Ollama dari Applications
3. Cek menu bar untuk icon Ollama
4. Restart terminal

### 2. Model Gemma 3 Tidak Bisa Diunduh

Gejala:
```
Error: unable to pull model
```

Penyebab dan Solusi:

A. Masalah Koneksi Internet:
   - Cek koneksi internet stabil
   - Test dengan: `ping google.com`
   - Gunakan WiFi yang stabil, bukan mobile data

B. Ruang Penyimpanan Tidak Cukup:
   - Cek ruang kosong:
     - Windows: File Explorer > This PC
     - Linux: `df -h`
     - MacOS: Apple menu > About This Mac > Storage
   - Pastikan minimal 5GB kosong
   - Hapus file tidak perlu jika kurang

C. Ollama Service Tidak Berjalan:
   - Pastikan Ollama running (cek system tray/menu bar)
   - Restart Ollama service

D. Download Terputus:
   - Ulangi perintah pull:
```bash
     ollama pull gemma3:4b
```
   - Ollama akan resume download otomatis

E. Port Blocked:
   - Pastikan port 11434 tidak diblokir firewall
   - Disable sementara firewall untuk test

### 3. Error Aktivasi Virtual Environment di Windows

Gejala:
```
cannot be loaded because running scripts is disabled on this system
```

Solusi:
1. Buka PowerShell sebagai Administrator
2. Jalankan perintah:
```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
3. Ketik Y untuk konfirmasi
4. Tutup PowerShell Administrator
5. Buka PowerShell/Command Prompt biasa
6. Ulangi aktivasi virtual environment:
```bash
   .\venv\Scripts\activate
```

Solusi Alternatif:
1. Gunakan Command Prompt (cmd) instead of PowerShell
2. Atau gunakan Git Bash jika sudah terinstall

### 4. Port 8501 Sudah Digunakan

Gejala:
```
OSError: [Errno 98] Address already in use
```

Penyebab:
- Streamlit lain masih berjalan
- Aplikasi lain menggunakan port 8501

Solusi A - Gunakan Port Lain:
```bash
streamlit run app.py --server.port 8502
```

Solusi B - Stop Proses yang Menggunakan Port:

Windows:
```bash
netstat -ano | findstr :8501
taskkill /PID <PID_NUMBER> /F
```

Linux/Mac:
```bash
lsof -i :8501
kill -9 <PID>
```

### 5. Module Tidak Ditemukan Setelah pip install

Gejala:
```
ModuleNotFoundError: No module named 'streamlit'
```

Penyebab:
- Virtual environment tidak aktif
- Package terinstall di Python global, bukan di venv

Solusi:
1. Pastikan virtual environment aktif (cek (venv) di prompt)
2. Jika belum aktif, aktivasi dulu:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
3. Reinstall dependencies:
```bash
   pip uninstall streamlit ollama pandas -y
   pip install streamlit ollama pandas
```
4. Verifikasi:
```bash
   pip list
```

### 6. Streamlit Tidak Bisa Terhubung ke Ollama

Gejala:
- Aplikasi loading terus tanpa response
- Error: "Connection refused"
- Chatbot tidak memberikan jawaban

Penyebab dan Solusi:

A. Ollama Service Tidak Berjalan:
   - Windows: Cek system tray, klik icon Ollama
   - Linux:
```bash
     sudo systemctl status ollama
     sudo systemctl start ollama
```
   - MacOS: Buka Ollama dari Applications

B. Model Belum Terunduh:
```bash
   ollama list
```
   Jika gemma3:4b tidak ada, download:
```bash
   ollama pull gemma3:4b
```

C. Port Ollama Berubah:
   - Default port Ollama: 11434
   - Cek di app.py, pastikan menggunakan port yang benar
   - Test koneksi:
```bash
     curl http://localhost:11434/api/tags
```

D. Firewall Memblokir:
   - Windows: Allow Ollama di Windows Defender Firewall
   - Linux: `sudo ufw allow 11434`
   - MacOS: System Preferences > Security & Privacy > Firewall

### 7. Chatbot Response Sangat Lambat

Penyebab dan Solusi:

A. Spesifikasi Hardware Kurang:
   - Gemma 3 4B memerlukan minimal 8GB RAM
   - Close aplikasi lain yang berat
   - Upgrade RAM jika memungkinkan

B. First Response Selalu Lambat:
   - Normal untuk first load (loading model ke memory)
   - Response berikutnya akan lebih cepat
   - Biarkan model tetap loaded (jangan stop aplikasi)

C. Model Belum Fully Loaded:
   - Tunggu 10-15 detik setelah start aplikasi
   - Cek Task Manager/Activity Monitor untuk CPU usage

### 8. Error Saat Membaca File JSON

Gejala:
```
JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

Penyebab dan Solusi:

A. File JSON Corrupt:
   - Download ulang file chatbot8.json atau chatbot9.json
   - Pastikan tidak corrupt saat download

B. File Tidak Ada:
   - Pastikan file .json ada di folder yang sama dengan app.py
   - Cek nama file sesuai (case-sensitive di Linux/Mac)

C. Format JSON Tidak Valid:
   - Validasi file JSON:
```bash
     python -m json.tool chatbot9.json
```
   - Jika ada error, perbaiki format JSON

### 9. Browser Tidak Otomatis Terbuka

Penyebab:
- Streamlit tidak bisa detect default browser
- Browser setting

Solusi:
1. Buka browser manual
2. Akses: http://localhost:8501
3. Atau set browser default di config Streamlit:
```bash
   streamlit config show
```
4. Edit ~/.streamlit/config.toml:
```toml
   [browser]
   serverAddress = "localhost"
   serverPort = 8501
```

### 10. Error Permission Denied

Gejala (Linux/Mac):
```
PermissionError: [Errno 13] Permission denied
```

Solusi:
1. Jangan run dengan sudo (tidak disarankan)
2. Cek permission folder proyek:
```bash
   ls -la
```
3. Ubah ownership jika perlu:
```bash
   sudo chown -R $USER:$USER uas_bot_kuliner
```
4. Atau pindahkan proyek ke folder user (~/Documents)

### 11. Streamlit Menampilkan Error "Unable to Load Model"

Solusi:
1. Verifikasi model tersedia:
```bash
   ollama list
```
2. Test model secara langsung:
```bash
   ollama run gemma3:4b "test"
```
3. Cek app.py menggunakan model name yang benar: "gemma3:4b"
4. Restart Ollama service
5. Restart aplikasi Streamlit

### 12. Virtual Environment Tidak Bisa Dibuat

Gejala:
```
Error: Command 'python -m venv venv' failed
```

Solusi untuk Windows:
```bash
python -m pip install --upgrade pip
python -m ensurepip
python -m venv venv
```

Solusi untuk Linux:
```bash
sudo apt install python3.10-venv
python3 -m venv venv
```

Solusi untuk MacOS:
```bash
pip3 install --upgrade pip
python3 -m venv venv
```

### Tips Debugging Umum

1. Selalu cek error message lengkap
2. Gunakan verbose mode untuk debugging:
```bash
   streamlit run app.py --logger.level=debug
```
3. Cek log Ollama:
   - Windows: %USERPROFILE%\.ollama\logs
   - Linux: /usr/share/ollama/logs atau journalctl -u ollama
   - MacOS: ~/Library/Logs/Ollama
4. Restart selalu solusi pertama:
   - Restart terminal
   - Restart Ollama service
   - Restart aplikasi
   - Restart komputer (last resort)
5. Update dependencies ke versi terbaru:
```bash
   pip install --upgrade streamlit ollama pandas
```


