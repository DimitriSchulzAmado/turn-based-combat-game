# Turn-Based Combat Game

Um jogo simples de combate por turnos desenvolvido em Python, onde um herói enfrenta um inimigo em batalhas estratégicas.

## 📋 Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Biblioteca padrão do Python** - `random` para geração de danos aleatórios

## 🏗️ Padrões de Projeto

- **Herança** - Classes `Hero` e `Enemy` herdam de `Character`
- **Encapsulamento** - Atributos privados com métodos getter
- **Polimorfismo** - Sobrescrita de métodos como `show_details()`
- **Separação de Responsabilidades** - Estrutura modular com separação clara entre personagens e lógica do jogo

## 📁 Estrutura do Projeto

```
jogo/
├── main.py                 # Ponto de entrada da aplicação
├── src/
│   ├── characters/         # Módulo dos personagens
│   │   ├── character.py    # Classe base Character
│   │   ├── hero.py         # Classe Hero
│   │   └── enemy.py        # Classe Enemy
│   └── game/
│       └── game.py         # Lógica principal do jogo
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado

### Passos para execução

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd jogo
   ```

2. **Execute o jogo:**
   ```bash
   python main.py
   ```

## 🎮 Como Jogar

1. O jogo iniciará automaticamente uma batalha entre o herói e o inimigo
2. A cada turno, você pode escolher:
   - **1**: Ataque normal
   - **2**: Ataque especial (mais poderoso)
3. O jogo continua até que um dos personagens seja derrotado
4. Pressione Enter para prosseguir entre as ações

## 🔧 Configuração de Desenvolvimento

Não há dependências externas. O projeto utiliza apenas a biblioteca padrão do Python.

Para desenvolvimento, recomenda-se:

- Python 3.8+
- Editor de código com suporte a Python (VS Code, PyCharm, etc.)
