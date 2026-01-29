# EcoFusionAI System Architecture

## 🏗️ Overall System Architecture

**EcoFusionAI is a research-grade, multimodal early-warning system that detects biodiversity stress trends using satellite vegetation health, species occurrence data, and bird acoustic activity.**

```
┌─────────────────────────────────────────────────────────────────┐
│                    EcoFusionAI System Architecture              │
│                   (Final Multimodal Version)                    │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Sources  │    │   Processing    │    │   Application   │
│                 │    │     Layer       │    │     Layer       │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ • MODIS NDVI    │───▶│ • Multimodal    │───▶│ • Streamlit     │
│   (Point Sample)│    │   Fusion        │    │   Dashboard     │
│ • GBIF Species  │    │ • Eco-Stress    │    │ • Early Warning │
│   Occurrences   │    │   Index         │    │   System        │
│ • BirdCLEF      │    │ • ML Regression │    │ • Feature       │
│   Audio Meta    │    │   Models        │    │   Importance    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Storage       │    │   ML Models     │    │   Outputs       │
│                 │    │                 │    │                 │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ • Fusion CSV    │    │ • Linear        │    │ • Stress Index  │
│ • Model Results │    │   Regression    │    │   Trends        │
│ • Feature       │    │ • Random Forest │    │ • Risk Alerts   │
│   Importance    │    │   Regressor     │    │ • Biodiversity  │
│ • Raw NDVI      │    │                 │    │   Insights      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 🔧 Technical Architecture Components

### 1. **Data Ingestion Layer**

#### A. **Satellite Data Processing (Google Earth Engine)**
```python
# Architecture: Point sampling approach (CRITICAL FIX applied)
┌─────────────────────────────────────────────────────────────┐
│                Google Earth Engine (GEE)                   │
├─────────────────────────────────────────────────────────────┤
│ • MODIS/061/MOD13Q1 Collection (16-day composites)        │
│ • Point sampling (30 points per region)                   │
│ • NDVI computation with masking (updateMask)              │
│ • Temporal analysis: 2018-2024 (7 years)                 │
│ • Scale: 250m resolution                                   │
│ • Output: Regional yearly NDVI means                       │
└─────────────────────────────────────────────────────────────┘
```

**Key Functions:**
- `get_sample_points()`: Generates random points within regions
- `extract_ndvi_temporal()`: Point sampling NDVI extraction
- **CRITICAL FIX**: `sampleRegions()` instead of `reduceRegions()`

#### B. **Biodiversity Data (GBIF Cube)**
```python
# Architecture: Species occurrence trends
┌─────────────────────────────────────────────────────────────┐
│                 GBIF Biodiversity Data                     │
├─────────────────────────────────────────────────────────────┤
│ • Yearly species richness (1990-2024)                     │
│ • Total occurrences per year                              │
│ • Sampling-corrected richness (species_per_1000_occ)      │
│ • Western Ghats focus region                              │
│ • Quality-filtered observations                            │
└─────────────────────────────────────────────────────────────┘
```

#### C. **Acoustic Data (BirdCLEF 2024)**
```python
# Architecture: Audio metadata aggregation
┌─────────────────────────────────────────────────────────────┐
│                BirdCLEF Audio Processing                   │
├─────────────────────────────────────────────────────────────┤
│ • 182 species audio metadata                              │
│ • Normalized audio strength calculation                    │
│ • Year-agnostic acoustic proxy                            │
│ • Aggregated to single signal strength                    │
│ • Scientifically defensible approach                       │
└─────────────────────────────────────────────────────────────┘
```

### 2. **Multimodal Fusion Engine**

#### A. **Data Fusion Pipeline (Notebook 3)**
```python
# Architecture: Three-stream fusion system
┌─────────────────────────────────────────────────────────────┐
│                   Multimodal Fusion Engine                 │
├─────────────────────────────────────────────────────────────┤
│ Stream 1: Environmental (NDVI)                            │
│   • Regional NDVI aggregation by year                     │
│   • Mean and standard deviation calculation               │
│                                                            │
│ Stream 2: Biodiversity (GBIF)                            │
│   • Species richness trends                               │
│   • Sampling bias correction                              │
│                                                            │
│ Stream 3: Acoustic (BirdCLEF)                            │
│   • Audio signal strength proxy                           │
│   • Repeated across temporal dimension                     │
│                                                            │
│ Fusion Output: 7 years × 7 features                       │
└─────────────────────────────────────────────────────────────┘
```

#### B. **Eco-Stress Index Calculation**
```python
# Architecture: Composite early-warning indicator
┌─────────────────────────────────────────────────────────────┐
│                 Eco-Stress Index Engine                    │
├─────────────────────────────────────────────────────────────┤
│ Formula:                                                   │
│   eco_stress_index = (1 - ndvi_mean) * 0.5 +             │
│                      (1 - audio_signal_strength) * 0.3 +  │
│                      (occurrences / max_occurrences) * 0.2│
│                                                            │
│ Components:                                                │
│   • Environmental stress (NDVI decline)                   │
│   • Acoustic decline (bird activity proxy)                │
│   • Sampling pressure (observation effort)                │
│                                                            │
│ Range: 0.0 (healthy) → 1.0 (critical stress)             │
│ Thresholds: <0.45 (Low), 0.45-0.6 (Moderate), >0.6 (High)│
└─────────────────────────────────────────────────────────────┘
```

### 3. **Machine Learning Pipeline**

#### A. **Regression Models Architecture**
```python
# Architecture: Dual-model regression system
┌─────────────────────────────────────────────────────────────┐
│                ML Regression Architecture                   │
├─────────────────────────────────────────────────────────────┤
│ Target Variable: species_per_1000_occ (sampling-corrected) │
│                                                            │
│ Features (4):                                              │
│   1. ndvi_mean              # Environmental signal         │
│   2. ndvi_std               # Environmental variability    │
│   3. audio_signal_strength  # Acoustic proxy              │
│   4. occurrences            # Sampling pressure control    │
│                                                            │
│ Model 1: Linear Regression                                 │
│   • Interpretable coefficients                            │
│   • Baseline performance                                   │
│   • Feature relationship analysis                          │
│                                                            │
│ Model 2: Random Forest Regressor                          │
│   • n_estimators: 300                                     │
│   • Feature importance extraction                          │
│   • Nonlinear pattern detection                           │
└─────────────────────────────────────────────────────────────┘
```

#### B. **Feature Importance Analysis**
```python
# Architecture: Driver identification system
┌─────────────────────────────────────────────────────────────┐
│              Feature Importance Architecture                │
├─────────────────────────────────────────────────────────────┤
│ Results (Random Forest):                                   │
│   1. ndvi_mean: 46.0% (Environmental dominance)           │
│   2. occurrences: 28.6% (Sampling effect)                 │
│   3. ndvi_std: 25.4% (Environmental variability)          │
│   4. audio_signal_strength: 0.0% (Constant signal)        │
│                                                            │
│ Scientific Insight:                                        │
│   • Environmental factors drive biodiversity patterns      │
│   • Sampling effort significantly affects measurements     │
│   • NDVI (vegetation health) is primary driver            │
│   • Audio signal constant due to regional aggregation     │
└─────────────────────────────────────────────────────────────┘
```

### 4. **Application Layer (Streamlit Dashboard)**

#### A. **Web Application Architecture**
```python
# Architecture: Six-tab research dashboard
┌─────────────────────────────────────────────────────────────┐
│                Streamlit Dashboard Architecture             │
├─────────────────────────────────────────────────────────────┤
│ Tab 1: Overview                                            │
│   • Research-grade positioning statement                   │
│   • SPPU Final Year BE Project branding                   │
│   • Key metrics and current system status                  │
│                                                            │
│ Tab 2: Scientific Methodology                             │
│   • Temporal alignment strategy explanation                │
│   • Data fusion process documentation                      │
│   • Scientific justification for approach                  │
│                                                            │
│ Tab 3: Biodiversity Trends                                │
│   • GBIF species richness timeline (1990-2024)            │
│   • Sampling bias correction explanation                   │
│   • Long-term baseline analysis                            │
│                                                            │
│ Tab 4: Early Warning System                               │
│   • Eco-stress index visualization                        │
│   • Risk threshold alerts (Low/Medium/High)                │
│   • Current status: 0.308 (Low Risk)                      │
│                                                            │
│ Tab 5: ML Model Insights                                  │
│   • Model performance comparison (Linear vs Random Forest) │
│   • Feature importance visualization (NDVI dominance)      │
│   • Small dataset limitation acknowledgment                │
│                                                            │
│ Tab 6: NDVI Regional Analysis                             │
│   • Regional NDVI breakdown (3 Western Ghats regions)     │
│   • Temporal trends (2018-2024)                           │
│   • Individual region health assessment                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Architecture

### **End-to-End Processing Pipeline**

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Notebook 1 │───▶│  Notebook 2 │───▶│  Notebook 3 │───▶│   App.py    │
│ NDVI Extract│    │GBIF + Audio │    │Multimodal   │    │ Dashboard   │
│             │    │ Aggregation │    │   Fusion    │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
       │                   │                   │                   │
       ▼                   ▼                   ▼                   ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│• Point      │    │• Species    │    │• Data       │    │• Early      │
│  Sampling   │    │  Richness   │    │  Fusion     │    │  Warning    │
│• 3 Regions  │    │• Audio Meta │    │• ML Models  │    │• Risk       │
│• 2018-2024  │    │• 1990-2024  │    │• Stress     │    │  Alerts     │
│             │    │             │    │  Index      │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### **Detailed Processing Workflow**

#### **Phase 1: NDVI Extraction (Notebook 1)**
```python
1. Earth Engine Authentication
   ├── ee.Initialize(project='ecofusion-ai')
   ├── MODIS Collection 6.1 access
   └── Point sampling methodology

2. Regional NDVI Processing
   ├── 3 Western Ghats regions
   ├── 30 random points per region
   ├── Annual mean calculation (2018-2024)
   └── CSV export: ndvi_temporal_dataset_POINT_SAMPLING.csv

3. CRITICAL FIX Applied
   ├── sampleRegions() instead of reduceRegions()
   ├── Bypasses MODIS masking issues
   └── Produces real NDVI values
```

#### **Phase 2: Biodiversity & Audio (Notebook 2)**
```python
1. GBIF Data Processing
   ├── Species occurrence trends (1990-2024)
   ├── Sampling bias correction
   ├── Regional aggregation
   └── CSV export: gbif_biodiversity_yearly.csv

2. BirdCLEF Audio Processing
   ├── 182 species metadata
   ├── Normalized audio strength
   ├── Year-agnostic aggregation
   └── CSV export: audio_species_richness.csv

3. Quality Assurance
   ├── Data validation
   ├── Missing value handling
   └── Format standardization
```

#### **Phase 3: Multimodal Fusion (Notebook 3)**
```python
1. Data Integration
   ├── NDVI yearly aggregation
   ├── Audio signal expansion
   ├── GBIF temporal alignment
   └── Feature vector creation

2. ML Model Training
   ├── Linear Regression (baseline)
   ├── Random Forest (feature importance)
   ├── Performance evaluation
   └── Model serialization

3. Eco-Stress Index
   ├── Composite indicator calculation
   ├── Risk threshold definition
   ├── Temporal trend analysis
   └── Early warning signals

4. Output Generation
   ├── fusion_multimodal_dataset.csv
   ├── model_results_summary.csv
   └── feature_importance.csv
```

#### **Phase 4: Dashboard Visualization (App.py)**
```python
1. Data Loading
   ├── Cached data loading (@st.cache_data)
   ├── Error handling
   └── Performance optimization

2. Interactive Visualization
   ├── Biodiversity trend plots
   ├── Stress index timeline
   ├── Feature importance charts
   └── Regional NDVI breakdown

3. Early Warning System
   ├── Real-time risk assessment
   ├── Alert generation (HIGH/MODERATE/LOW)
   ├── Scientific interpretation
   └── Conservation recommendations
```

---

## 🗄️ Data Architecture

### **Storage Layer Organization**

```
EcoFusion/
├── data/                                    # Input Data Layer
│   ├── ndvi_temporal_dataset_POINT_SAMPLING.csv  # 🛰️ NDVI point sampling (21 records)
│   ├── gbif_biodiversity_yearly_WESTERN_GHATS.csv # 🦅 Species trends (16 years, 1990-2013)
│   ├── audio_species_richness_WESTERN_GHATS.csv   # 🔊 Audio metadata (163 species)
│   ├── audio_signal_summary_WESTERN_GHATS.csv     # 🔊 Audio signal summary
│   ├── species_stress_indicators_WESTERN_GHATS.csv # 🚨 Species stress analysis
│   └── naturalearth/                             # 🗺️ Geographic boundaries
│
├── models/                                  # Model Persistence Layer
│   ├── ecofusion_rf_v2.pkl                      # 🤖 Random Forest v2
│   ├── ecofusion_features_v2.txt                # 📋 Feature list
│   ├── ecofusion_feature_importance_v2.csv      # 🎯 Feature importance
│   └── ecofusion_metrics_v2.json                # 📊 Model metrics
│
├── outputs/                                 # Results & Artifacts Layer
│   ├── fusion_multimodal_dataset_WESTERN_GHATS.csv # 🔬 Fused dataset (7 years)
│   ├── model_results_summary.csv                # 📊 ML performance
│   └── feature_importance.csv                   # 🎯 Driver analysis
│
└── notebooks/                               # Processing Pipeline
    ├── notebook_01_environment_ndvi.ipynb       # 🛰️ NDVI extraction
    ├── notebook-2-biodiversity-feature-engineering.ipynb # 🦅 GBIF + Audio
    └── notebook_03_multimodal_fusion.ipynb      # 🔬 ML fusion
```

### **Data Schema Architecture**

#### **Fusion Dataset Schema (fusion_multimodal_dataset_WESTERN_GHATS.csv)**
```python
Schema: Multimodal temporal dataset (Western Ghats focused)
├── year: int                          # Temporal dimension (2018-2024)
├── species_richness: int              # GBIF species count
├── occurrences: int                   # GBIF observation count
├── species_per_1000_occ: float        # Sampling-corrected richness (TARGET)
├── species_per_1000_occ_smooth: float # Smoothed richness indicator
├── ndvi_mean: float                   # Regional NDVI average
├── ndvi_std: float                    # NDVI variability
├── audio_signal_strength: float       # Acoustic proxy (0.899 constant)
├── species_stress_index: float        # Species-specific stress indicator
├── critical_species_stress: float     # Critical species stress level
├── high_species_stress: float         # High stress species indicator
├── eco_stress_index: float            # Composite stress indicator
├── environmental_stress: float        # Environmental component
└── biodiversity_decline: float        # Biodiversity decline indicator

Records: 7 rows × 14 columns (2018-2024)
Target: Regression (species_per_1000_occ_smooth)
Current Status: 0.308 eco_stress_index (Low Risk)
```

#### **Model Results Schema**
```python
Model Performance Schema:
├── Model: str                         # Algorithm name
├── RMSE: float                        # Root Mean Square Error
└── R2: float                          # R-squared score

Feature Importance Schema:
├── Feature: str (index)               # Feature name
└── importance: float                  # Random Forest importance
```

---

## ⚙️ Technology Stack Architecture

### **Core Dependencies & Versions**

#### **Data Processing Stack**
```python
┌─────────────────────────────────────────────────────────────┐
│                 Data Processing Layer                       │
├─────────────────────────────────────────────────────────────┤
│ pandas==2.2.2          # DataFrame operations              │
│ numpy==1.26.4          # Numerical computing               │
│ scikit-learn==1.4.2    # ML algorithms (LR, RF)           │
│ earthengine-api        # Google Earth Engine client        │
└─────────────────────────────────────────────────────────────┘
```

#### **Visualization & Web Stack**
```python
┌─────────────────────────────────────────────────────────────┐
│              Visualization & Web Layer                      │
├─────────────────────────────────────────────────────────────┤
│ streamlit==1.30.0      # Web application framework         │
│ matplotlib==3.8.4      # Static plotting                   │
│ seaborn==0.13.2        # Statistical visualization         │
└─────────────────────────────────────────────────────────────┘
```

### **External Service Integration**

#### **Google Earth Engine Architecture**
```python
┌─────────────────────────────────────────────────────────────┐
│              Google Earth Engine Integration                │
├─────────────────────────────────────────────────────────────┤
│ Authentication: OAuth2 (project='ecofusion-ai')           │
│ Collections Used:                                          │
│   • MODIS/061/MOD13Q1 (16-day NDVI composites)           │
│ Processing Method: Point sampling (sampleRegions)         │
│ Scale: 250 meters                                          │
│ Temporal Range: 2018-2024                                 │
│ Output: Regional yearly NDVI statistics                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔒 Security & Limitations Architecture

### **Research Limitations (Explicitly Acknowledged)**
```python
┌─────────────────────────────────────────────────────────────┐
│                Research Limitations                         │
├─────────────────────────────────────────────────────────────┤
│ Temporal Scope:                                            │
│   • Small dataset: 7 years (2018-2024)                    │
│   • Limited statistical power                             │
│   • Negative R² expected with small samples               │
│                                                            │
│ Spatial Scope:                                            │
│   • 3 regions (proof-of-concept)                          │
│   • Western Ghats focus only                              │
│   • Point sampling approach                               │
│                                                            │
│ Methodological:                                           │
│   • Audio signal aggregated yearly                        │
│   • Prototype-level system                                │
│   • Research methodology over production accuracy          │
└─────────────────────────────────────────────────────────────┘
```

### **Academic Positioning**
```python
┌─────────────────────────────────────────────────────────────┐
│                Academic Positioning                         │
├─────────────────────────────────────────────────────────────┤
│ Project Type: Decision-support prototype                   │
│ Target Users: Researchers, forest officials, NGOs          │
│ Contribution: Multimodal ecological data fusion            │
│ Innovation: Early-warning stress index                     │
│ Validation: Scientifically defensible methodology          │
│ Scope: Final Year BE Project (SPPU)                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Performance & Scalability Architecture

### **Current Performance Metrics**
```python
┌─────────────────────────────────────────────────────────────┐
│                Performance Characteristics                  │
├─────────────────────────────────────────────────────────────┤
│ Data Processing:                                           │
│   • NDVI extraction: ~15-25 minutes (3 regions)           │
│   • Fusion processing: <1 minute                          │
│   • ML training: <1 minute                                │
│                                                            │
│ Dashboard Performance:                                     │
│   • Load time: <5 seconds                                 │
│   • Plot rendering: <2 seconds                            │
│   • Interactive response: Real-time                        │
│                                                            │
│ Current System Status (January 2026):                     │
│   • Eco-stress index: 0.308 (🟢 Low Risk)                │
│   • Bird species analyzed: 163 (Western Ghats)            │
│   • Audio signal strength: 0.247 (24.7% ecosystem health) │
│   • NDVI dominance: 46.0% feature importance              │
│                                                            │
│ Memory Usage:                                             │
│   • Peak RAM: <2GB                                        │
│   • Streamlit app: <500MB                                 │
│   • Model size: <10MB                                     │
└─────────────────────────────────────────────────────────────┘
```

### **Scalability Pathways**
```python
┌─────────────────────────────────────────────────────────────┐
│                 Future Scalability                         │
├─────────────────────────────────────────────────────────────┤
│ Data Expansion:                                            │
│   • More regions (11+ originally planned)                 │
│   • Longer temporal series (10+ years)                    │
│   • Additional species groups                             │
│                                                            │
│ Technical Enhancement:                                     │
│   • Real-time satellite ingestion                         │
│   • Deep learning for audio analysis                      │
│   • Spatial visualization (GeoTIFF)                       │
│   • Production deployment                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Stakeholder Architecture

### **Target User Categories**
```python
┌─────────────────────────────────────────────────────────────┐
│                 Stakeholder Ecosystem                      │
├─────────────────────────────────────────────────────────────┤
│ Government:                                                │
│   • Forest Department officials                           │
│   • Ministry of Environment (MoEFCC)                      │
│   • State biodiversity boards                             │
│                                                            │
│ Research & Academia:                                       │
│   • IISc, NCBS researchers                                │
│   • Environmental science students                         │
│   • Conservation biologists                               │
│                                                            │
│ Conservation Organizations:                                │
│   • WWF India                                             │
│   • Wildlife Conservation Society                          │
│   • Local NGOs                                            │
│                                                            │
│ Policy & Planning:                                        │
│   • Climate change planners                               │
│   • Biodiversity policy makers                            │
│   • Conservation strategists                              │
└─────────────────────────────────────────────────────────────┘
```

---

This updated system architecture accurately reflects the **final multimodal fusion approach** with proper positioning as a **research-grade early-warning system** for **Final Year BE Project (SPPU)**. The architecture emphasizes the **three-notebook pipeline**, **eco-stress index innovation**, and **honest acknowledgment of research limitations**.