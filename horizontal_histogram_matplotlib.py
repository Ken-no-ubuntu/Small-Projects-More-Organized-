import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.family'] = 'MS Gothic'
# Data for the bars
categories = ['ケアハウス(7.5-12.4)', '老人ホーム(10-14.4)','保健施設(8.8-15.1)','介護医療院(8.6-15.5)']
start_values = [7.5, 10,8.8, 8.6]
end_values = [12.4, 14.4,15.1,15.5]

# Calculate the width of each bar
widths = [end - start for start, end in zip(start_values, end_values)]

# Create a DataFrame
df = pd.DataFrame({'Category': categories, 'Start': start_values, 'Width': widths})

# Plot the floating bars using horizontal bar chart
plt.barh(y=df['Category'], width=df['Width'], left=df['Start'], color=sns.color_palette('viridis', len(df)))

# Customize the x-axis
plt.xlabel('月額料金（万円単位)')

# Add the starting and ending values of each bar to the plot
#for index, row in df.iterrows():
    #plt.text(row['Start'], index, f'{row["Start"]}', color='black', va='center')
    #plt.text(row['Start'] + row['Width'], index, f'{row["Start"] + row["Width"]}', color='black', va='center')

# Adjust the x-axis limits to ensure bars float
plt.xlim(0, max(end_values) + 5)

plt.ylabel('公的施設分類')
# Show the plot
plt.show()