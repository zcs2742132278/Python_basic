'''
创建Embedding模型
OpenAI 的 Embedding（嵌入）是一套把「文本 / 代码」转成「高维数字向量」的模型与 API，用来做语义理解、检索、RAG 等

我没有OpenAI的账号，所以换用DeepSeek的方式实现
'''
import pandas as pd
from sentence_transformers import SentenceTransformer

# 表示学习+Embedding(嵌入)

# 1.读取数据，然后预处理
# 从头开始读取
df = pd.read_csv(r'D:\Python_code\Python_basic\datas\fine_food_reviews_1k.csv', index_col=0)

# 双重 方括号 选取多列，返回一个新的 DataFrame
# 把筛选结果重新赋值给 df，覆盖原来的 DataFrame
df = df[['Time', 'ProductId', 'UserId', 'Score', 'Summary', 'Text']]

# 删除cvs中缺失的数据，NaN，Nat的数据
df = df.dropna()

# 把'Summary','Text' 合并
df['combined'] = 'Title:' + df.Summary.str.strip() + ';Content:' + df.Text.str.strip()

top_n = 1000

# 根据时间排序
df = df.sort_values('Time')
# 删去Time列
df = df.drop('Time', axis=1)

df = df.tail(top_n)

# 2.生成Embedding之后的向量空间，并且保存
# 使用本地 sentence-transformers 模型，无需 API Key
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 生成Embedding
df['embedding'] = df.combined.apply(lambda x: model.encode(x).tolist())


df.to_csv(r'D:\Python_code\Python_basic\datas\embedding_out2k.csv')

print(df['embedding'][0])