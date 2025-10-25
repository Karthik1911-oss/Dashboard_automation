import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10


def visualize_4_dashboard(df: pd.DataFrame,
                          numeric_col: str,
                          categorical_col: str,
                          datetime_col: str = None):
    """
    Generate 4 key visualizations in 2x2 grid:
    1. Histogram
    2. Box Plot
    3. Bar Chart
    4. Pie Chart
    Optional: Line Plot if datetime + numeric column provided
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes = axes.flatten()

    # 1. Histogram
    axes[0].hist(df[numeric_col].dropna(), bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    axes[0].set_title(f'Histogram of {numeric_col}')
    axes[0].set_xlabel(numeric_col)
    axes[0].set_ylabel('Frequency')

    # Add value labels for histogram
    counts, bins = np.histogram(df[numeric_col].dropna(), bins=30)
    for i in range(len(bins)-1):
        axes[0].text(bins[i] + (bins[i+1]-bins[i])/2, counts[i]+0.5, str(counts[i]),
                     ha='center', va='bottom', fontsize=8, rotation=90)

    # 2. Boxplot
    axes[1].boxplot(df[numeric_col].dropna())
    axes[1].set_title(f'Box Plot of {numeric_col}')
    axes[1].set_ylabel('Values')

    # 3. Bar Chart
    value_counts = df[categorical_col].value_counts().head(10)
    bars = axes[2].bar(value_counts.index, value_counts.values, color='coral', edgecolor='black')
    axes[2].set_title(f'Bar Chart of {categorical_col}')
    axes[2].set_xlabel(categorical_col)
    axes[2].set_ylabel('Count')
    axes[2].tick_params(axis='x', rotation=45)

    # Add value labels for bar chart
    for bar in bars:
        height = bar.get_height()
        axes[2].text(bar.get_x() + bar.get_width()/2, height + 0.5, f'{int(height)}',
                     ha='center', va='bottom', fontsize=9)

    # 4. Pie Chart
    pie_counts = df[categorical_col].value_counts().head(8)
    axes[3].pie(pie_counts.values, labels=pie_counts.index, autopct='%1.1f%%', startangle=90)
    axes[3].set_title(f'Pie Chart of {categorical_col}')

    plt.tight_layout()
    plt.show()

    # Optional: Line Plot if datetime column provided
    if datetime_col:
        plt.figure(figsize=(12, 5))
        df_sorted = df[[datetime_col, numeric_col]].dropna().sort_values(datetime_col)
        plt.plot(df_sorted[datetime_col], df_sorted[numeric_col], marker='o', linewidth=2, color='teal')
        plt.title(f'{numeric_col} over {datetime_col}')
        plt.xlabel(datetime_col)
        plt.ylabel(numeric_col)
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)

        # Add value labels to line plot
        for x, y in zip(df_sorted[datetime_col], df_sorted[numeric_col]):
            plt.text(x, y, f'{y:.0f}', fontsize=8, ha='center', va='bottom', rotation=45)

        plt.tight_layout()
        plt.show()


def main():
    # Load your dataset
    file_path = r"C:\Users\KARTHIK RAJ\Documents\Outside Participant 2023-24.xlsx"
    df = pd.read_excel(file_path)

    # Specify the columns for visualization
    numeric_col = 'Age'           # Replace with your numeric column
    categorical_col = 'Gender'    # Replace with your categorical column
    datetime_col = 'EnrollmentDate'  # Optional, replace with your datetime column if exists

    # Call the visualization function
    visualize_4_dashboard(df, numeric_col, categorical_col, datetime_col)



if __name__ == "__main__":
    main()
