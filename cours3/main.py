import pandas as pd

# employee_data = pd.read_excel('employee_data.xlsx')
# print(employee_data.head())
# print(employee_data.info())
# print(employee_data.describe())

# add .head() will print the first 5 rows
# add .info() will add meta data
# add .describe() will explain the data

# employee_data['Bonus'] = employee_data['Salary'] * 0.1
# employee_data.to_excel('employee_data_with_bonus.xlsx', index = False)

# 10% bonus
# need to specify index or else it will start at the left

input_data = pd.read_excel('input.xlsx')
input_data['Total'] = input_data['Quantity'] * input_data['Price']

input_data.to_excel('output.xlsx', index = False)

print(output_data)
