from sdv.tabular import CTGAN
import pandas as pd

df = pd.read_csv("dataset_evasao_sintetico_v3.csv")

model = CTGAN()
model.fit(df)

df_refinado = model.sample(3000)

df_refinado.to_csv("evasao_refinado.csv", index=False)

