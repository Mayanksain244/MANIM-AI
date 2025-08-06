import pandas as pd
from datasets import load_dataset

train_data = pd.read_parquet("data/manim_sft_dataset_train.parquet")
all_data = pd.read_parquet("data/manim_sft_dataset_all.parquet")

print(train_data.head())    