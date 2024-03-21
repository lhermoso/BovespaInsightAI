Para criar um `README.md` para o seu projeto que inclui instruções sobre o preenchimento do arquivo `.env-example` e a instalação dos pacotes usando `requirements.txt`, você pode usar o seguinte modelo:

---

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

## Contribuindo

Sinta-se à vontade para contribuir para o projeto! Se você tiver melhorias ou correções, abra um pull request ou uma issue no repositório do GitHub.

---
