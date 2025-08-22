import pandas as pd
import matplotlib.pyplot as plt

# Carrega a planilha
df = pd.read_excel("vendas.xlsx", sheet_name="data-parsed-by-rebeca bodin (12")

# Exibe as primeiras linhas para verificar
print(df.head())

# Remove linhas com valores nulos nas colunas principais
df = df.dropna(subset=["Business Category", "Followers"])

# Agrupa por categoria de negócio e soma os seguidores
agrupado = df.groupby("Business Category")["Followers"].sum().sort_values(ascending=False)

# Exibe gráfico
agrupado.plot(kind="bar", figsize=(10, 6), title="Total de seguidores por categoria")
plt.xlabel("Categoria de negócio")
plt.ylabel("Total de seguidores")
plt.tight_layout()
plt.show()
