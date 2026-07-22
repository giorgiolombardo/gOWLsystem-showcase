"""
gOWLsystem - Precision Viticulture & VRA Pipeline Demo
Helper functions for vegetation index calculation and spatial processing.
"""

import numpy as np

def calculate_ndvi(nir_band: np.ndarray, red_band: np.ndarray) -> np.ndarray:
    """
    Calculates Normalized Difference Vegetation Index (NDVI) from NIR and Red bands.
    
    Parameters:
        nir_band (np.ndarray): Near-Infrared band array.
        red_band (np.ndarray): Red band array.
        
    Returns:
        np.ndarray: Calculated NDVI values scaled between -1.0 and 1.0.
    """
    # Prevent division by zero
    denominator = nir_band + red_band
    denominator[denominator == 0] = 0.0001
    
    ndvi = (nir_band - red_band) / denominator
    return np.clip(ndvi, -1.0, 1.0)


def generate_vra_zones(ndvi_array: np.ndarray, thresholds: tuple = (0.3, 0.6)) -> np.ndarray:
    """
    Categorizes NDVI raster into 3 distinct VRA management zones:
    Zone 1: Low vigor (High input requirement)
    Zone 2: Medium vigor (Standard input)
    Zone 3: High vigor (Low input requirement)
    """
    zones = np.zeros_like(ndvi_array, dtype=int)
    zones[ndvi_array < thresholds[0]] = 1
    zones[(ndvi_array >= thresholds[0]) & (ndvi_array < thresholds[1])] = 2
    zones[ndvi_array >= thresholds[1]] = 3
    
    return zones

if __name__ == "__main__":
    print("gOWLsystem VRA processing utility loaded successfully.")
  
