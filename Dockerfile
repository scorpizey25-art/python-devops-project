# Gunakan image Python 3.9 sebagai base image
FROM python:3.9-slim

# Tetapkan direktori kerja di dalam container
WORKDIR /app

# Salin semua file dari direktori lokal Anda ke direktori kerja di dalam container
COPY . .

# Perintah untuk menjalankan unit test Anda
RUN python -m unittest discover

# Perintah untuk menjalankan aplikasi utama
CMD ["python", "app.py"]
