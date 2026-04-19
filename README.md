# 🌿 EcoFusionAI – Multimodal Biodiversity Early Warning System

## 🎓 Final Year BE Project – Computer Engineering (SPPU)

EcoFusionAI is a research-grade, multimodal early-warning system that detects biodiversity stress trends in the Western Ghats biodiversity hotspot using satellite vegetation health, species occurrence data, and bird acoustic activity.

## 🚀 **Live Demo**
**🌐 Try the app: [https://ecofusionai.streamlit.app/](https://ecofusionai.streamlit.app/)**

## 👥 **Project Team**

| Team Member | Role |
|-------------|------|
| **Akhila Ohmkumar** | Team Member |
| **Anjali Barge** | Team Member |
| **Neha Dhurgude** | Team Member |
| **Dhanashree Jadhav** | Team Member |
| **Tanvi Powar** | Team Member |

**Final Year BE Project | Computer Engineering | SPPU**

## 📊 **Current System Status**

### **Key Metrics (January 2026):**
- **Analysis Period:** 2018-2024 (7 years)
- **Bird Species:** 163 (Western Ghats filtered)
- **GBIF Records:** 16 yearly summaries
- **Current Stress:** 0.308 (🟢 Low Risk)
- **Audio Signal:** 0.247

### **Data Sources:**
- 🛰️ **MODIS NDVI** - Satellite vegetation health (2018-2024)
- 🦅 **GBIF Species Data** - Long-term biodiversity baseline (1990-2024)  
- 🔊 **BirdCLEF Audio** - Regional biodiversity indicator (163 species)

## 🌐 **Dashboard Features**

The interactive dashboard includes 5 main sections:

1. **🏠 Overview** - Research objectives and key metrics
2. **📈 Biodiversity Trends** - Long-term species patterns
3. **🚨 Early Warning System** - Stress detection and alerts
4. **🤖 ML Model Insights** - Model performance and feature importance
5. **🛰️ NDVI Regional Analysis** - Regional vegetation health

## 🔬 **Scientific Approach**

All data sources are geographically filtered to Western Ghats region (8.0-21.0°N, 73.0-77.5°E) ensuring meaningful ecological correlations and scientific validity.

**Eco-Stress Index Formula:**
- Environmental stress (50%) + Acoustic signal loss (30%) + Sampling pressure (20%)
- Current status: 0.308 (Low Risk)

## 🚀 **Quick Start**

### **Live Demo (Recommended)**
Visit: [https://ecofusionai.streamlit.app/](https://ecofusionai.streamlit.app/)

### **Local Setup**
```bash
git clone https://github.com/AB2511/EcoFusionAI.git
cd EcoFusionAI
pip install -r requirements.txt
streamlit run app.py
```

## 📁 **Project Structure**
```
EcoFusionAI/
├── app.py                              # Main dashboard
├── data/                               # Western Ghats datasets
├── notebooks/                          # 3 processing notebooks
├── models/                             # Trained ML models
├── SYSTEM_ARCHITECTURE.md              # Technical architecture
├── TECHNICAL_DOCUMENTATION.md          # Setup and usage guide
├── ACADEMIC_CONTRIBUTIONS.md           # Research value and achievements
└── README.md                           # This file
```

## 🎯 **Key Results**
- **NDVI dominance:** 46.0% feature importance (vegetation health drives biodiversity)
- **Critical species identified:** White-cheeked Barbet, Malabar Whistling Thrush, Indian Scimitar Babbler
- **Current ecosystem status:** Low stress (0.308) with stable trend

## 📚 **Data Citation**
GBIF.org (28 January 2026) GBIF Occurrence Download  
https://doi.org/10.15468/dl.zdxvtf  
*Herbarium of French Institute of Pondicherry*

## 📞 **Contact**
**🎓 Academic Project:** Final Year BE - Computer Engineering (SPPU)  
**📧 Repository:** [https://github.com/AB2511/EcoFusionAI](https://github.com/AB2511/EcoFusionAI)  
**🌐 Live Demo:** [https://ecofusionai.streamlit.app/](https://ecofusionai.streamlit.app/)
