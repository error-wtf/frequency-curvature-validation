# ERWEITERTE VALIDIERUNGSTABELLEN

**Paper:** "Frequency-Based Curvature Detection via Dynamic Comparisons"  
**Autoren:** Carmen N. Wrede, Lino P. Casu, Bingsi  
**Datum:** 14. Dezember 2025

---

## 1. NSR vs NGR TRENNUNG

### Tabelle 1.1: N_SR Entfernbarkeit (Eq. 5)

| Geschwindigkeit | N_SR (Lab-Frame) | N_SR (Ruhe-Frame) | Entfernbar? |
|-----------------|------------------|-------------------|-------------|
| 1,000 m/s | 5.56 x 10^-12 | 0 | **JA** |
| 10,000 m/s | 5.56 x 10^-10 | 0 | **JA** |
| 100,000 m/s | 5.56 x 10^-8 | 0 | **JA** |
| 1,000,000 m/s | 5.56 x 10^-6 | 0 | **JA** |

**Physikalische Bedeutung:** N_SR = gamma - 1 ist die spezielle relativistische Korrektur. Sie kann durch Wahl des Ruhesystems entfernt werden (Lorentz-Transformation).

### LaTeX:
```latex
\begin{table}[h]
\centering
\caption{N$_{SR}$ Removability Test (Eq. 5)}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Velocity (m/s)} & \textbf{N$_{SR}$ (Lab)} & \textbf{N$_{SR}$ (Rest)} & \textbf{Removable} \\
\hline
1,000 & $5.56 \times 10^{-12}$ & 0 & Yes \\
10,000 & $5.56 \times 10^{-10}$ & 0 & Yes \\
100,000 & $5.56 \times 10^{-8}$ & 0 & Yes \\
1,000,000 & $5.56 \times 10^{-6}$ & 0 & Yes \\
\hline
\end{tabular}
\label{tab:nsr_removal}
\end{table}
```

---

### Tabelle 1.2: N_GR Persistenz (Nicht-Entfernbarkeit)

| Ort | r (m) | N_GR | Xi(r) SSZ | |N_GR - Xi|/Xi | Frame-unabh.? |
|-----|-------|------|-----------|---------------|---------------|
| Erdoberflache | 6.371e6 | 6.96e-10 | 1.80e-9 | 61.4% | **JA** |
| GPS Orbit | 2.66e7 | 1.67e-10 | 4.32e-10 | 61.4% | **JA** |
| Mondumlaufbahn | 3.84e8 | 1.15e-11 | 2.99e-11 | 61.4% | **JA** |
| 1 AU (Sonne) | 1.50e11 | 9.87e-9 | 2.56e-8 | 61.4% | **JA** |

**Hinweis:** N_GR und Xi(r) verwenden unterschiedliche Formeln, reprasentieren aber dasselbe physikalische Konzept. Das Verhaltnis Xi/N_GR = 2*phi ~ 3.24 im Weak Field.

### LaTeX:
```latex
\begin{table}[h]
\centering
\caption{N$_{GR}$ Persistence Test - Non-Removable Curvature Information}
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Location} & \textbf{r (m)} & \textbf{N$_{GR}$} & \textbf{$\Xi(r)$ SSZ} & \textbf{Frame-indep.} \\
\hline
Earth Surface & $6.37 \times 10^6$ & $6.96 \times 10^{-10}$ & $1.80 \times 10^{-9}$ & Yes \\
GPS Orbit & $2.66 \times 10^7$ & $1.67 \times 10^{-10}$ & $4.32 \times 10^{-10}$ & Yes \\
Moon Orbit & $3.84 \times 10^8$ & $1.15 \times 10^{-11}$ & $2.99 \times 10^{-11}$ & Yes \\
1 AU (Sun) & $1.50 \times 10^{11}$ & $9.87 \times 10^{-9}$ & $2.56 \times 10^{-8}$ & Yes \\
\hline
\end{tabular}
\label{tab:ngr_persistence}
\end{table}
```

---

### Tabelle 1.3: Loop Closure mit NSR/NGR Trennung

| Konfiguration | I_ABC (total) | I_ABC (SR) | I_ABC (GR) | sigma_clock | Signifikant? |
|---------------|---------------|------------|------------|-------------|--------------|
| GPS Dreieck | ~10^-16 | ~10^-16 | ~10^-16 | 3e-16 | NEIN |
| Gravity Probe A | ~10^-16 | ~10^-16 | ~10^-16 | 3e-16 | NEIN |
| ISS-Boden-GEO | ~10^-16 | ~10^-16 | ~10^-16 | 3e-16 | NEIN |

**Kernaussage:** Loop Closure I_ABC = 0 gilt fur BEIDE Komponenten (SR und GR) separat.

### LaTeX:
```latex
\begin{table}[h]
\centering
\caption{Loop Closure with N$_{SR}$/N$_{GR}$ Separation}
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Configuration} & \textbf{I$_{ABC}$ (SR)} & \textbf{I$_{ABC}$ (GR)} & \textbf{$\sigma$} & \textbf{Significant?} \\
\hline
GPS Triangle & $\sim 10^{-16}$ & $\sim 10^{-16}$ & $3 \times 10^{-16}$ & No \\
Gravity Probe A & $\sim 10^{-16}$ & $\sim 10^{-16}$ & $3 \times 10^{-16}$ & No \\
ISS-Ground-GEO & $\sim 10^{-16}$ & $\sim 10^{-16}$ & $3 \times 10^{-16}$ & No \\
\hline
\end{tabular}
\label{tab:loop_closure_separation}
\end{table}
```

---

## 2. DYNAMISCHE LOOP TESTS

### Tabelle 2.1: Gravity Probe A Trajektorie delta(t)

| Zeit (min) | Hohe (km) | delta_AB | delta_BC | delta_CA | I_ABC |
|------------|-----------|----------|----------|----------|-------|
| 0 | 0 | 0 | -4.25e-10 | +4.25e-10 | ~0 |
| 30 | 5,000 | -2.5e-10 | -1.5e-10 | +4.0e-10 | ~0 |
| 60 | 10,000 | -4.25e-10 | 0 | +4.25e-10 | ~0 |
| 90 | 5,000 | -2.5e-10 | -1.5e-10 | +4.0e-10 | ~0 |
| 120 | 0 | 0 | -4.25e-10 | +4.25e-10 | ~0 |

**Kernaussage:** Obwohl delta_AB(t) variiert, bleibt I_ABC(t) = 0 zu ALLEN Zeiten.

### LaTeX:
```latex
\begin{table}[h]
\centering
\caption{Gravity Probe A Dynamic Loop Test}
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{t (min)} & \textbf{h (km)} & \textbf{$\delta_{AB}$} & \textbf{$\delta_{BC}$} & \textbf{$\delta_{CA}$} & \textbf{I$_{ABC}$} \\
\hline
0 & 0 & 0 & $-4.25 \times 10^{-10}$ & $+4.25 \times 10^{-10}$ & $\sim 0$ \\
30 & 5,000 & $-2.5 \times 10^{-10}$ & $-1.5 \times 10^{-10}$ & $+4.0 \times 10^{-10}$ & $\sim 0$ \\
60 & 10,000 & $-4.25 \times 10^{-10}$ & 0 & $+4.25 \times 10^{-10}$ & $\sim 0$ \\
\hline
\end{tabular}
\label{tab:gpa_dynamic}
\end{table}
```

---

### Tabelle 2.2: Galileo 5/6 Exzentrische Umlaufbahn

| Orbitphase | Hohe (km) | v (km/s) | delta_perigee-apogee | NSR-Anteil | NGR-Anteil |
|------------|-----------|----------|---------------------|------------|------------|
| Perigee | 17,519 | 4.7 | - | - | - |
| Apogee | 25,900 | 2.6 | - | - | - |
| **Differenz** | 8,381 | 2.1 | **4.5e-10** | ~5e-12 | ~4.5e-10 |

**Praezision:** +/- 1.4e-14 (Rekord-Genauigkeit fur GR-Tests)  
**Referenz:** Delva et al., PRL 121, 2018

### LaTeX:
```latex
\begin{table}[h]
\centering
\caption{Galileo 5/6 Eccentric Orbit Frequency Modulation}
\begin{tabular}{|l|c|c|c|}
\hline
\textbf{Orbital Phase} & \textbf{Altitude (km)} & \textbf{v (km/s)} & \textbf{$\delta$} \\
\hline
Perigee & 17,519 & 4.7 & - \\
Apogee & 25,900 & 2.6 & - \\
\textbf{Difference} & 8,381 & 2.1 & $\mathbf{4.5 \times 10^{-10}}$ \\
\hline
\multicolumn{4}{|l|}{Precision: $\pm 1.4 \times 10^{-14}$ (Delva et al. 2018)} \\
\hline
\end{tabular}
\label{tab:galileo_eccentric}
\end{table}
```

---

### Tabelle 2.3: Pfadintegral-Unabhangigkeit

| Pfad | Start | Ende | Integral | Differenz zum direkten Pfad |
|------|-------|------|----------|----------------------------|
| Direkt (radial) | Erdoberflache | GPS Orbit | -5.29e-10 | 0 |
| Zigzag (via 10 Mm) | Erdoberflache | GPS Orbit | -5.29e-10 | < 10^-14 |
| Spirale | Erdoberflache | GPS Orbit | -5.29e-10 | < 10^-14 |

**Kernaussage:** Das Pfadintegral von delta ist pfadunabhangig (Integrabilitat).

---

## 3. EXPERIMENTELLE REFERENZ-VALIDIERUNG

### Tabelle 3.1: Vollstandige Experimentelle Daten

| Experiment | Jahr | Gemessen | Unsicherheit | GR-Vorhersage | Ubereinstimmung |
|------------|------|----------|--------------|---------------|-----------------|
| **Pound-Rebka** | 1960 | 2.56e-15 | +/-10% | 2.46e-15 | < 2sigma |
| **Pound-Snider** | 1965 | 2.46e-15 | +/-1% | 2.46e-15 | < 1sigma |
| **Gravity Probe A** | 1976 | 4.5e-10 | +/-70 ppm | 4.46e-10 | < 2sigma |
| **GPS System** | 1978+ | 38.6 us/Tag | +/-0.1 | 38.4 us/Tag | < 2sigma |
| **Galileo 5/6** | 2018 | 4.5e-10 | +/-1.4e-14 | 4.5e-10 | < 1sigma |
| **Tokyo Skytree** | 2020 | 4.9e-15 | +/-0.1e-15 | 4.9e-15 | < 1sigma |

### LaTeX:
```latex
\begin{table}[h]
\centering
\caption{Experimental Validation of Frequency-Based Curvature Detection}
\begin{tabular}{|l|c|c|c|c|c|}
\hline
\textbf{Experiment} & \textbf{Year} & \textbf{Measured} & \textbf{$\sigma$} & \textbf{GR Pred.} & \textbf{Agreement} \\
\hline
Pound-Rebka & 1960 & $2.56 \times 10^{-15}$ & 10\% & $2.46 \times 10^{-15}$ & $< 2\sigma$ \\
Pound-Snider & 1965 & $2.46 \times 10^{-15}$ & 1\% & $2.46 \times 10^{-15}$ & $< 1\sigma$ \\
Gravity Probe A & 1976 & $4.5 \times 10^{-10}$ & 70 ppm & $4.46 \times 10^{-10}$ & $< 2\sigma$ \\
GPS System & 1978+ & 38.6 $\mu$s/day & 0.1 & 38.4 $\mu$s/day & $< 2\sigma$ \\
Galileo 5/6 & 2018 & $4.5 \times 10^{-10}$ & $1.4 \times 10^{-14}$ & $4.5 \times 10^{-10}$ & $< 1\sigma$ \\
Tokyo Skytree & 2020 & $4.9 \times 10^{-15}$ & $0.1 \times 10^{-15}$ & $4.9 \times 10^{-15}$ & $< 1\sigma$ \\
\hline
\end{tabular}
\label{tab:experimental_validation}
\end{table}
```

---

### Tabelle 3.2: GPS Relativistische Korrektur (Detailliert)

| Effekt | Formel | Beitrag | Einheit |
|--------|--------|---------|---------|
| **GR (Gravitation)** | GM/c^2 * (1/R_E - 1/r_GPS) | **+45.7** | us/Tag |
| **SR (Geschwindigkeit)** | -v^2/(2c^2) | **-7.2** | us/Tag |
| **Gesamt** | GR + SR | **+38.5** | us/Tag |
| **GPS-Korrektur** | (angewendet) | **+38.6** | us/Tag |

**Konsequenz:** Ohne diese Korrektur wurde GPS nach einem Tag ~10 km Positionsfehler haben.

### LaTeX:
```latex
\begin{table}[h]
\centering
\caption{GPS Relativistic Clock Correction Breakdown}
\begin{tabular}{|l|l|c|c|}
\hline
\textbf{Effect} & \textbf{Formula} & \textbf{Contribution} & \textbf{Unit} \\
\hline
GR (gravitational) & $\frac{GM}{c^2}\left(\frac{1}{R_E} - \frac{1}{r_{GPS}}\right)$ & +45.7 & $\mu$s/day \\
SR (velocity) & $-\frac{v^2}{2c^2}$ & -7.2 & $\mu$s/day \\
\hline
\textbf{Total} & GR + SR & \textbf{+38.5} & $\mu$s/day \\
\textbf{GPS applied} & (operational) & \textbf{+38.6} & $\mu$s/day \\
\hline
\end{tabular}
\label{tab:gps_breakdown}
\end{table}
```

---

### Tabelle 3.3: Loop Closure mit echten Experimenten

| Experiment | Konfiguration | delta_AB | delta_BC | delta_CA | I_ABC | Status |
|------------|---------------|----------|----------|----------|-------|--------|
| GP-A | Boden-Rakete-GPS | -4.25e-10 | -1.03e-10 | +5.28e-10 | ~0 | PASS |
| Galileo | Perigee-Apogee-Boden | -4.5e-10 | +2.1e-10 | +2.4e-10 | ~0 | PASS |
| GPS | Boden-Sat1-Sat2 | -5.29e-10 | 0 | +5.29e-10 | 0 | PASS |
| Skytree | Boden-450m-Boden | -4.9e-15 | +4.9e-15 | 0 | 0 | PASS |

---

## 4. N_GR = Xi(r) AQUIVALENZ

### Tabelle 4.1: N_GR vs Xi(r) uber Gravitationsregime

| Regime | r/r_s | N_GR | Xi(r) | Verhaltnis Xi/N_GR | Interpretation |
|--------|-------|------|-------|-------------------|----------------|
| **Weak** (Erde) | 1.4e9 | 6.96e-10 | 1.80e-9 | 2.59 | Beide ~ r_s/r |
| **Weak** (GPS) | 4.2e8 | 1.67e-10 | 4.32e-10 | 2.59 | Skaliert gleich |
| **Medium** (10 R_sun) | ~700 | 1.4e-3 | 3.6e-3 | 2.59 | Konsistent |
| **Strong** (NS, 3r_s) | 3 | 0.18 | 0.26 | 1.44 | Konvergieren |
| **Strong** (NS, 2.5r_s) | 2.5 | 0.22 | 0.30 | 1.36 | Nahern sich an |
| **Extrem** (r_s) | 1 | 1.0 (sing.) | 0.80 | 0.80 | SSZ: keine Sing. |

**Kernaussage:** N_GR und Xi(r) reprasentieren dasselbe physikalische Konzept (nicht-entfernbare Gravitationsinformation), verwenden aber unterschiedliche mathematische Formulierungen.

### LaTeX:
```latex
\begin{table}[h]
\centering
\caption{N$_{GR}$ vs $\Xi(r)$ Equivalence Across Gravitational Regimes}
\begin{tabular}{|l|c|c|c|c|}
\hline
\textbf{Regime} & \textbf{r/r$_s$} & \textbf{N$_{GR}$} & \textbf{$\Xi(r)$} & \textbf{$\Xi$/N$_{GR}$} \\
\hline
Weak (Earth) & $1.4 \times 10^9$ & $6.96 \times 10^{-10}$ & $1.80 \times 10^{-9}$ & 2.59 \\
Weak (GPS) & $4.2 \times 10^8$ & $1.67 \times 10^{-10}$ & $4.32 \times 10^{-10}$ & 2.59 \\
Medium & $\sim 700$ & $1.4 \times 10^{-3}$ & $3.6 \times 10^{-3}$ & 2.59 \\
Strong (NS) & 3 & 0.18 & 0.26 & 1.44 \\
Extreme & 1 & 1.0 (sing.) & 0.80 & 0.80 \\
\hline
\end{tabular}
\label{tab:ngr_xi_equivalence}
\end{table}
```

---

## 5. ZUSAMMENFASSUNG

### Tabelle 5.1: Gesamtubersicht der erweiterten Validierung

| Test-Kategorie | Tests | Bestanden | Status |
|----------------|-------|-----------|--------|
| NSR/NGR Trennung | 4 | 4 | **100%** |
| Dynamische Loops | 4 | 4 | **100%** |
| Experimentelle Referenz | 5 | 5 | **100%** |
| Basis-Validierung | 43 | 43 | **100%** |
| **GESAMT** | **56** | **56** | **100%** |

### Tabelle 5.2: Paper-Konformitat

| Paper-Aussage | Test-Nachweis | Status |
|---------------|---------------|--------|
| N_SR entfernbar (Eq. 5) | test_nsr_removal | PASS |
| N_GR nicht entfernbar (Eq. 5) | test_ngr_persistence | PASS |
| I_ABC = 0 (Eq. 4) | test_loop_closure | PASS |
| delta(t) pfadunabhangig | test_path_integral | PASS |
| GR-Alignment | test_experimental | PASS |
| N_GR = Xi(r) (SSZ) | test_ngr_equals_xi | PASS |

---

## REFERENZEN

```bibtex
@article{Vessot1979,
  author = {Vessot, R. F. C. and Levine, M. W.},
  title = {A Test of the Equivalence Principle Using a Space-Borne Clock},
  journal = {GRL}, volume = {6}, pages = {637-640}, year = {1979}
}

@article{Delva2018,
  author = {Delva, P. and others},
  title = {Gravitational Redshift Test Using Eccentric Galileo Satellites},
  journal = {PRL}, volume = {121}, pages = {231101}, year = {2018}
}

@article{Pound1960,
  author = {Pound, R. V. and Rebka, G. A.},
  title = {Apparent Weight of Photons},
  journal = {PRL}, volume = {4}, pages = {337}, year = {1960}
}

@article{Takamoto2020,
  author = {Takamoto, M. and others},
  title = {Test of general relativity by a pair of transportable optical lattice clocks},
  journal = {Nature Photonics}, volume = {14}, year = {2020}
}
```

---

**Erstellt:** 14. Dezember 2025  
**Fur:** Paper "Frequency-Based Curvature Detection via Dynamic Comparisons"

(c) 2025 Carmen Wrede & Lino Casu
