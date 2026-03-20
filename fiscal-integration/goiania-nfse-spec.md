### 🏛️ Especificação NFS-e Goiânia (Padrão ABRASF)

**Endpoints:**
- Homologação: `https://homologacao.goiania.go.gov.br/ws/nfse.asmx`
- Produção: `https://nfse.goiania.go.gov.br/ws/nfse.asmx`

**Estrutura Base do XML (Envio de Lote):**
```xml
<EnviarLoteRpsEnvio xmlns="[http://www.abrasf.org.br/nfse.xsd](http://www.abrasf.org.br/nfse.xsd)">
  <LoteRps Id="Lote001" versao="1.00">
    <NumeroLote>1</NumeroLote>
    <Cnpj>00000000000000</Cnpj>
    <InscricaoMunicipal>000000</InscricaoMunicipal>
    <QuantidadeRps>1</QuantidadeRps>
    <ListaRps>
      </ListaRps>
  </LoteRps>
</EnviarLoteRpsEnvio>