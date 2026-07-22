# 🚁 gOWLsystem - Viticoltura di precisione e pipeline VRA

**gOWLsystem** è una pipeline automatizzata in Python progettata per l'elaborazione di dati fotogrammetrici da drone e la generazione di mappe di prescrizione a rateo variabile (VRA) per la viticoltura di precisione.

---

## 💡 Cos' è? A cosa serve?

Il sistema automatizza il flusso di lavoro che va dall'ortofoto multispettrale/RGB generata da drone alla mappa finale caricabile sui computer di bordo delle macchine agricole (trattori, spandiconcime, atomizzatori).

---

## ⚙️ Architettura del Sistema (5 Step)

1. **Pre-elaborazione e allineamento**
   * Importazione di ortofoti GeoTIFF e calcolo degli indici di vigore (NDVI, NDRE, ecc.).
2. **Filtraggio e riduzione del rumore**
   * Pulizia del dato per isolare la chioma della vite dal suolo e dall'interfilare inerbito.
3. **Zonizzazione Dinamica**
   * Clustering e segmentazione dell'appezzamento in zone omogenee di vigore.
4. **Generazione mappe VRA**
   * Calcolo delle dosi di apporto e conversione nei formati vettoriali standard (Shapefile / ISOXML).
5. **Controllo qualità ed esportazione**
   * Validazione geometrica, verifica dei metadati e generazione del report sintetico.

---

## 🛠️ Stack Tecnologico
* **Linguaggio:** Python 3.x
* **Librerie Geospatiali:** `rasterio`, `numpy`, `geopandas`, `shapely`
* **GIS Integrati:** QGIS / QField, WebODM
* **Formati Output:** GeoTIFF, ESRI Shapefile, ISOXML

---

## 📩 Contatti & Collaborazioni
Sei un agronomo, una cantina o un terzista interessato a testare il sistema o a integrare il flusso nei tuoi vigneti?

* **LinkedIn:** https://www.linkedin.com/in/giorgio-lombardo-796751362
* **Zona operativa:** Lombardia e limitrofi

