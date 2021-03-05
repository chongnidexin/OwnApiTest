import pandas as pd

df = pd.read_excel('test_data.xlsx', sheet_name='inquire')
# test_data = []
# for i in df.index.values:
#     row_data = df.ix[i, ['url', 'data', 'title', 'case_id', 'http_method']].to_dict()
#     test_data.append(row_data)
#     df.ix

# print(test_data)
print(df.ix[1])