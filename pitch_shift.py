import librosa
import soundfile as sf

# 1. Load file audio (pastikan format .wav, .mp3, dll)
input_path = 'data\goatsound.wav'  # ganti dengan filemu
y, sr = librosa.load(input_path)

# 2. Pitch shift (jumlah semitone)
# +12 = 1 oktaf naik (chipmunk), -12 = 1 oktaf turun (deep voice)
pitch_up = librosa.effects.pitch_shift(y, sr, n_steps=12)     # Naik 12 semitone
pitch_down = librosa.effects.pitch_shift(y, sr, n_steps=-8)   # Turun 8 semitone

# 3. Simpan hasilnya
sf.write('data/suara_chipmunk.wav', pitch_up, sr)
sf.write('data/suara_berat.wav', pitch_down, sr)

print("✅ Pitch shifting selesai! Cek file hasil di folder 'data'")
