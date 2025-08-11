# Máquina de Venda de Ingressos de Cinema 🎟️

Este é um terminal de uma máquina de venda de ingressos de cinema, implementada em Python utilizando os princípios da **Arquitetura Limpa (Clean Architecture)**.

## Funcionalidades

- Criação, atualização e exclusão de contas de clientes
- Busca e listagem de filmes
- Reserva de ingressos (booking)
- Compra de ingressos com venda adicional de produtos (ex.: pipoca, refrigerante, doces)
- Geração de ingressos no terminal e em arquivo
- Registro de ações para depuração e conformidade

## Estrutura de Diretórios

```
cine_vending_machine/
├── domain/
│   ├── customer.py
│   ├── movie.py
│   └── product.py
├── repositories/
│   ├── customer_repository.py
│   └── movie_repository.py
├── services/
│   └── ticket_purchase_service.py
├── utils/
│   ├── logger.py
│   └── ticket_writer.py
├── logs/
│   └── cine.log
├── tickets/
│   └── (Arquivos de ingressos gerados)
├── tests/
│   ├── test_customer.py
│   ├── test_movie.py
│   ├── test_product.py
│   └── test_ticket_purchase_service.py
├── main.py
└── README.md
```

## Requisitos

- Python 3.7 ou superior

## Como Executar a Aplicação

```bash
python main.py
```

Siga as instruções no terminal para:

- Criar, atualizar ou excluir uma conta
- Buscar e visualizar filmes disponíveis
- Reservar ingressos (selecionar assentos e mantê-los temporariamente)
- Confirmar a compra e escolher produtos adicionais

## Como Executar os Testes Unitários

```bash
pip install -r requirements.txt
cd test
pytest
```

## Saída

- Os ingressos são impressos no terminal e salvos no diretório `tickets/`.
- Todas as operações e erros são registrados em `logs/cine.log`.

## Observações

- Cada sala de cinema possui capacidade limitada.
- Preços:

  - Ingresso: R$ 20,00 (Valor variável)
  - Refrigerante: R$ 4,00
  - Pipoca: R$ 3,00
  - Doce: R$ 2,00

## Licença

MIT

### Desenvolvedor
Nome: Sogolon Manding-Djata Vieira Jauará


