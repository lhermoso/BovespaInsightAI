# BovespaInsightAI

BovespaInsightAI é uma plataforma inovadora de análise financeira que se destaca por sua dedicação exclusiva ao mercado de ações brasileiro, a Bovespa. 

Utilizando o poderoso pacote crewai juntamente com avançadas técnicas de inteligência artificial, o projeto proporciona insights detalhados e recomendações de investimento sobre empresas listadas na Bovespa. 

Por meio de uma equipe de agentes AI especializados, cada um focado em uma faceta distinta da análise financeira, BovespaInsightAI equipa investidores com análises aprofundadas e orientações estratégicas, facilitando tomadas de decisões informadas no dinâmico mercado de ações do Brasil.

## Configuração Inicial

Antes de começar, é necessário configurar o ambiente do projeto corretamente. Siga as etapas abaixo para configurar o seu ambiente.

### Configuração do Ambiente

1. **Clonar o Repositório**

   Primeiro, clone o repositório do projeto para sua máquina local usando o Git:

   ```
   git clone <URL_DO_REPOSITÓRIO>
   ```

2. **Configurar Variáveis de Ambiente**

   Dentro do projeto, você encontrará um arquivo chamado `.env-example`. Este arquivo contém um modelo das variáveis de ambiente necessárias para o funcionamento do projeto. Você deve criar uma cópia deste arquivo, renomeá-la para `.env` e preencher os valores conforme necessário.

   ```
   cp .env-example .env
   ```

   Abra o arquivo `.env` em um editor de texto e preencha os valores conforme sua configuração. As chaves das APIs podem ser obtidas nos seguintes sites:

   - **OPENAI_API_KEY**: Obtenha sua chave de API em [OpenAI](https://openai.com). Essa chave permitirá que você acesse os modelos de linguagem da OpenAI, como o GPT-4.
   - **SERPER_API_KEY**: Você pode obter uma chave gratuita em [Serper](https://serper.dev/). Essa API é usada para pesquisas avançadas e análise de resultados de motores de busca.
   - **BRAP_API_KEY**: Registre-se em [BrAPI](https://brapi.dev/) para obter uma chave. BrAPI fornece acesso a uma variedade de dados financeiros e de mercado.

   Preencha os valores no arquivo `.env` da seguinte forma:

   ```
   OPENAI_API_KEY=<Sua Chave OpenAI>
   SERPER_API_KEY=<Sua Chave Serper>
   OPENAI_MODEL_NAME=gpt-4-turbo-preview
   BRAP_API_KEY=<Sua Chave BrAPI>
   ```

3. **Instalar Dependências**

   O projeto depende de vários pacotes Python para funcionar corretamente. Para instalar essas dependências, use o seguinte comando:

   ```
   pip install -r requirements.txt
   ```


## Uso

Para iniciar o sistema de análise financeira, execute o arquivo `main.py`. O sistema solicitará que você insira o nome da empresa que deseja analisar. Após a entrada, os agentes de inteligência artificial realizarão análises e fornecerão um relatório detalhado.

```
python main.py
```

## Exemplo de Saída do Programa

Abaixo está um exemplo de um relatório de recomendação de investimento gerado pelo BovespaInsightAI, focando na Petrobras (Ticker: PETR4). Este exemplo ilustra o nível de detalhe e a profundidade das análises que os investidores podem esperar receber.

### **Relatório de Recomendação de Investimento Executivo: PETR4 (Petróleo Brasileiro S.A. - Petrobras)**

---

#### **1. Resumo Executivo**

Este relatório de investimento abrangente oferece uma análise profunda da Petrobras (Ticker: PETR4), uma entidade líder no setor global de energia, com foco principal em sua saúde financeira, posicionamento de mercado, iniciativas estratégicas e perspectivas futuras. Dadas as análises detalhadas que englobam demonstrações financeiras, posicionamento estratégico, política de dividendos e tendências de mercado, a PETR4 emerge como uma robusta oportunidade de investimento com potencial de crescimento distinto e rendimentos de dividendos favoráveis. No entanto, considerações sobre a volatilidade do mercado e ambientes regulatórios são imperativas para uma decisão de investimento equilibrada.

#### **2. Saúde Financeira e Posicionamento Estratégico**

A Petrobras demonstrou impressionante resiliência e crescimento financeiro, com a receita total saltando de 263,827 bilhões de BRL em 2019 para 641,256 bilhões de BRL em 2022. A trajetória do lucro líquido da empresa sublinha operações eficientes e rentabilidade. A base de ativos permanece sólida, embora os níveis de dívida de longo prazo necessitem de gestão vigilante.

#### **3. Política de Dividendos e Retornos**

A política de dividendos consistente da empresa, com uma taxa de pagamento recente de 1,355278 BRL em novembro de 2023, sublinha seu compromisso com o valor do acionista. Esta distribuição constante de dividendos apoia uma tese de investimento favorável para portfólios focados em renda.

#### **4. Tendências de Mercado e Iniciativas Estratégicas**

A Petrobras está estrategicamente posicionada para capitalizar a transição global para a energia renovável, com investimentos significativos em projetos de GNL e renováveis. Esta abordagem voltada para o futuro não só se alinha com as tendências de sustentabilidade, mas também abre caminhos para um crescimento robusto na paisagem energética em evolução.

#### **5. Avaliação e Riscos de Investimento**

Atualmente negociada a 36,68 BRL, com um preço-alvo máximo de 49 BRL definido por analistas, a PETR4 apresenta um perfil de risco-retorno equilibrado. As principais métricas de avaliação indicam uma sólida proposta de investimento. No entanto, os potenciais investidores devem considerar as implicações da dinâmica do mercado global de energia e dos desafios regulatórios no Brasil.

#### **6. Conclusão e Recomendação Estratégica de Investimento**

**A PETR4 se destaca como uma avenida de investimento atraente**, amalgamando robustez financeira, visão estratégica na evolução da energia e uma política de dividendos amigável ao acionista. Nossa recomendação é uma postura de **"Compra"** para a PETR4, baseada em seu potencial de crescimento, posicionamento estratégico em energia renovável e rendimentos de dividendos atraentes. Incentiva-se que os investidores considerem um horizonte de médio a longo prazo, equilibribrando os riscos inerentes com os fortes fundamentos da empresa e as oportunidades de mercado.

**Os investidores devem permanecer vigilantes** à volatilidade do setor global de energia e às mudanças regulatórias no Brasil, ajustando suas estratégias de investimento de acordo. Também é aconselhável o monitoramento contínuo das práticas de gestão da dívida da empresa e dos desenvolvimentos regulatórios para mitigar potenciais riscos.

**A combinação da força financeira da PETR4, iniciativas estratégicas e alinhamento com as tendências globais de energia posiciona-a como um competidor notável para inclusão em portfólios de investimento diversificados**, com o objetivo de alavancar o crescimento do setor de energia enquanto navega por seus desafios.

*Este relatório sintetiza análises financeiras e estratégicas extensas até o ano de 2024, visando fornecer aos investidores uma base clara e informada para suas decisões de investimento na Petrobras.*

**Aviso Legal:** *Este relatório é apenas para fins informativos e não constitui um conselho financeiro ou uma solicitação para comprar ou vender valores mobiliários. Os investidores devem realizar sua própria diligência e consultar um conselheiro financeiro antes de tomar quaisquer decisões de investimento.*

---

## Contribuindo

Sinta-se à vontade para contribuir para o projeto! Se você tiver melhorias ou correções, abra um pull request ou uma issue no repositório do GitHub.

---
