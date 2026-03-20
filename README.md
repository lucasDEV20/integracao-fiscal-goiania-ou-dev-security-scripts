# 🚀 Integração Fiscal & Security Dev Environment

Este repositório centraliza ferramentas de automação para integração fiscal (padrão Goiânia/GO) e scripts de segurança de infraestrutura. O objetivo é facilitar o fluxo de desenvolvimento para sistemas que lidam com faturamento eletrônico e proteção de servidores Windows.

---

## 📂 Estrutura do Repositório

### 🏛️ `fiscal-integration/`
Conteúdo focado na comunicação com os WebServices da Prefeitura de Goiânia.
- **`goiania-nfse-spec.md`**: Documentação técnica contendo endpoints (Homologação/Produção), métodos SOAP (ABRASF) e exemplos de XML de envio.
- **`calc_impostos.py`**: Script em Python demonstrando a lógica de cálculo de impostos retidos (ISS/Aliquota) para serviços prestados.

### 🛡️ `security-scripts/`
Scripts para endurecimento (hardening) de sistemas Windows.
- **`setup-rdp-block.bat`**: Automação via CMD para desabilitar o protocolo RDP no registro e configurar regras restritivas no Firewall do Windows (Porta 3389).

---

## 🛠️ Tecnologias Utilizadas
- **Linguagens:** Python, Batch (CMD)
- **Protocolos:** SOAP/REST, XML (Padrão ABRASF 1.0)
- **Ambiente:** Windows Server / Integração Fiscal Municipal

---

## 🚀 Como Utilizar

### Integração Fiscal
Para utilizar os esquemas de XML em Goiânia:
1. Verifique os endpoints no arquivo de especificação.
2. Utilize um certificado digital (A1/A3) para assinar as mensagens XML.
3. Utilize a lógica de `calc_impostos.py` para validar os valores antes do envio do lote.

### Segurança
**Atenção:** Os scripts na pasta `security-scripts/` devem ser executados como **Administrador**.
- O script `setup-rdp-block.bat` interrompe conexões remotas imediatamente para prevenir ataques de força bruta.

---

## ✍️ Autor
**Lucas Araújo da Silva**
*Analista de Sistemas & Desenvolvedor Full-Stack*

---
> *Este projeto faz parte de um conjunto de ferramentas para otimização de processos fiscais e segurança digital.*
