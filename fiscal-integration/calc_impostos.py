---

### 2️⃣ Na pasta `fiscal-integration/`
Crie o arquivo **`calc_impostos.py`** e cole isto:

```python
def calcular_iss_goiania(valor_bruto, aliquota):
    """
    Calcula o ISS retido e o valor líquido do serviço.
    Exemplo para serviços prestados em Goiânia/GO.
    """
    valor_iss = valor_bruto * (aliquota / 100)
    valor_liquido = valor_bruto - valor_iss
    
    return {
        "valor_servico": valor_bruto,
        "iss_retido": valor_iss,
        "total_receber": valor_liquido
    }

# Teste: R$ 5.000,00 com alíquota de 5%
resultado = calcular_iss_goiania(5000, 5)
print(f"ISS: R$ {resultado['iss_retido']:.2f}")
print(f"Total: R$ {resultado['total_receber']:.2f}")---

### 2️⃣ Na pasta `fiscal-integration/`
Crie o arquivo **`calc_impostos.py`** e cole isto:

```python
def calcular_iss_goiania(valor_bruto, aliquota):
    """
    Calcula o ISS retido e o valor líquido do serviço.
    Exemplo para serviços prestados em Goiânia/GO.
    """
    valor_iss = valor_bruto * (aliquota / 100)
    valor_liquido = valor_bruto - valor_iss
    
    return {
        "valor_servico": valor_bruto,
        "iss_retido": valor_iss,
        "total_receber": valor_liquido
    }

# Teste: R$ 5.000,00 com alíquota de 5%
resultado = calcular_iss_goiania(5000, 5)
print(f"ISS: R$ {resultado['iss_retido']:.2f}")
print(f"Total: R$ {resultado['total_receber']:.2f}")