# -------------------------------------- Import Library ------------------------------

## Read Data and Preprocessing Data
import pandas as pd

## Visualization
import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt

## Dashboard 
import streamlit as st 

# ------------------------------ CONFIG ------------------------------
st.set_page_config(
    page_title="Dashboard Analisis Atribut Fisik Kepiting",
    page_icon="🦀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------------- Read dataset ------------------------------
df = pd.read_pickle("data_crab_clean.pkl")
df2 = pd.read_pickle("data_crab_raw.pkl")

# -------------------------------------- Membuat Sidebar --------------------
with st.sidebar:
    # Menambahkan Logo Pribadi
    st.image("blue-crab.png")
    st.write("""
             Dashboard Analisis Atribut Fisik Kepiting, merupakan alat yang menampilkan hasil analisis 
             berdasarkan data kepiting yang ditemukan di Boston dengan memvisualisasikannya ke dalam bentuk diagram. 
             """)
    st.caption('Copyright © Raihan H. 2024')

# -------------------------------------- ROW 1 --------------------
st.write("# Dashboard Analisis Atribut Fisik Kepiting")
st.write("""
         Analisis ini menggunakan bahasa pemrograman Python dan visualisasi 
         interaktif (Plotly Express). Data yang digunakan adalah data 
         kepiting di area Boston, Massachusetts, Amerika Serikat. Data ini disertakan dengan atribut fisik 
        kepiting berasal dari sumber https://www.kaggle.com/datasets/sidhus/crab-age-prediction?resource=download.
         """)
with st.expander("Klik untuk melihat detail data (raw)!"):
    st.write("Data Mentah Atribut Fisik Kepiting",df2)    

with st.expander("Klik untuk melihat detail data (clean)!"):
    st.write("Data Bersih Atribut Fisik Kepiting",df)    


# -------------------------------------- ROW 2 --------------------

st.write("### 1. Bagaimana distribusi data kepiting di Boston?")

# --------------- A. Persiapan Data

choices1 = st.radio("""Pilih salah satu atribut!""",
         ["Age","Height","Length","Diameter", "Gender"])

# --------------- B. Visualisasi

if(choices1 == "Age"):
    fig_hist = px.histogram(df,
        x="Age",
        title="Histogram Jumlah Kepiting berdasarkan Umur (bulan)",
    )

elif (choices1 == "Height"):    
    fig_hist = px.histogram(df,
        x="Height",
        title="Histogram Jumlah Kepiting berdasarkan Tinggi",
    )

elif (choices1 == "Length"):
    fig_hist = px.histogram(df,
        x="Length",
        title="Histogram Jumlah Kepiting berdasarkan Panjang",
    )

elif (choices1 == "Diameter"):
    fig_hist = px.histogram(df,
        x="Diameter",
        title="Histogram Jumlah Kepiting berdasarkan Diameter",
    )

elif (choices1 == "Gender"):
    fig_hist = px.histogram(df,
        x="Gender",
        title="Histogram Jumlah Kepiting berdasarkan Gender",
    )

fig_hist.update_layout(
     {        
        'plot_bgcolor': 'rgba(0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0)'
    },
    margin=dict(l=10, r=10, t=50, b=50)
    )

st.plotly_chart(fig_hist)

# -------------------------------------- ROW 3 --------------------

st.write("### 2. Bagaimana sebaran, rentang, dan outlier atribut berat (Weight) kepiting yang diperoleh?")

# --------------- A. Persiapan Data

choices2 = st.radio("""Pilih salah satu atribut!""",
         ["Weight", "Shell Weight", "Shucked Weight", "Viscera Weight"])


# --------------- B. Visualisasi

if(choices2 == "Weight"):
    fig_bxplot = px.box(
        df,
        y = "Weight",
        points="all",
        title="Boxplot Berat Kepiting",
    )

elif (choices2 == "Shell Weight"):    
    fig_bxplot = px.box(
        df,
        y = "Shell Weight",        
        points="all",
        title="Boxplot Berat Cangkang Kepiting",
    )

elif (choices2 == "Shucked Weight"):    
    fig_bxplot = px.box(
        df,
        y = "Shucked Weight",        
        points="all",
        title="Boxplot Berat Kepiting Tanpa Cangkang",
    )

elif (choices2 == "Viscera Weight"):    
    fig_bxplot = px.box(
        df,
        y = "Viscera Weight",
        points="all",
        title="Boxplot Kepiting dengan berat pembungkus organ perut di dalam tubuh",
    )

fig_bxplot.update_layout(
        {        
        'plot_bgcolor': 'rgba(0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0)'
    },
    margin=dict(l=10, r=10, t=50, b=50)
    )
st.plotly_chart(fig_bxplot)


# -------------------------------------- ROW 4 --------------------

st.write("### 3. Bagaimana hubungan antara atribut kepiting (Length, Diameter, Weight)?")

st.write("""Untuk melihat hubungan atribut data dapat menggunakan Scatter Plot yang membandingkan antara dua nilai numerik, 
         dalam hal ini Length, Diameter, dan Weight yang dimiliki kepiting. Hasil analisis dapat dilihat pada gambar grafik dibawah yang menunjukkan adanya hubungan positif dengan posisi titik cenderung mengarah ke atas kanan.""")

# --------------- A. Persiapan Data

fig, (ax_ld, ax_wd, ax_lw) = plt.subplots(
    nrows=1,
    ncols=3,
    figsize=(6,4)
)

ax_ld = sns.scatterplot(
    data=df,
    x="Length",
    y="Diameter",
    ax=ax_ld
)

ax_wd = sns.scatterplot(
    data=df,
    x="Weight",
    y="Diameter",
    ax=ax_wd
)

ax_lw = sns.scatterplot(
    data=df,
    x="Length",
    y="Weight",
    ax=ax_lw
)

ax_ld.set_title("Diameter vs Length")
ax_ld.grid(True)
ax_wd.set_title("Diameter vs Weight")
ax_wd.grid(True)
ax_lw.set_title("Weight vs Length")
ax_lw.grid(True)

# --------------- B. Visualisasi

fig.set_tight_layout(True)
st.pyplot(fig)

# -------------------------------------- ROW 5 --------------------

st.write("### 4. Bagaimana hubungan seluruh atribut kepiting?")

st.write("""Untuk melihat hubungan seluruh atribut data pada dataset kepiting digunakan Pair Plot yang membandingkan seluruh nilai atribut numerik.
         Hasil analisis dapat dilihat pada gambar grafik dibawah yang menunjukkan keseluruhan hubungan antar atribut yang diperoleh.""")

# --------------- A. Visualisasi

sns.set_palette("bright")
pairplot = sns.pairplot(df, hue="Gender")

st.pyplot(pairplot)
