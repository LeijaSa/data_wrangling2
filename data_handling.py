
import pandas as pd


def load_data_to_dataframe(file_path):
    try:
        df=pd.read_csv(file_path)
        return df
    except (FileNotFoundError, pd.errors.ParserError):
        print("Error loading file. Check the file path and format.")
        return None

def read_ten_lines(df):
    return df.head(10)

def get_info(df):
    print("Dataframe shape:", df.shape)
    print("Dataframe columns:", df.columns)
    print("Dataframe info:")
    print(df.info())

def clean_column_names(df):
    """Removes leading/trailing whitespace from column names."""
    df.rename(columns=lambda x:x.strip(),inplace=True)
    return df

def remove_duplicates(df):
    """Removes duplicates from column order_id."""
    df.drop_duplicates(subset='order_id',inplace=True) 
    return df

def ensure_data_types(df):
    """Converts numeric columns to numeric data type. Handles errors gracefully."""
    numeric_columns=['order_id', 'product_id', 'quantity', 'unit_price', 'customer_id']
    df.loc[:, numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    return df

def drop_null_columns(df):
    """Drops rows with missing numeric values."""
    df.dropna(subset=['unit_price', 'quantity','product_id','customer_id','product_category'],inplace=True)
    return df

def ensure_valid_date(df):
    try:
      df['order_date'] =pd.to_datetime(df['order_date'])
    except ValueError:
        print("Invalid date format detected. Assuming 'YYYY-MM-DD' format.")
    return df

def handle_floats_to_ints(df):
    df['product_id']=df['product_id'].astype(int)
    df['customer_id']=df['customer_id'].astype(int)
    df['quantity']=df['quantity'].astype(int)
    return df

def create_new_column(df):
    df['total_price']=df['quantity']*df['unit_price']
    return df

def extract_features_from_order_date(df):   
    # Extract day of week, month and year from 'order_date' column and add new columns to the dataframe
    df['day']=df[ "order_date"].dt.day
    df['month']=df[ "order_date"].dt.month
    df['year']= df['order_date'].dt.year
    return df

def groupby(df):
    df_copy = df.copy()
    df_grouped = df_copy.groupby('product_category').agg({'total_price':'sum','quantity': 'mean'})
    return df_grouped

def get_summary_table(df):
    df_copy = df.copy()
    table=pd.pivot_table(df_copy, index='product_category',columns='month',values='total_price', aggfunc='sum')
    return table

def show_prices_as_percentage(df):
    df_copy = df.copy()
    average_price=df_copy['unit_price'].mean()
    df_copy['unit_price']=(df_copy['unit_price']/average_price*100).round(1)
    return df_copy
    
def main():
    file_path="ecommerce_sales.csv"
    df=load_data_to_dataframe(file_path)
    if df is not None:
        df=clean_column_names(df)
        df=remove_duplicates(df)
        df=ensure_data_types(df)
        df=drop_null_columns(df)
        df=ensure_valid_date(df)
        df=handle_floats_to_ints(df)
        df=create_new_column(df)
        df=extract_features_from_order_date(df)
        #print(df)

        df_grouped=groupby(df)
        print(df_grouped)

        df_summary=get_summary_table(df)
        print(df_summary)

        df=show_prices_as_percentage(df)
        print(df)
        


if __name__ == "__main__":
    main()