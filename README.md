## Lead Finder
Aplicação que realiza a busca por leads de forma simples e rápida.

### Requisitos
- **Python 3.10+** instalado no sistema
- **Git** (opcional, mas recomendado)

### Baixar / clonar o projeto
Se ainda não tiver o projeto localmente:

```bash
git clone https://seu-usuario/seu-repo.git
cd Lead_Finder
```

> Substitua a URL acima pela URL real do seu repositório no GitHub/GitLab/etc.

### Criar e ativar o ambiente virtual (sem versionar no Git)
Dentro da pasta do projeto, crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no **Windows (PowerShell)**:

```bash
.\venv\Scripts\Activate.ps1
```

Quando terminar de usar o projeto, você pode desativar com:

```bash
deactivate
```

> O diretório `venv/` já está no `.gitignore`, então não será enviado para o Git.

### Instalar dependências (`requirements.txt`)
Com o ambiente virtual **ativado**, instale todas as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Como rodar a aplicação
Com o ambiente virtual **ativado** e as dependências instaladas, use o comando abaixo para iniciar a aplicação Streamlit:

```bash
python -m streamlit run app.py
```

Após rodar o comando, o Streamlit abrirá a aplicação no navegador (ou mostrará um link no terminal para você acessar).

### Boas práticas com Git
- **Nunca** commitar:
  - pastas de ambiente virtual (`venv/`, `.venv/`, `env/`)
  - arquivos `.env` com senhas/chaves
  - arquivos gerados automaticamente (logs, caches, etc.)
- Sempre confira os arquivos antes de commitar:

```bash
git status
git diff
```
