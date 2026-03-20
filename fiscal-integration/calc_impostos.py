# Cálculo de Impostos - Padrão Goiânia/GO
v_servico = 2500.0
aliquota = 5.0  # 5% de ISS

# Lógica de cálculo
v_iss = v_servico * (aliquota / 100)
v_liquido = v_servico - v_iss

# Exibição dos resultados
print("--- TESTE FISCAL GOIÂNIA ---")
print(f"Valor do Serviço: R$ {v_servico:.2f}")
print(f"Imposto (ISS): R$ {v_iss:.2f}")
print(f"Valor Líquido: R$ {v_liquido:.2f}")
print("----------------------------")