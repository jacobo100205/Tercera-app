import pandas as pd 
import geopandas as pgd
import matplotlib.pyplot as plt 
import streamlit as st 

st.title("Esto es una app") 

year = st.slelectbox("Seleccione un año",[2024,2023,2022])

if year == 2024:
    df_m = gpd.read_parquet("hombres24.parquet")
    df_f = gpd.read_parquet("mujeres24.parquet")
elif year == 2023:
    df_m = gpd.read_parquet("hombres23.parquet")
    df_f = gpd.read_parquet("mujeres23.parquet")
else year == 2022:
    df_m  = gpd.read_parquet("hombres22.parquet")
    df_f = gpd.read_parquet("mujeres22.parquet")


df_m = pgd.read_file('hombres.geojson')
df_f = pgd.read_file('mujeres.geojson')

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
df_m.plot(column='FT', ax=ax[0], legend=True, vmin = 0.2, vmax=1)
df_f.plot(column='FT', ax=ax[1], legend=True, vmin = 0.2, vmax=1)

ax[0].set_title('TGP - Hombres')
ax[1].set_title('TGP - Mujeres')
ax[0].axis('off')
ax[1].axis('off')

st.pyplot(fig)