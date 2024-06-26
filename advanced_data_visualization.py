# -*- coding: utf-8 -*-
"""Advanced Data Visualization

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sqTGjyA0cf-NQLZVbpB-TdkwqVT0Ht5p

**Colour Coding**

Colour coding is a method of using different colours to represent various categories, values, or data ranges in a visualization. It helps in distinguishing elements quickly, making patterns and trends more visible, and improving the overall readability of the chart.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

ev_data = pd.read_csv('Electric_Vehicle_Population_Data.csv')

ev_make_distribution = ev_data['Make'].value_counts().head(10)  # Limiting to top 10 for clarity
# selecting the top 3 manufacturers based on the number of vehicles registered
top_3_makes = ev_make_distribution.head(3).index

# filtering the dataset for these top manufacturers
top_makes_data = ev_data[ev_data['Make'].isin(top_3_makes)]

# analyzing the popularity of EV models within these top manufacturers
ev_model_distribution_top_makes = top_makes_data.groupby(['Make', 'Model']).size().sort_values(ascending=False).reset_index(name='Number of Vehicles')

# visualizing the top 10 models across these manufacturers for clarity
top_models = ev_model_distribution_top_makes.head(10)

plt.figure(figsize=(12, 8))
sns.barplot(x='Number of Vehicles', y='Model', hue='Make', data=top_models, palette="viridis")
plt.title('Top Models in Top 3 Makes by EV Registrations')
plt.xlabel('Number of Vehicles Registered')
plt.ylabel('Model')
plt.legend(title='Make', loc='center right')
plt.tight_layout()
plt.show()

"""In the above graph, colour coding is employed to distinguish between the different manufacturers (makes) for the top electric vehicle models. Here’s how it is applied:

**Hue Parameter:** The hue parameter in the sns.barplot() function is set to the ‘Make’ column. It tells Seaborn to use different colours for each make.

**Palette:** The ‘viridis’ palette is used, which provides a perceptually uniform colour scale. It means each make is represented by a unique colour, enhancing the visual distinction between them.

**Legend:** A legend is automatically added by Seaborn, mapping each colour used in the bar plot to the corresponding make. It helps in identifying which colour represents which manufacturer.

**Line Styles**

Line styles can be used to differentiate between multiple datasets or trends shown on the same plot. Dashed, dotted, and solid lines are common styles that help users distinguish between different series in line plots.
"""

# filtering the data for BEV and PHEV only and excluding extreme outliers (electric range == 0)
filtered_ev_data = ev_data[(ev_data['Electric Range'] > 0) & (ev_data['Electric Vehicle Type'].isin(['Battery Electric Vehicle (BEV)', 'Plug-in Hybrid Electric Vehicle (PHEV)']))]

# grouping the data by model year and ev type to get the average electric range
yearly_avg_range = filtered_ev_data.groupby(['Model Year', 'Electric Vehicle Type']).agg({'Electric Range': 'mean'}).reset_index()

# setting up the plot
plt.figure(figsize=(14, 7))

# plotting BEV
bev_data = yearly_avg_range[yearly_avg_range['Electric Vehicle Type'] == 'Battery Electric Vehicle (BEV)']
plt.plot(bev_data['Model Year'], bev_data['Electric Range'], linestyle='-', marker='o', label='BEV (Battery Electric Vehicle)')

# plotting PHEV
phev_data = yearly_avg_range[yearly_avg_range['Electric Vehicle Type'] == 'Plug-in Hybrid Electric Vehicle (PHEV)']
plt.plot(phev_data['Model Year'], phev_data['Electric Range'], linestyle='--', marker='x', label='PHEV (Plug-in Hybrid Electric Vehicle)')

plt.title('Average Electric Range by Model Year for BEV and PHEV')
plt.xlabel('Model Year')
plt.ylabel('Average Electric Range (miles)')
plt.legend()
plt.grid(True)

plt.show()

"""In the above graph, line styles are used to distinguish between two different categories of electric vehicles: Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs). Here’s a breakdown of how line styles are employed:

1.BEVs are represented using a solid line (linestyle=’-‘) combined with circle markers (marker=’o’). This style provides a continuous, clear visualization of the BEV data points across model years.

2.PHEVs are depicted with a dashed line (linestyle=’–‘) and cross markers (marker=’x’). The dashed line visually differentiates PHEVs from BEVs, helping to quickly identify and contrast the trends between these two vehicle types.

**Conditional Formatting**

Conditional formatting changes the formatting of an item based on its value or some other criterion. This technique is often seen in heatmaps or tables where cell colours change according to the data value, helping to highlight anomalies, trends, or specific conditions.
"""

import numpy as np

# filtering out entries with zero MSRP or zero electric range for better clarity in visualization
valid_data = ev_data[(ev_data['Base MSRP'] > 0) & (ev_data['Electric Range'] > 0)]

# creating the scatter plot with conditional formatting based on electric range
plt.figure(figsize=(10, 6))
scatter = plt.scatter(valid_data['Model Year'], valid_data['Base MSRP'], c=valid_data['Electric Range'], cmap='viridis', alpha=0.6)

# adding a colorbar to show the electric range
colorbar = plt.colorbar(scatter)
colorbar.set_label('Electric Range (miles)')

# setting titles and labels
plt.title('Model Year vs. Base MSRP Colored by Electric Range')
plt.xlabel('Model Year')
plt.ylabel('Base MSRP ($)')

plt.grid(True)
plt.show()

"""In the above graph, conditional formatting is applied in the context of a scatter plot to visually represent variations in the electric range of vehicles based on their colour intensity. Here’s a concise explanation of how conditional formatting is used:

Colour Mapping: The electric range of each vehicle is used as the basis for the colour of each scatter plot point. The c parameter in plt.scatter() is set to the ‘Electric Range’ column, which assigns a colour to each point corresponding to its electric range value.

**Colour Palette:** The ‘viridis’ colourmap is used (cmap=’viridis’), which provides a range of colours from dark to light. This colour map is particularly effective because it offers good colour differentiation and is perceptually uniform, making it easier to interpret the differences in electric range visually.

**Colorbar as a Legend:** A colour bar is added to the plot, which acts as a legend to map the colour gradients back to actual electric range values. It helps viewers understand what electric range values correspond to the colours in the plot.

**Visual Differentiation:** The use of colours conditioned on data values allows for immediate visual differentiation of data points based on their electric range. This format helps highlight trends or outliers in the relationship between the model year, MSRP, and electric range of the vehicles.

**Subplots**

Subplots are used to create multiple plots in the same figure. It is useful for comparing different datasets side by side or showing different aspects of the same data.
"""

# setting up the figure for subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# histogram of electric range
sns.histplot(filtered_ev_data['Electric Range'], bins=30, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution of Electric Range')
axes[0].set_xlabel('Electric Range (miles)')
axes[0].set_ylabel('Frequency')

# histogram of base MSRP
msrp_data = ev_data[ev_data['Base MSRP'] > 0]
sns.histplot(msrp_data['Base MSRP'], bins=30, ax=axes[1], color='salmon')
axes[1].set_title('Distribution of Base MSRP')
axes[1].set_xlabel('Base MSRP ($)')
axes[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

"""In the above graph, subplots are utilized to create multiple separate plots within a single figure, allowing for a side-by-side comparison of different distributions. Here’s how subplots are used in this context:

1.plt.subplots(nrows=1, ncols=2, figsize=(14, 6)) set up a figure with a single row containing two columns, which means there will be two plots aligned horizontally. The figsize parameter specifies the size of the entire figure.

2.The first subplot, accessed via axes[0], is used for plotting the histogram of the ‘Electric Range’. Specific aspects like the title, x-label, and y-label are set to indicate what this subplot represents.

3.The second subplot, accessed via axes[1], displays the histogram of the ‘Base MSRP’. Again, appropriate labels and a title are set to differentiate it from the first plot and clarify what is being shown.1.

**Interactive Elements**

Interactive elements like tooltips, sliders, and buttons allow users to interact with the data visually. It can involve filtering data, changing what is displayed, or simply displaying more detailed information about a particular data point when hovered over or clicked.

Interactive elements can be applied using the plotly library in Python.
"""

import plotly.express as px

# filtering data to improve visualization clarity
interactive_data = msrp_data[msrp_data['Electric Range'] > 0]

# creating an interactive scatter plot
fig = px.scatter(interactive_data, x='Electric Range', y='Base MSRP', color='Make', hover_data=['Model', 'Model Year', 'Electric Vehicle Type'],
                 title='Electric Range vs. Base MSRP by Make')
fig.update_layout(xaxis_title='Electric Range (miles)', yaxis_title='Base MSRP ($)', coloraxis_colorbar=dict(title='Make'))
fig.show()

