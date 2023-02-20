import pandas as pd
from django.contrib.auth.hashers import make_password
from gupms.models import Account
from django.core.exceptions import ValidationError
def import_accounts(filepath):
    df = pd.read_excel(filepath)
    for index, row in df.iterrows():
        if pd.isna(row['name']) or pd.isna(row['email']) or pd.isna(row['password']):
            print(f'Skipping row {index + 2}: missing data')
            continue
        password = make_password(row['password'])  # hash the password
        account = Account(name=row['name'], email=row['email'], password=password)
        # add other fields as needed
        try:
            account.full_clean()  # validate model fields
            account.save()
            print(f'Imported account {account.id}: {account.email}')
        except ValidationError as e:
            print(f'Skipping row {index + 2}: invalid data ({e})')
    print('Accounts imported successfully')

if __name__ == '__main__':
    import_accounts('path/to/excel_file.xlsx')
