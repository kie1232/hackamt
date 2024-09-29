# Sistema de Registro de Produtos

Este projeto é um sistema simples de registro de produtos desenvolvido em Python, utilizando a biblioteca Tkinter para a interface gráfica e Pandas para o gerenciamento de dados. O sistema permite que o usuário selecione produtos e registre IDs de itens, monitorando o progresso do registro.

## Funcionalidades

- **Seleção de Produtos**: O usuário pode escolher entre uma lista de produtos disponíveis.
- **Registro de IDs**: Após a seleção de um produto, o usuário pode inserir IDs correspondentes e o sistema informará quantos IDs ainda precisam ser registrados.
- **Status do Registro**: O status do registro é atualizado em tempo real, indicando se o registro está pendente ou completo.
- **Interface Gráfica**: A interface é amigável e intuitiva, facilitando a navegação e o uso do sistema.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Tkinter**: Biblioteca para a criação da interface gráfica.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Pillow**: Biblioteca para manipulação de imagens (opcional, utilizada para exibir imagens).

## Instalação

1. **Clone o repositório** ou faça o download do código.
2. **Instale as dependências** necessárias (se ainda não estiverem instaladas):
   ```bash
   pip install pandas pillow
   ```
3. **Execute o programa**:
   ```bash
   python nome_do_arquivo.py
   ```

## Como Usar

1. Ao iniciar o programa, você será recebido na tela inicial.
2. Clique no botão "Iniciar Registro de Produtos" para acessar a página de seleção de produtos.
3. Escolha um produto na lista suspensa.
4. Insira os IDs na caixa de entrada e pressione Enter ou clique no botão "Confirmar" para registrar o ID.
5. O sistema mostrará quantos IDs ainda precisam ser registrados. Quando todos os IDs forem registrados, uma mensagem de sucesso aparecerá.

## Exemplo de Imagem

![Exemplo de Tela](C:/Users/Igoor/OneDrive/Documentos/Projetos/hackamt/in.png)  
*(Certifique-se de que a imagem está no caminho correto antes de executar o programa.)*

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões, correções ou melhorias, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
