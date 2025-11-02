# 🚀 Galactic Duel: Space Shooter with AI Wingman!

> **"Dua roket. Satu misi. Selamatkan galaksi — atau hancur bersamanya."**

**Galactic Duel** adalah game tembak-menembak luar angkasa yang dibangun dengan **Python dan Pygame**, menghadirkan pengalaman klasik dengan sentuhan modern: kamu tidak bertarung sendirian! Di samping roket utamamu, ada **AI wingman cerdas** yang secara otomatis mengikuti, menargetkan, dan menembak musuh terdekat—memberimu keunggulan taktis di medan antariksa!

Hancurkan UFO, hindari asteroid mematikan, dan raih kemenangan sebelum musuh menghancurkanmu!

---

## 🌌 Fitur Utama

- **🎮 Dua Karakter dalam Satu Layar**  
  - Roket utama dikendalikan pemain (← → + SPASI)  
  - Roket kedua dikendalikan **AI otomatis**: mencari, mengikuti, dan menembak musuh terdekat

- **🛸 Musuh Dinamis & Bahaya Asteroid**  
  - UFO jatuh dengan kecepatan acak  
  - Asteroid tak bisa dihancurkan—hindari atau kalah!

- **🎯 Tujuan Jelas**  
  - ✅ **Menang**: Hancurkan **10 UFO**  
  - ❌ **Kalah jika**:  
    - 3 musuh lolos melewati layar  
    - Roket utama atau AI tertabrak UFO/asteroid

- **🎧 Suasana Imersif**  
  - Musik latar luar angkasa (`space.ogg`)  
  - Efek suara tembakan (`fire.ogg`)  
  - *Fallback otomatis jika file suara tidak ditemukan*

- **⚡ Ringan & Edukatif**  
  - Cocok untuk belajar dasar game development dengan Pygame  
  - Kode bersih, modular, dan mudah dimodifikasi

---

## 🎮 Cara Bermain

1. Gerakkan roket utama dengan tombol **panah kiri/kanan (← →)**
2. Tembak musuh dengan tombol **SPASI**
3. Roket kedua **otomatis bertarung** di sisimu—tidak perlu dikendalikan!
4. Capai **skor 10** sebelum kehabisan nyawa!

---

## ▶️ Jalankan Game

Pastikan kamu memiliki **Python** dan **Pygame** terinstal:

```bash
pip install pygame
```
## Lalu jalankan game:
```bash
python shooter_game.py
```
⚠️ Catatan Aset:
File gambar dan suara harus berada di folder yang sama dengan skrip: 

Gambar: galaxy.jpg, rocket.png, ufo.png, asteroid.png, bullet.png
Audio: space.ogg, fire.ogg
(Preferensi: gunakan format JPG untuk gambar dan hindari ekstensi .mp3 untuk audio)

📄 Lisensi
Proyek ini dilisensikan di bawah MIT License.
📝 Lihat teks lengkap lisensi di:
👉 https://github.com/username/galactic-duel/blob/main/LICENSE

Dibuat dengan ❤️ untuk pecinta game retro, pemula Python, dan eksperimen AI sederhana.
Siap menjadi legenda antariksa? Mainkan sekarang! 🌠

