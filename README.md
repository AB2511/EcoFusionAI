# 🌿 EcoFusionAI – Multimodal Biodiversity Early Warning System

## 🎓 Final Year BE Project – Computer Engineering (SPPU)

**EcoFusionAI is a research-grade, multimodal early-warning system that detects biodiversity stress trends using satellite vegetation health, species occurrence data, and bird acoustic activity.**

## 🚀 **Live Demo**
**🌐 Try the app: [https://ecofusionai.streamlit.app/](https://ecofusionai.streamlit.app/)**

The system integrates:
- 🛰️ **Satellite-derived vegetation health** (NDVI – MODIS)
- 🦅 **Species occurrence trends** (GBIF Cube)
- 🔊 **Bird acoustic activity** (BirdCLEF 2024)

The project focuses on the **Western Ghats**, a global biodiversity hotspot, and demonstrates how AI/ML can support conservation monitoring and decision-making.

## 📌 Project Objectives

- **Detect long-term biodiversity stress trends**
- **Combine heterogeneous ecological data sources**
- **Develop a composite Eco-Stress Index**
- **Apply ML models for pattern discovery**
- **Provide an interactive dashboard for interpretation**

## 🧠 System Architecture

```
Satellite NDVI (MODIS)
        ↓
Species Occurrence (GBIF)
        ↓
Bird Audio Metadata (BirdCLEF)
        ↓
Multimodal Data Fusion
        ↓
Eco-Stress Index Calculation
        ↓
ML Models (RF, LR)
        ↓
Interactive Dashboard (Streamlit)
```

## 🔁 User Workflow

### 1️⃣ Data Preparation (Offline)
- NDVI extracted via Google Earth Engine
- GBIF biodiversity trends computed yearly
- BirdCLEF audio metadata aggregated

### 2️⃣ Multimodal Fusion
- Environmental + Biological + Acoustic signals merged
- Sampling bias corrected
- Features normalized

### 3️⃣ Stress Index Computation
**Eco-Stress Index combines:**
- NDVI decline (environmental degradation)
- Acoustic signal loss (avian activity proxy)
- Observation pressure (sampling effort)

### 4️⃣ ML Analysis
- Linear Regression (baseline)
- Random Forest (feature importance)
- Results interpreted (not overclaimed)

### 5️⃣ Visualization
- Biodiversity trends
- Stress alerts
- Feature importance insights

## 👤 Intended Users

| User | How they use EcoFusionAI |
|------|--------------------------|
| **Forest officers** | Identify high-risk years |
| **Conservation NGOs** | Monitor ecosystem health |
| **Researchers** | Study environment–species links |
| **Students** | Learn multimodal AI |
| **Policy planners** | Early warning signals |

## 🧪 Use Cases

### ✅ Use Case 1: Early Biodiversity Stress Detection
Detect years where vegetation loss + reduced bird activity indicate ecosystem stress.

### ✅ Use Case 2: Conservation Priority Identification
Identify periods needing conservation intervention.

### ✅ Use Case 3: Research & Education
Demonstrate multimodal AI applied to ecology.

## 📊 Machine Learning Insights

- **NDVI is the strongest driver** of biodiversity change
- **Sampling effort significantly affects** observations
- **Audio data acts as a complementary signal**
- **Negative R² reflects small-sample research limitation**, not model failure

## ⚠️ Limitations (Explicitly Acknowledged)

- Small temporal dataset (7 years)
- Audio signal aggregated yearly
- Prototype-level system (not production)

## 🚀 Future Enhancements

- Region-wise user input
- Real-time satellite ingestion
- GeoTIFF-based spatial visualization
- Larger temporal datasets
- Deep learning for audio signals

## 🏁 Conclusion

**EcoFusionAI demonstrates how multimodal AI systems can act as early warning tools for biodiversity loss.** While not designed for precise prediction, the system provides scientifically defensible insights useful for conservation planning and research.

---

## 🚀 Quick Start

### 🌐 **Live Demo (Recommended)**
**Visit the deployed app: [https://ecofusionai.streamlit.app/](https://ecofusionai.streamlit.app/)**

No installation required! Explore the complete multimodal biodiversity monitoring system directly in your browser.

### 💻 **Local Development**

#### Prerequisites
- Python 3.8+
- Google Earth Engine account (for Notebook 1)

#### Installation
```bash
git clone https://github.com/AB2511/EcoFusionAI.git
cd EcoFusionAI
pip install -r requirements.txt
```

#### Running Locally
```bash
streamlit run app.py
```

### 📓 **Processing Pipeline**
1. **Notebook 1**: NDVI extraction (requires Earth Engine authentication)
2. **Notebook 2**: GBIF + Audio data processing  
3. **Notebook 3**: Multimodal fusion + ML analysis
4. **App.py**: Interactive dashboard visualization

---

## 📋 Project Structure

```
EcoFusionAI/
├── notebooks/                          # Processing Pipeline
│   ├── notebook_01_environment_ndvi.ipynb    # 🛰️ NDVI extraction (Phase-1)
│   ├── notebook_02_biodiversity_audio.ipynb  # 🦅 GBIF + Audio processing
│   └── notebook_03_multimodal_fusion.ipynb   # 🔬 Multimodal fusion + ML
│
├── data/                               # Essential Data Files
│   ├── ndvi_temporal_dataset_POINT_SAMPLING.csv  # NDVI results (Phase-1 → Phase-2)
│   ├── gbif_biodiversity_yearly.csv              # Species occurrence trends
│   ├── audio_species_richness.csv                # Bird acoustic metadata
│   └── naturalearth/                             # Geographic boundaries
│
├── app.py                              # 🖥️ Streamlit Dashboard
├── fusion_multimodal_dataset.csv       # 🔬 Final fused dataset
├── model_results_summary.csv           # 📊 ML performance results
├── feature_importance.csv              # 🎯 Feature importance analysis
├── requirements.txt                    # 📦 Dependencies
├── README.md                          # 📖 Project documentation
├── SYSTEM_ARCHITECTURE.md             # 🏗️ Technical architecture
└── .gitignore                         # 🚫 Git ignore rules
```

## 🎯 Key Stakeholders

| Category | Examples |
|----------|----------|
| **Government** | Forest Dept., MoEFCC |
| **NGOs** | WWF India, WCS |
| **Research** | IISc, NCBS |
| **Academia** | Environmental science students |
| **Policy** | Climate & biodiversity planners |

**This project is a decision-support prototype, not a consumer app.**

## 🌐 **Live Application**

**🚀 Experience EcoFusionAI: [https://ecofusionai.streamlit.app/](https://ecofusionai.streamlit.app/)**

### **Dashboard Features:**
- 📊 **Overview** - System introduction and key metrics
- 📈 **Biodiversity Trends** - Long-term species richness analysis
- 🚨 **Early Warning System** - Real-time biodiversity stress alerts
- 🤖 **ML Model Insights** - Feature importance and model performance
- 🛰️ **Exploratory NDVI View** - Regional vegetation health analysis

---

## 👥 **Project Team**

**Final Year BE Students - Computer Engineering (SPPU)**

| Team Member | Role |
|-------------|------|
| **Akhila Ohmkumar** | Team Member |
| **Anjali Barge** | Team Member |
| **Neha Dhurgude** | Team Member |
| **Dhanashree Jadhav** | Team Member |
| **Tanvi Powar** | Team Member |

*Final Year BE Project | Computer Engineering | SPPU*
