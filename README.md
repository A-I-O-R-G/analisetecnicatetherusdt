# 📝 Documentação do Projeto: Análise Técnica da Stablecoin Tether (USDT)

## 📖 Introdução
Este projeto visa a criação de um script para análise técnica da stablecoin Tether (USDT). O objetivo principal é coletar, analisar e visualizar dados de preços históricos em relação a outras criptomoedas e moedas fiduciárias, fornecendo insights valiosos para traders e investidores.

### Funcionalidades-chave:
- Coleta de dados históricos de preços e volume de negociação.
- Cálculo de indicadores técnicos como médias móveis, suporte e resistência.
- Visualização dos resultados em gráficos interativos.

---

## ⚙️ Instalação

### Requisitos do Sistema:
- Python 3.x instalado.
- Bibliotecas necessárias: `requests`, `pandas`, `numpy`, `plotly`.

### Dependências Necessárias:
```bash
pip install requests pandas numpy plotly
```

### Guia Passo-a-Passo:
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd seu_repositorio
   ```
3. Instale as dependências conforme indicado acima.

### Configuração Inicial:
- Nenhuma configuração adicional é necessária para iniciar o projeto.

---

## 🔍 Uso

### Exemplos Práticos:
Execute o script principal para coletar dados e gerar gráficos:
```bash
python main.py
```

### Comandos Principais:
- **`coletar_dados_historicos`**: Função para coletar dados históricos da Tether.
- **`media_movel`**: Calcula a média móvel a partir dos dados coletados.
- **`calcular_rsi`**: Calcula o Índice de Força Relativa (RSI) dos preços.

### Configurações Disponíveis:
- `symbol`: Defina para qual par deseja coletar dados (ex: 'USDTBUSD').
- `interval`: Ajuste o intervalo de tempo para a coleta de dados (opcional, padrão é '1d').

### Casos de Uso Comuns:
- Análise diária de preços.
- Identificação de padrões de negociação.

---

## 📁 Estrutura do Projeto
```
seu_repositorio/
├── main.py             # Script principal para análise técnica
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação deste projeto
```

---

## 🌐 API

### Endpoints Disponíveis:
- `GET https://api.binance.com/api/v3/klines`: Coleta dados de preços históricos.

### Métodos e Parâmetros:
- **Método**: `GET`
- **Parâmetros**:
  - `symbol`: O par de negociação, ex: 'USDTBUSD'.
  - `interval`: O intervalo para as velas, ex: '1d'.
  - `limit`: Limite de dados a serem coletados.

### Exemplos de Requisições:
```python
coletar_dados_historicos('USDTBUSD')
```

### Respostas Esperadas:
```json
[
    ["open_time", "open", "high", "low", "close", "volume", ...]
]
```

---

## 🤝 Contribuição

### Guia para Contribuidores:
1. Crie um fork do repositório.
2. Crie sua branch:
   ```bash
   git checkout -b feature/nome-da-sua-feature
   ```
3. Faça suas alterações e commit:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nome-da-sua-feature
   ```

### Padrões de Código:
- Utilize PEP 8 para a formatação Python.

### Processo de Pull Request:
- Abra um pull request na interface do GitHub descrevendo suas alterações.

### Boas Práticas:
- Documente suas funções e métodos.
- Teste suas alterações antes de enviar.

---

## 📜 Licença

### Tipo de Licença:
Este projeto está licenciado sob a Licença MIT.

### Termos de Uso:
Liberdade para uso, cópia, modificação e distribuição do software.

### Restrições:
Não há restrições além da inclusão do aviso de licença em qualquer distribuição do software.

---

## 🛠️ Manutenção Contínua
Mantemos atualizações regulares, revisões e adições de novas funcionalidades com foco na precisão e eficiência do código.

---

Sinta-se à vontade para ajustar quaisquer partes da documentação conforme necessário. Se precisar de mais informações ou ajustes, estarei à disposição!