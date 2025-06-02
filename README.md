# Expense Control

Este projeto tem como objetivo ajudar o usuário a ter controle sobre a movimentação bancária(entradas e saídas).

## 📁 Estrutura do Projeto

```
expenseControl/
├── scr
│   └── controller
│       ├── CategoryController.java
│       ├── DashboardController.java
│       └── TransactionController.java
│   ├── models
│       ├── Category.java
│       ├── Dashboard.java
│       ├── Transaction.java
│       └── TransactionType.java
│   ├── otherFx
│   ├── utils
│       └── ChartHelper.java
│       └── Utils.java
│   ├── view
│       └── CategoryView.java
│       └── DashboardView.java
│       └── TransactionView.java
│   ├── Application.md
│   ├── Main.md
├── .gitignore
└── README.md
```

## 🪛 Funções

- [  ] Adicionar, remover ou editar dados de movimentação
- [  ] Visualizar saldo atual e movimentações
- [  ] Filtragem, ferramenta de busca e sistema de ordenação
- [  ] Gráficos
- [  ] Exportar em .SVG .PDF .XML ou .JSON **_(Extra)_**

### 📄 Sobre as funções:

Ao adicionar uma movimentação todos os campos, exceto descrição, não devem ser nulos.

## 🛠️ Tecnologias Usadas

- Java 24

## 🤝 Contribuindo

Contribuições são super bem-vindas!

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b minha-feature`)
3. Commit suas mudanças (`git commit -m 'feat: minha nova feature'`)
4. Dê push na sua branch (`git push origin minha-feature`)
5. Abra um Pull Request


## 📄 Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://mit-license.org) para mais detalhes.