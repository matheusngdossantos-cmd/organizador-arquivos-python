# 🗂️ Organizador de Arquivos em Python

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20(Zero%20pip)-brightgreen)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success)

Automação em Python desenvolvida para organizar pastas com acúmulo desordenado de arquivos (como **Downloads** ou **Área de Trabalho**). Com interface gráfica nativa para seleção do diretório e classificação dinâmica por tipo de extensão, o script cria automaticamente as pastas de destino e realoca cada arquivo de forma segura e instantânea.

---

## 📌 Sobre o Projeto

Quem nunca acumulou centenas de relatórios, imagens, planilhas e códigos na pasta de Downloads? Este projeto resolve esse problema de forma automatizada:

1. **Interface Gráfica Intuitiva**: Abre a janela nativa do seu sistema operacional para escolher a pasta com apenas um clique, sem precisar digitar caminhos longos no terminal.
2. **Criação Sob Demanda**: Verifica se as pastas de destino já existem antes de criá-las (`os.path.exists` + `os.mkdir`), evitando erros e mantendo o diretório limpo.
3. **Classificação Automática**: Identifica a extensão do arquivo e o move para sua categoria correspondente em segundos.
4. **Zero Dependências Externas**: Utiliza apenas módulos nativos da biblioteca padrão do Python (`os` e `tkinter`), funcionando diretamente após clonar o repositório.

---

## 📂 Categorias e Extensões Suportadas

O organizador categoriza os arquivos nas seguintes subpastas:

| Pasta de Destino | Extensões Mapeadas | Finalidade |
| :--- | :--- | :--- |
| `imagens/` | `.png`, `.jpg` | Fotos, capturas de tela e ilustrações |
| `planilhas/` | `.xlsx` | Arquivos do Microsoft Excel |
| `pdfs/` | `.pdf` | Documentos e relatórios em PDF |
| `csv/` | `.csv` | Datasets e planilhas tabulares leves |
| `word/` | `.docx` | Documentos do Microsoft Word |
| `pptx/` | `.pptx` | Apresentações do PowerPoint |
| `python/` | `.py` | Scripts e códigos-fonte Python |

---

## 🚀 Como Executar

### Pré-requisitos
- Ter o **Python 3.8 ou superior** instalado na máquina ([Download oficial do Python](https://www.python.org/downloads/)).
- O módulo `tkinter` já vem instalado por padrão no Windows e macOS. No Linux Ubuntu/Debian, caso necessário:
  ```bash
  sudo apt-get install python3-tk
  ```

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/organizador-de-arquivos.git
   cd organizador-de-arquivos
   ```

2. **Execute o script:**
   ```bash
   python organizador.py
   ```
   *(No macOS ou Linux, use `python3 organizador.py` se necessário).*

3. **Selecione a pasta:**
   Uma janela pop-up será exibida com o título *"Selecione uma pasta"*. Navegue até a pasta que deseja organizar (ex: `Downloads`) e clique em **Selecionar**.

4. **Resultado:**
   Todos os arquivos suportados serão organizados nas suas respectivas subpastas automaticamente!

---

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)**: Linguagem de programação principal.
- **`os` (Standard Library)**: Varredura de diretórios (`os.listdir`), separação de nome e extensão (`os.path.splitext`), verificação de existência (`os.path.exists`), criação de pastas (`os.mkdir`) e movimentação (`os.rename`).
- **`tkinter.filedialog` (Standard Library)**: Janela de diálogo nativa do sistema (`askdirectory`) para seleção visual intuitiva.

---

## 💡 Como Personalizar

Você pode adicionar novas extensões ou pastas facilmente editando o dicionário `locais` no arquivo `organizador.py`:

```python
locais = {
    'imagens': ['.png', '.jpg', '.jpeg', '.gif', '.svg'],
    'planilhas': ['.xlsx', '.xls'],
    'pdfs': ['.pdf'],
    'csv': ['.csv'],
    'word': ['.docx', '.doc'],
    'pptx': ['.pptx', '.ppt'],
    'python': ['.py', '.ipynb'],
    'compactados': ['.zip', '.rar', '.7z'],
    'videos': ['.mp4', '.mkv', '.avi'],
    'audio': ['.mp3', '.wav']
}
```

---

## 📁 Estrutura do Repositório

```text
organizador-de-arquivos/
│
├── organizador.py        # Código-fonte principal da automação
├── README.md             # Documentação completa e instruções do projeto
├── requirements.txt      # Especificação das dependências (Standard Library)
├── .gitignore            # Arquivos e diretórios ignorados pelo Git
└── LICENSE               # Licença MIT de código aberto
```

---

## 📄 Licença

Este projeto está sob a licença **MIT** - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👤 Autor

Desenvolvido por **Matheus** 🚀  
- GitHub: [@matheusngdossantos](https://github.com/matheusngdossantos)  
- E-mail: [matheusngdossantos@gmail.com](mailto:matheusngdossantos@gmail.com)  

Se este projeto te ajudou a manter seu computador organizado, deixe uma ⭐️ no repositório!
