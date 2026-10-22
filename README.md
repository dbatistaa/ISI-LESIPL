# Auditoria de Logs de Autenticação SSH e Deteção Automatizada de Ataques de Força Bruta

## Identificação

-   **Autor:** Daniel Alves Batista
-   **Unidade curricular:** Integração de Sistemas de Informação
-   **Curso:** Licenciatura em Engenharia de Sistemas Informáticos (Pós Laboral)
-   **Ano letivo:** 2026/2027

## 1. Descrição

Este projeto aplica um processo ETL à análise de logs de autenticação
SSH. O workflow KNIME lê logs SSH e dados complementares em XML, extrai
campos através de expressões regulares, cruza e trata os dados, consulta
a API externa ip-api.com para enriquecer os endereços IP e guarda
eventos no PostgreSQL. O Grafana permite visualizar indicadores e
gráficos.

A regra de deteção seleciona autenticações falhadas, agrupa-as por IP e
identifica endereços com **cinco ou mais falhas**. Não utiliza uma
janela temporal; por isso, sinaliza atividade potencialmente suspeita,
mas não confirma definitivamente um ataque.

## 2. Tecnologias

-   **KNIME Analytics Platform:** processamento ETL.
-   **PostgreSQL:** persistência dos eventos.
-   **Grafana:** dashboard de visualização.
-   **API externa ip-api.com:** informação sobre país, cidade e
    fornecedor de Internet.
-   **Python:** geração de logs sintéticos através de
    `generate_logs.py`.
-   **Docker Compose:** utilizado para executar PostgreSQL e Grafana, se
    o ficheiro Compose estiver incluído no repositório.

O Node-RED e uma API REST própria não fazem parte da implementação
concluída.

## 3. Estrutura do repositório

O repositório contém os seguintes ficheiros e recursos do projeto:

README.md — descrição do projeto e instruções de execução.

generate_logs.py — script Python para gerar logs de autenticação SSH sintéticos.

data/ — diretório com os ficheiros de dados utilizados no processamento.

Ficheiro do workflow KNIME — definição do processo ETL de leitura, transformação, enriquecimento e deteção.

docker-compose.yml — configuração dos serviços PostgreSQL e Grafana.

init.sql — script SQL para inicialização da base de dados e criação das tabelas.

Relatório final — documentação do trabalho desenvolvido.

Vídeo de demonstração — apresentação do workflow e dos resultados obtidos.

## 4. Pré-requisitos

-   KNIME Analytics Platform.
-   Python 3, caso queira gerar novamente os logs.
-   Docker Desktop e Docker Compose, caso exista um
    `docker-compose.yml`.
-   Acesso à API externa para enriquecimento dos endereços IP.
-   PostgreSQL e Grafana configurados para o ambiente utilizado.

## 5. Como executar

### Gerar logs de teste (opcional)

Na pasta que contém `generate_logs.py`, execute:

``` bash
python3 generate_logs.py
```

O script original escreve em `data/auth.log`, relativamente à pasta de
trabalho atual. Confirme que a pasta existe e que o caminho corresponde
ao configurado no nó `Line Reader`. A execução substitui o conteúdo
anterior do ficheiro.

### Iniciar os serviços (se existir Docker Compose)

Na pasta onde se encontra `docker-compose.yml`, execute:

``` bash
docker compose up -d
docker compose ps
```

Consulte o ficheiro Compose para confirmar portas, serviços e
credenciais. Não publique credenciais reais no repositório.

### Executar o workflow

1.  Abra o KNIME Analytics Platform.
2.  Abra ou importe o workflow do repositório.
3.  Confirme os caminhos dos ficheiros de entrada.
4.  Confirme a ligação ao PostgreSQL.
5.  Execute o workflow e verifique as etapas de leitura, transformação,
    enriquecimento, persistência e exportação JSON.

### Consultar o Grafana

Abra o endereço e a porta definidos na configuração local. Se a
configuração utilizada expuser a porta habitual do Grafana, experimente
`http://localhost:3000`. Utilize as credenciais configuradas no ambiente
e confirme que a fonte de dados PostgreSQL está operacional.

## 6. Regra de deteção e limitações

1.  Filtrar eventos com estado `Failed`.
2.  Agrupar por endereço IP.
3.  Contar as tentativas falhadas.
4.  Selecionar IPs com contagem igual ou superior a cinco.
5.  Exportar os resultados para JSON.

A regra não considera uma janela temporal. O limiar representa a
contagem de falhas no conjunto de dados processado, não necessariamente
falhas num curto intervalo.

## 7. Vídeo de demonstração

**Link para o vídeo:** https://drive.google.com/file/d/1NfWFMTBdv58XdRDMQTV2Xv-TapOV6JzY/view?usp=sharing

O vídeo demonstra o workflow KNIME, as etapas principais de
transformação e deteção e o dashboard Grafana.

## 8. Relatório

O relatório final acompanha os restantes materiais de submissão, de
acordo com as instruções da unidade curricular.
