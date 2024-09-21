# Extração de Produtos de Site de Compras

Este projeto utiliza Selenium para navegar em um site de compras, alternando entre diferentes filtros de pesquisa. O objetivo é extrair os produtos que aparecem em todas as buscas realizadas, permitindo a identificação dos itens mais relevantes de forma eficiente.

## Funcionalidades

- **Busca por Produtos:** Realiza pesquisas por termos específicos, como "notebook".
- **Extração de Produtos:** Extrai nomes de produtos de páginas de resultados, considerando diferentes filtros (sem filtros, menores preços, melhores avaliados).
- **Identificação de Produtos Comuns:** Identifica e salva os produtos que aparecem em todas as pesquisas, permitindo uma análise mais eficaz.

## Tecnologias Utilizadas

- **Python:** Linguagem de programação principal.
- **Selenium:** Biblioteca para automação de navegadores, utilizada para interagir com o site de compras.
- **WebDriver:** Ferramenta para controlar o navegador Chrome.
- **XPATH:** Utilizado para localizar elementos no DOM da página.

## Como Usar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/duducamargo/selenium-project.git
