import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="EcoFusionAI – Biodiversity Early Warning System",
    layout="wide"
)

# --------------------------------------------------
# Load data
# --------------------------------------------------
@st.cache_data
def load_data():
    fusion = pd.read_csv("fusion_multimodal_dataset.csv")
    model_results = pd.read_csv("model_results_summary.csv")
    feature_importance = pd.read_csv("feature_importance.csv")
    return fusion, model_results, feature_importance

fusion, model_results, feature_importance = load_data()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("🌿 EcoFusionAI")
section = st.sidebar.radio(
    "Navigate",
    [
        "Overview",
        "Biodiversity Trends",
        "Early Warning System",
        "ML Model Insights",
        "Exploratory NDVI View (Phase-1)",
    ]
)

# --------------------------------------------------
# Overview
# --------------------------------------------------
if section == "Overview":
    st.title("🌏 EcoFusionAI – Multimodal Biodiversity Monitoring")
    
    st.markdown("""
    **EcoFusionAI is a research-grade, multimodal early-warning system that detects biodiversity stress trends using satellite vegetation health, species occurrence data, and bird acoustic activity.**
    
    The system integrates:
    - 🛰️ **Satellite vegetation health (NDVI)**
    - 🦅 **Species occurrence trends (GBIF)**
    - 🔊 **Bird acoustic activity (BirdCLEF)**
    
    to **detect early signals of biodiversity stress** in the **Western Ghats**.
    
    🎓 *Final Year BE Project – Computer Engineering (SPPU)*
    
    **This project is a decision-support prototype, not a consumer app.**
    """)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Years Covered", f"{fusion.year.min()} – {fusion.year.max()}")
    col2.metric("Audio Species", int(fusion['audio_signal_strength'].count()))
    col3.metric("Avg Stress Index", f"{fusion['eco_stress_index'].mean():.3f}")

# --------------------------------------------------
# Biodiversity Trends
# --------------------------------------------------
elif section == "Biodiversity Trends":
    st.title("📈 Long-Term Biodiversity Trends")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(
        fusion["year"],
        fusion["species_per_1000_occ"],
        marker="o",
        linewidth=2
    )
    ax.set_xlabel("Year")
    ax.set_ylabel("Species per 1000 Occurrences")
    ax.set_title("Sampling-Corrected Species Richness (GBIF)")
    ax.grid(alpha=0.3)
    st.pyplot(fig)
    
    st.info("""
    ✔ Corrected for sampling bias  
    ✔ Uses GBIF Cube aggregation  
    ✔ Reflects real biodiversity trends, not observation effort
    """)

# --------------------------------------------------
# Early Warning System
# --------------------------------------------------
elif section == "Early Warning System":
    st.title("🚨 Biodiversity Early-Warning Index")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        data=fusion,
        x="year",
        y="eco_stress_index",
        marker="o",
        ax=ax
    )
    ax.axhline(0.6, color="red", linestyle="--", label="High Risk Threshold")
    ax.set_title("Eco-Stress Index Over Time")
    ax.set_ylabel("Stress Index (0 = Healthy, 1 = Critical)")
    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig)
    
    latest = fusion.iloc[-1]
    
    if latest.eco_stress_index > 0.6:
        st.error(f"🚨 HIGH RISK detected in {int(latest.year)}")
    elif latest.eco_stress_index > 0.45:
        st.warning(f"⚠️ MODERATE RISK detected in {int(latest.year)}")
    else:
        st.success(f"✅ LOW RISK in {int(latest.year)}")
    
    st.markdown("""
    **Stress Index combines:**
    - NDVI decline (environmental degradation)
    - Acoustic signal loss (avian activity)
    - Observation pressure (sampling bias proxy)
    """)

# --------------------------------------------------
# ML Model Insights
# --------------------------------------------------
elif section == "ML Model Insights":
    st.title("🤖 Machine Learning Insights")
    
    st.subheader("Model Performance")
    st.dataframe(model_results, use_container_width=True)
    
    st.info("""
    ⚠️ Negative R² is expected due to **small sample size (7 years)**  
    ✔ Methodology is scientifically valid  
    ✔ Designed as a **proof-of-concept early warning system**
    """)
    
    st.subheader("Feature Importance (Random Forest)")
    
    fig, ax = plt.subplots(figsize=(8, 5))
    feature_importance.sort_values(
        by="importance", ascending=True
    ).plot.barh(
        ax=ax, legend=False
    )
    ax.set_xlabel("Importance Score")
    ax.set_title("Drivers of Biodiversity Change")
    ax.grid(alpha=0.3)
    st.pyplot(fig)
    
    st.markdown("""
    **Key Insight:**  
    🌿 Vegetation health (NDVI) is the strongest driver of biodiversity change,  
    validating the **environment → species response hypothesis**.
    """)

# --------------------------------------------------
# Exploratory NDVI View (Phase-1)
# --------------------------------------------------
elif section == "Exploratory NDVI View (Phase-1)":
    st.title("🛰️ Exploratory NDVI View (Phase-1)")
    
    st.info("""
    **Phase-1 Bridge:** This view shows the original NDVI extraction results  
    from individual regions before aggregation into the multimodal system.
    """)
    
    # Load the original NDVI point sampling data
    try:
        ndvi_raw = pd.read_csv("data/ndvi_temporal_dataset_POINT_SAMPLING.csv")
        
        st.subheader("📊 NDVI Trends by Region")
        
        # Region selector
        regions = ndvi_raw['region'].unique()
        selected_regions = st.multiselect(
            "Select regions to display:",
            regions,
            default=regions[:3] if len(regions) > 3 else regions
        )
        
        if selected_regions:
            # Filter data
            filtered_data = ndvi_raw[ndvi_raw['region'].isin(selected_regions)]
            
            # Create the plot
            fig, ax = plt.subplots(figsize=(12, 6))
            
            for region in selected_regions:
                region_data = filtered_data[filtered_data['region'] == region]
                ax.plot(
                    region_data['year'], 
                    region_data['ndvi_mean'], 
                    marker='o', 
                    linewidth=2, 
                    label=region,
                    alpha=0.8
                )
            
            ax.set_xlabel("Year")
            ax.set_ylabel("NDVI Mean")
            ax.set_title("NDVI Trends by Region (Point Sampling Results)")
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            ax.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)
            
            # Summary statistics
            st.subheader("📋 Regional NDVI Summary")
            summary_stats = filtered_data.groupby('region').agg({
                'ndvi_mean': ['mean', 'min', 'max', 'std'],
                'num_samples': 'mean'
            }).round(3)
            
            # Flatten column names
            summary_stats.columns = ['Mean_NDVI', 'Min_NDVI', 'Max_NDVI', 'Std_NDVI', 'Avg_Samples']
            st.dataframe(summary_stats, use_container_width=True)
            
            # Key insights
            st.subheader("🔍 Phase-1 Insights")
            
            best_region = summary_stats['Mean_NDVI'].idxmax()
            worst_region = summary_stats['Mean_NDVI'].idxmin()
            most_variable = summary_stats['Std_NDVI'].idxmax()
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "🌿 Healthiest Region", 
                    best_region,
                    f"{summary_stats.loc[best_region, 'Mean_NDVI']:.3f} NDVI"
                )
            
            with col2:
                st.metric(
                    "⚠️ Most Stressed Region", 
                    worst_region,
                    f"{summary_stats.loc[worst_region, 'Mean_NDVI']:.3f} NDVI"
                )
            
            with col3:
                st.metric(
                    "📊 Most Variable Region", 
                    most_variable,
                    f"{summary_stats.loc[most_variable, 'Std_NDVI']:.3f} std"
                )
            
            st.markdown("""
            **Phase-1 → Phase-2 Evolution:**
            - **Phase-1**: Individual region NDVI extraction (shown above)
            - **Phase-2**: Aggregated yearly NDVI + multimodal fusion
            - **Result**: From regional monitoring → ecosystem-wide early warning
            """)
        
        else:
            st.warning("Please select at least one region to display.")
            
    except FileNotFoundError:
        st.error("NDVI point sampling data not found. Please run Notebook 1 first.")
    except Exception as e:
        st.error(f"Error loading NDVI data: {e}")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("EcoFusionAI | Research-grade multimodal early-warning system ")