# 🔧 EcoFusionAI Technical Documentation

## 🏗️ **System Architecture**

### **Technology Stack:**
- **Backend:** Python 3.8+, Pandas, NumPy, Scikit-learn
- **Visualization:** Matplotlib, Seaborn, Streamlit
- **Data Processing:** Google Earth Engine, GBIF API
- **ML Framework:** Scikit-learn (Linear Regression, Random Forest)
- **Deployment:** Streamlit Cloud, GitHub Actions

### **System Components:**

```
📊 Data Pipeline
├── 🛰️ Google Earth Engine (MODIS NDVI extraction)
├── 🦅 GBIF API (Species occurrence data)
├── 🔊 BirdCLEF Dataset (Audio metadata processing)
└── 🔄 Multimodal Fusion Engine

🤖 ML Pipeline  
├── 📈 Feature Engineering (bias correction, normalization)
├── 🎯 Model Training (Linear Regression, Random Forest)
├── ✅ Cross-Validation (5-fold with F1 scoring)
└── 📊 Performance Evaluation (RMSE, R², Feature Importance)

🌐 Dashboard Application
├── 🖥️ Streamlit Framework (Interactive web interface)
├── 📊 Matplotlib/Seaborn (Data visualization)
├── 🔄 Real-time Calculations (Dynamic stress index)
└── 📱 Responsive Design (Desktop + mobile support)
```

## 🌐 **Dashboard Features**

### **5 Interactive Sections:**

#### 🏠 **Overview**
- System introduction and research objectives
- Key metrics summary with real-time values
- Scientific approach explanation
- Navigation guide for all features

#### 📈 **Biodiversity Trends**
- Long-term GBIF species richness analysis (1990-2024)
- Sampling-corrected biodiversity indicators
- Historical peak identification (2011: 976.74 species/1000 occ)
- Recent decline quantification (-15.4% in 2018-2024)

#### 🚨 **Early Warning System**
- **Eco-Stress Index:** Real-time biodiversity stress assessment
- **Formula:** (1-NDVI)*0.5 + (1-Audio)*0.3 + (Sampling)*0.2
- **Risk Thresholds:** 🟢 Low (0.0-0.4), 🟡 Medium (0.4-0.6), 🔴 High (0.6-1.0)
- **Current Status:** 0.308 (🟢 Low Risk) with stable trend

#### 🤖 **ML Model Insights**
- **Model Comparison:** Linear Regression vs Random Forest
- **Feature Importance Analysis:** NDVI dominance (46.0%)
- **Performance Metrics:** RMSE, R², Cross-validation scores
- **Scientific Interpretation:** Environmental vs acoustic vs sampling factors

#### 🛰️ **NDVI Regional Analysis**
- **3 Key Regions:** Periyar National Park, Western Ghats North/South
- **Vegetation Health Monitoring:** 2018-2024 temporal trends
- **Regional Statistics:** Mean NDVI, variability, health rankings

## 📊 **Data Sources & Integration**

### 🛰️ **MODIS NDVI (Environmental Layer)**
- **Source:** NASA MODIS Terra satellite imagery
- **Period:** 2018-2024 (7 years, high temporal resolution)
- **Processing:** Google Earth Engine cloud-masked extraction
- **Coverage:** Point sampling across 3 Western Ghats regions

### 🦅 **GBIF Biodiversity (Species Layer)**
- **Source:** Herbarium of French Institute of Pondicherry (IFP)
- **Period:** 1990-2024 (35 years, long-term baseline)
- **Records:** 25,023 botanical specimens, 16 yearly summaries
- **DOI:** https://doi.org/10.15468/dl.zdxvtf

### 🔊 **BirdCLEF Audio (Acoustic Layer)**
- **Source:** BirdCLEF 2024 competition dataset
- **Coverage:** 163 Western Ghats bird species
- **Records:** 2,175 audio recordings analyzed
- **Key Species:** White-cheeked Barbet, Malabar Whistling Thrush, Indian Scimitar Babbler

## 🔄 **Data Processing Workflow**

### **1. Data Preparation (Automated)**
- **NDVI Extraction:** Google Earth Engine API with cloud masking
- **GBIF Processing:** Automated download with geographic filtering
- **Audio Analysis:** BirdCLEF metadata aggregation and species mapping
- **Quality Control:** Data validation, outlier detection, bias correction

### **2. Multimodal Fusion (Real-time)**
- **Temporal Alignment:** Strategic alignment preserving long-term credibility
- **Feature Engineering:** Composite indicators and stress metrics
- **Normalization:** Cross-source data standardization
- **Validation:** Statistical consistency checks

### **3. ML Analysis (Interactive)**
- **Model Training:** Automated pipeline with cross-validation
- **Feature Importance:** Real-time ranking and interpretation
- **Prediction:** Biodiversity stress forecasting
- **Uncertainty:** Confidence intervals and limitation acknowledgment

## 💻 **Installation & Setup**

### **Prerequisites:**
- Python 3.8+ (recommended: Python 3.9)
- Google Earth Engine account (for NDVI data processing)
- Git for version control

### **Installation Steps:**
```bash
# 1. Clone the repository
git clone https://github.com/AB2511/EcoFusionAI.git
cd EcoFusionAI

# 2. Create virtual environment (recommended)
python -m venv ecofusion_env
source ecofusion_env/bin/activate  # On Windows: ecofusion_env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up Google Earth Engine (for data processing)
earthengine authenticate

# 5. Run the dashboard
streamlit run app.py
```

### **Development Workflow:**
```bash
# Option A: Use existing processed data (Quick Start)
streamlit run app.py  # Uses pre-processed datasets

# Option B: Run complete ML pipeline (Advanced)
python run_ml_pipeline.py  # Generates fresh model artifacts
streamlit run app.py

# Option C: Full data processing (Research)
# 1. Run Notebook 1: NDVI extraction (requires Earth Engine)
# 2. Run Notebook 2: Biodiversity feature engineering  
# 3. Run Notebook 3: Multimodal fusion + ML analysis
# 4. Launch dashboard: streamlit run app.py
```

## 📁 **Project Structure**
```
EcoFusionAI/
├── 📊 Data Pipeline
│   ├── notebooks/
│   │   ├── notebook_01_environment_ndvi.ipynb     # 🛰️ NDVI extraction
│   │   ├── notebook-2-biodiversity-feature-engineering.ipynb  # 🦅 GBIF + Audio
│   │   └── notebook_03_multimodal_fusion.ipynb   # 🔬 ML analysis
│   └── data/                                      # Processed datasets
│
├── 🌐 Dashboard Application
│   ├── app.py                                     # Main Streamlit app
│   ├── test_dashboard.py                          # Dashboard testing
│   └── requirements.txt                           # Dependencies
│
├── 🤖 ML Pipeline
│   ├── run_ml_pipeline.py                         # Automated training
│   ├── generate_v2_model.py                       # Model generation
│   └── models/                                    # Trained models
│
├── 📚 Documentation
│   ├── README.md                                  # Main documentation
│   ├── TECHNICAL_DOCUMENTATION.md                 # This file
│   ├── SYSTEM_ARCHITECTURE.md                     # Architecture details
│   ├── PROJECT_STATUS.md                          # Current status
│   └── FINAL_DELIVERABLE.md                       # Academic summary
│
└── 🔧 Configuration
    ├── .gitignore                                 # Git ignore rules
    └── requirements.txt                           # Python dependencies
```

## 🎯 **Performance Metrics**

### **ML Model Results:**
- **Linear Regression:** RMSE: 0.0277, R²: -0.977 (expected negative due to small dataset)
- **Random Forest:** RMSE: 0.0301, R²: -1.327
- **Best Model:** Linear Regression (simpler, more interpretable)

### **Feature Importance:**
1. **NDVI Mean:** 46.0% - Vegetation health is primary driver
2. **Occurrences:** 28.6% - Sampling effort affects results
3. **NDVI Std:** 25.4% - Vegetation variability matters
4. **Audio Signal:** 0.0% - Regional aggregation limits impact

### **Regional Analysis:**
- **Healthiest Region:** Periyar National Park (0.683 NDVI)
- **Most Stressed:** Western Ghats North (0.455 NDVI)
- **Most Variable:** Periyar National Park (0.035 std)

## 🚀 **Deployment**

### **Live Application:**
- **URL:** https://ecofusionai.streamlit.app/
- **Platform:** Streamlit Cloud
- **Auto-deployment:** GitHub integration
- **Monitoring:** Built-in analytics

### **Local Development:**
- **Framework:** Streamlit
- **Port:** Default 8501
- **Hot reload:** Automatic on file changes
- **Debug mode:** Available via --debug flag

## ⚠️ **Known Issues & Limitations**

### **Current Limitations:**
- Small temporal dataset (7 years NDVI, 16 years GBIF overlap)
- Audio signal aggregated regionally (lacks temporal consistency)
- Prototype-level system (decision-support, not production tool)
- Western Ghats geographic focus (not globally generalizable)
- Point sampling approach for NDVI (regional averages)

### **Future Enhancements:**
- Expanded temporal coverage (longer time series)
- Real-time satellite integration (automated NDVI updates)
- Species-specific audio analysis (individual species trends)
- Larger geographic scope (other biodiversity hotspots)
- Deep learning integration (CNN/RNN for audio and satellite data)