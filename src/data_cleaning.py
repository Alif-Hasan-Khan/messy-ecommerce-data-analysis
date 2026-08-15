# %%
import pandas as pd

df = pd.read_csv("../data/raw/messy_ecommerce_sales_data.csv")

print(df.head())



# %%
#Basic dataset information

print("Dataset shape:")
print(df.shape)

print("\nDataset information:")
df.info()


# %%
# Check missing values

print("Missing values:")
print(df.isnull().sum())



# %%
# Clean column names

df.columns = df.columns.str.strip()

print("Cleaned column names:")
print(df.columns.tolist())



# %%
# Check duplicate rows

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)

print("\nDuplicate row:")
print(df[df.duplicated()])



# %%
