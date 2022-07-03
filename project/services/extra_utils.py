import pandas as pd


file_name = 'BD_loan.feather'
df = pd.read_feather(file_name)
print(df.columns)
# print(df.shape)  # (1176120, 27) 
print(df.info())  # memory usage --> 242.3MB

df_to_db = df.sample(n=10000, random_state=1)

print(df_to_db.head())
print(df_to_db.info())  # memory usage --> 2.1MB
print(df_to_db.loan_status.unique())
df_to_db['loan_status'] = df_to_db['loan_status'].replace({
    0: 'Charged Off',
    1: 'Fully Paid',
})
print(df_to_db.head())
df_to_db.reset_index().to_feather('mini_db.feather')
