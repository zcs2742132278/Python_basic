'''
创建Embedding模型
'''
import pandas as pd

# 表示学习+Embedding(嵌入)

# 从头开始读取
df = pd.read_csv('D:\Python_code\Python_basic\datas\\fine_food_reviews_1k.csv', index_col=0)

# print(df)
# 双重 方括号 选取多列，返回一个新的 DataFrame
# 把筛选结果重新赋值给 df，覆盖原来的 DataFrame
df = df[['Time', 'ProductId', 'UserId', 'Score', 'Summary', 'Text']]

# 删除cvs中缺失的数据，NaN，Nat的数据
df = df.dropna()

# 把'Summary','Text' 合并
df['combined'] = 'Title:' + df.Summary.str.strip() + ';Content:' + df.Text.str.strip()

n=10

# 输出前n行
print(df.head(n))