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
# Remove duplicate rows

df = df.drop_duplicates()

print("Dataset shape after removing duplicates:")
print(df.shape)



# %%
#Inspect unique values

print("Products:")
print(df["Product"].unique())

print("\nCategories:")
print(df["Category"].unique())

print("\nPayment Methods:")
print(df["Payment_Method"].unique())

print("\nStatus:")
print(df["Status"].unique())


# %%
#Clean Product and Category names

# Remove extra spaces and standardize capitalization
df["Product"] = df["Product"].str.strip().str.title()
df["Category"] = df["Category"].str.strip().str.title()

# Fix category values with the same meaning
df["Category"] = df["Category"].replace({
    "Electronic": "Electronics"
})

print("Products after cleaning:")
print(df["Product"].unique())

print("\nCategories after cleaning:")
print(df["Category"].unique())


# %%
#Clean Quantity column

# Keep original values for inspection
print("Quantity values before conversion:")
print(df["Quantity"].unique())

# Convert Quantity to numeric
# Invalid values such as "4a" become NaN
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

print("\nQuantity values after conversion:")
print(df["Quantity"].unique())

print("\nMissing/invalid Quantity values:")
print(df[df["Quantity"].isna()])


# %%
#Handle negative Quantity

print("Negative Quantity rows:")
print(df[df["Quantity"] < 0])

# Negative quantity is invalid, so convert it to missing value
df.loc[df["Quantity"] < 0, "Quantity"] = pd.NA

print("\nNegative quantities after cleaning:")
print((df["Quantity"] < 0).sum())



# %%
# Clean Price column

print("Price values before cleaning:")
print(df["Price"].unique())

# Convert Price to string
df["Price"] = df["Price"].astype("string")

# Remove dollar sign
df["Price"] = df["Price"].str.replace("$", "", regex=False)

# Convert "four hundred" to 400
df["Price"] = df["Price"].replace({
    "four hundred": "400"
})

# Convert to numeric
# Invalid values such as "abd" become NaN
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("\nPrice values after cleaning:")
print(df["Price"].unique())

print("\nMissing/invalid Price values:")
print(df[df["Price"].isna()])


# %%
#Handle negative Price

print("Negative Price rows:")
print(df[df["Price"] < 0])

# Negative prices are invalid
df.loc[df["Price"] < 0, "Price"] = pd.NA

print("\nNumber of negative prices after cleaning:")
print((df["Price"] < 0).sum())


# %%
#Handle missing Category values

print("Rows with missing Category:")
print(df[df["Category"].isna()][["Product", "Category"]])

# %%
# Product-to-category mapping
product_category_map = (
    df.dropna(subset=["Category"])
      .drop_duplicates(subset=["Product"])
      .set_index("Product")["Category"]
      .to_dict()
)

# Fill missing categories using the product mapping
df["Category"] = df["Category"].fillna(
    df["Product"].map(product_category_map)
)

# If any are still missing
df["Category"] = df["Category"].fillna("Unknown")

print("\nMissing Category values after cleaning:")
print(df["Category"].isna().sum())



# %%
#  Handle missing Quantity and Price

quantity_median = df["Quantity"].median()
price_median = df["Price"].median()

df["Quantity"] = df["Quantity"].fillna(quantity_median)
df["Price"] = df["Price"].fillna(price_median)

print("Missing Quantity:", df["Quantity"].isna().sum())
print("Missing Price:", df["Price"].isna().sum())

# %%
#Clean Order_Date

print("Order Date before conversion:")
print(df["Order_Date"].unique())

# Convert dates
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

print("\nInvalid/missing dates:")
print(df[df["Order_Date"].isna()])


# %%
#  Remove invalid dates

print("Rows before removing invalid dates:", len(df))

df = df.dropna(subset=["Order_Date"])

print("Rows after removing invalid dates:", len(df))

# %%
# Recalculate Total

df["Total"] = df["Quantity"] * df["Price"]

print(df[["Quantity", "Price", "Total"]].head())




# %%
# FINAL CLEANING: Remove duplicates created after cleaning

print("Duplicates before final removal:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicates after final removal:")
print(df.duplicated().sum())

print("\nFinal dataset shape:")
print(df.shape)

# %%
# Final data quality check

print("Final dataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nNegative Quantity:")
print((df["Quantity"] < 0).sum())

print("\nNegative Price:")
print((df["Price"] < 0).sum())




# %%
# Saving final cleaned dataset

output_path = "../data/cleaned/cleaned_ecommerce_sales_data.csv"

df.to_csv(output_path, index=False)

print(f"Final cleaned dataset saved to: {output_path}")
# %%
