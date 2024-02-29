# Zillow Analytics Project

[Visão Geral](#visão-geral) | [Configuração do Ambiente](#configuração-do-ambiente) | [Estrutura da DAG](#estrutura-da-dag) | [Fluxo de Dados](#fluxo-de-dados) | [Contribuição](#contribuição) | [Autores](#autores) | [Licença](#licença)

## Visão Geral

O projeto Zillow Analytics é um sistema de engenharia de dados desenvolvido para consumir dados da API Zillow através do site RapidAPI, processar esses dados e armazená-los em um data warehouse para análise posterior. Este documento fornece uma visão geral do projeto, seus componentes principais e instruções para configurar e executar o sistema.

## Configuração do Ambiente

### Pré-requisitos

- Conta na AWS com permissões para criar e gerenciar recursos como EC2, S3 e Redshift.
- Conhecimento básico de Apache Airflow e Python.

### Passos de Configuração

1. **Crie uma instância EC2 na AWS**:
   - Crie uma instância EC2 Linux na AWS e instale os requisitos necessários, como Python, AWS CLI e Apache Airflow.

2. **Configure o Apache Airflow**:
   - Instale o Apache Airflow na instância EC2 e configure o ambiente de acordo com as necessidades do projeto.

3. **Defina as credenciais da AWS**:
   - Configure as credenciais da AWS na instância EC2 para que o Airflow possa acessar os serviços da AWS, como S3 e Redshift.

4. **Clone o repositório do projeto**:
   - Clone o repositório do projeto para a instância EC2 e organize os arquivos, incluindo a DAG e os códigos das funções Lambda.

5. **Configure as tarefas da DAG**:
   - Configure as tarefas da DAG conforme necessário, especificando os endpoints da API, os parâmetros de autenticação e os destinos de armazenamento.

6. **Teste o fluxo de dados**:
   - Execute a DAG e verifique se o fluxo de dados está funcionando corretamente, desde a extração dos dados da API até o carregamento no Redshift.

## Estrutura da DAG

A DAG (Directed Acyclic Graph) do projeto consiste em várias tarefas que são executadas em sequência para realizar o fluxo de processamento de dados. Abaixo estão as principais tarefas da DAG:

1. **Extract Zillow Data**: Tarefa responsável por fazer a requisição à API Zillow e extrair os dados.
2. **Load to S3**: Tarefa que move o arquivo JSON resultante para o bucket S3, na pasta "bronze".
3. **Is File in S3 Available**: Sensor que verifica se o arquivo foi processado e está disponível na pasta "gold" do bucket S3.
4. **Transfer S3 to Redshift**: Tarefa que carrega os dados do arquivo CSV no Redshift para análise posterior.

## Fluxo de Dados

O fluxo de dados no projeto segue as seguintes etapas:

1. Os dados são extraídos da API Zillow e armazenados em um arquivo JSON.
2. O arquivo JSON é movido para o bucket S3, onde desencadeia a execução de funções Lambda para processamento adicional.
3. Após o processamento, os dados são armazenados no Redshift para análise e consulta.

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas, bugs ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório do projeto.

## Autores

- Lucas Campos
