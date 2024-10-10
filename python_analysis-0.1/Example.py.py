import pandas as pd
from python_analysis.cleaning import fill_missing
from python_analysis.visualization import plot_histogram
from python_analysis.statistics import t_test


# Sample DataFrame for testing
df = pd.DataFrame({
    'age': [25, 30, None, 40, 50],
    'income': [50000, 60000, 55000, None, 65000]
})

# Data cleaning
df_clean = fill_missing(df)
print("Data after filling missing values:")
print(df_clean)

# Data visualization
plot_histogram(df_clean, 'age')

# Statistical analysis
t_stat, p_value = t_test(df_clean['age'].dropna(), df_clean['income'].dropna())
print(f"T-statistic: {t_stat}, P-value: {p_value}")
