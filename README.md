# K-Nearest Neighbor Sistem Rekomendasi Kopi Indonesia

## Deskripsi
Implementasi algoritma K-Nearest Neighbor dari scratch untuk merekomendasikan jenis kopi Indonesia yang aman bagi penderita gangguan lambung.

## Dataset
- Total: 50 records kopi Indonesia
- Features: Species, Origin, Region, Processing Method, Acidity
- Target: Rekomendasi (1=Aman, 0=Tidak Aman)
- Kriteria: Acidity < 7.5 & Processing Method != 'Dry'

## Model
- Algorithm: K-Nearest Neighbor (k=3)
- Distance Metric: Euclidean Distance
- Training: 80% (37 samples)
- Testing: 20% (10 samples)
