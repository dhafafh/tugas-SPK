#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
K-Nearest Neighbor Sistem Rekomendasi Kopi Indonesia
untuk Penderita Gangguan Lambung
"""

import pandas as pd
import numpy as np
import math

class KNearestNeighbor:
    """Implementasi K-Nearest Neighbor dari scratch"""
    
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None
    
    def fit(self, X_train, y_train):
        """Menyimpan data training (Lazy Learning)"""
        self.X_train = X_train
        self.y_train = y_train
    
    def euclidean_distance(self, point1, point2):
        """Hitung jarak Euclidean"""
        sum_sq = sum((p1 - p2)**2 for p1, p2 in zip(point1, point2))
        return math.sqrt(sum_sq)
    
    def predict_single(self, x_test):
        """Prediksi untuk satu data"""
        # Hitung jarak ke semua training data
        distances = []
        for i, x_train in enumerate(self.X_train):
            dist = self.euclidean_distance(x_test, x_train)
            distances.append((dist, self.y_train[i], i))
        
        # Sort by distance
        distances.sort(key=lambda x: x[0])
        
        # Ambil k nearest
        k_nearest = distances[:self.k]
        
        # Voting
        votes = {}
        for _, label, _ in k_nearest:
            votes[label] = votes.get(label, 0) + 1
        
        predicted = max(votes, key=votes.get)
        return predicted, k_nearest
    
    def predict(self, X_test):
        """Prediksi untuk multiple data"""
        predictions = []
        for x_test in X_test:
            pred, _ = self.predict_single(x_test)
            predictions.append(pred)
        return np.array(predictions)


if __name__ == "__main__":
    print("\nK-Nearest Neighbor KOpi Indonesia")
    print("Program siap digunakan atau diimport ke Jupyter Notebook")
    print("\nUsage:")
    print("  from knn_kopi import KNearestNeighbor")
    print("  knn = KNearestNeighbor(k=3)")
    print("  knn.fit(X_train, y_train)")
    print("  predictions = knn.predict(X_test)")
    print("\n")
