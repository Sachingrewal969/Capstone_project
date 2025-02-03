import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text_data = pickle.load(open('datasets/feature_text.pkl','rb'))

group_df = new_df.groupby('sector').mean(numeric_only=True)[['price','price_per_sqft','built_up_area','latitude','longitude']]

st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)

# *************
st.header('Features Wordcloud')
# Sector dropdown for word cloud
selected_sector = st.selectbox("Select Sector for Wordcloud", new_df['sector'].unique())

# Filter feature text for the selected sector
if 'features' in new_df.columns:
    feature_text = new_df[new_df['sector'] == selected_sector]['features'].dropna().str.cat(sep=' ')
else:
    feature_text = feature_text_data

wordcloud = WordCloud(
    width=800, height=800,
    background_color='black',
    stopwords=set(['s']), 
    min_font_size=10
).generate(feature_text)

# Create a figure and plot the word cloud
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig)

st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)


st.header('Histogram of Property Prices')

fig_hist = px.histogram(new_df, x='price', nbins=50, 
                        title='Distribution of Property Prices', 
                        labels={'price': 'Property Price'})
st.plotly_chart(fig_hist, use_container_width=True)


st.header('Correlation Heatmap')

# Ensure numeric columns
new_df['price'] = pd.to_numeric(new_df['price'], errors='coerce')
new_df['price_per_sqft'] = pd.to_numeric(new_df['price_per_sqft'], errors='coerce')

# Select only numeric columns for correlation
numeric_df = new_df.select_dtypes(include=['number'])

# Compute the correlation matrix
correlation = numeric_df.corr()

fig_corr = px.imshow(correlation, 
                     color_continuous_scale='Blues', 
                     title='Correlation Heatmap',
                     width = 1200,
                     height = 600)
st.plotly_chart(fig_corr, use_container_width=True)


st.header('Average Prices by Property Type')

average_price = new_df.groupby('property_type')['price'].mean().reset_index()

fig_bar = px.bar(average_price, x='property_type', y='price', 
                 title='Average Property Prices by Type',
                 labels={'price': 'Average Price'})
st.plotly_chart(fig_bar, use_container_width=True)
