'''
创建Embedding模型
使用 ModelScope（魔搭社区）下载模型，sentence-transformers 本地加载
'''
import pandas as pd
from sentence_transformers import SentenceTransformer

# 表示学习+Embedding(嵌入)

# 1.读取数据，然后预处理
df = pd.read_csv(r'D:\Python_code\Python_basic\datas\fine_food_reviews_1k.csv', index_col=0)

df = df[['Time', 'ProductId', 'UserId', 'Score', 'Summary', 'Text']]
df = df.dropna()

# 把'Summary','Text' 合并
df['combined'] = 'Title:' + df.Summary.str.strip() + ';Content:' + df.Text.str.strip()

top_n = 1000

# 根据时间排序
df = df.sort_values('Time')
df = df.drop('Time', axis=1)
df = df.tail(top_n)

# 2.生成Embedding之后的向量空间，并且保存
# 从 ModelScope 下载模型到本地
from modelscope import snapshot_download
model_dir = snapshot_download('iic/nlp_gte_sentence-embedding_chinese-base')

# 用 sentence-transformers 加载本地模型
model = SentenceTransformer(model_dir)

# 生成Embedding
df['embedding'] = df.combined.apply(lambda x: model.encode(x).tolist())

df.to_csv(r'D:\Python_code\Python_basic\datas\embedding_out2k.csv')

print(df['embedding'][0])