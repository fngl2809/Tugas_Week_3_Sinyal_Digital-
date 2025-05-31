import soundfile as sf
import numpy as np

# Load file audio
input_file = 'data\goatsound.wav'  # ganti dengan nama file kamu
data, samplerate = sf.read(input_file)

# Balik urutan data
reversed_data = np.flipud(data)

# Simpan sebagai file baru
output_file = 'data/reversed_output.wav'
sf.write(output_file, reversed_data, samplerate)

print(f"File berhasil disimpan: {output_file}")
