# ✂️ Agente IA Salão de Beleza — Interface Web

## 🎯 O que é?

Um **sistema completo de agendamento e atendimento com IA** para salões, barbearias e estética, com:

- 💬 **Chat com IA** (Gemini) — responde como um atendente humano
- 📅 **Gerenciador de agendamentos** — criar, editar, deletar
- 📊 **Dashboard** — métricas em tempo real
- 👥 **Gerenciador de contatos** — lista de clientes
- 📋 **Relatórios** — exportar CSV/Excel
- ⚙️ **Configurações** — personalizar seu salão

---

## 🚀 Começar em 5 Minutos

### Opção 1 — Publicar Online (Recomendado)

Veja: [PUBLICAR_STREAMLIT.md](PUBLICAR_STREAMLIT.md)

1. Copie este repositório no GitHub
2. Vá em [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu GitHub e faça deploy
4. Adicione GEMINI_API_KEY nos Secrets
5. **Pronto! Seu app está no ar!**

### Opção 2 — Rodar Localmente

```bash
# Instale dependências
pip install -r requirements.txt

# Crie arquivo de secrets
mkdir .streamlit
echo 'GEMINI_API_KEY = "sua_chave_aqui"' > .streamlit/secrets.toml

# Rode a app
streamlit run app.py
```

Acesse: `http://localhost:8501`

---

## 📦 Estrutura

```
agente-web/
├── app.py                      # App principal Streamlit
├── requirements.txt            # Dependências
├── .streamlit_secrets_example.toml # Template de secrets
├── PUBLICAR_STREAMLIT.md      # Guia de deploy
└── README.md                   # Este arquivo
```

---

## 🔧 Configuração

### 1. Obtenha GEMINI_API_KEY

```
https://aistudio.google.com
→ "Get API Key" → "Create API Key"
→ Copie a chave
```

### 2. Configure os Secrets

**Localmente:**
```bash
mkdir .streamlit
nano .streamlit/secrets.toml
```

```toml
GEMINI_API_KEY = "AIza..."
SALAO_NOME = "Seu Salão"
SALAO_ENDERECO = "Seu Endereço"
SALAO_TELEFONE = "Seu Telefone"
IA_NOME = "Sofia"
```

**No Streamlit Cloud:**
1. Dashboard do app
2. "Settings" → "Secrets"
3. Cole a configuração acima
4. Save

---

## 🎮 Funcionalidades

| Seção | Descrição |
|-------|-----------|
| **📊 Dashboard** | Métricas, gráficos, próximos agendamentos |
| **📅 Agendamentos** | Criar, editar, listar, filtrar |
| **💬 Chat IA** | Conversa com Gemini sobre serviços |
| **⚙️ Configurações** | Personalizar salão, horários, serviços |
| **📞 Contatos** | Gerenciar clientes e histórico |
| **📋 Relatórios** | Gráficos, exportar CSV/Excel |

---

## 🎨 Customização

### Mudar cores
Edite a seção CSS em `app.py`:
```python
--cor-primaria: #e91e8c;
--cor-secundaria: #ff6b9d;
```

### Adicionar novo serviço
Edite em `⚙️ Configurações` dentro da app ou em `app.py`:
```python
servicos_padrao = [
    "Novo Serviço - R$ 50,00",
    ...
]
```

### Mudare comportamento da IA
Edite `PROMPT_SOFIA` em `app.py`:
```python
prompt_sistema = f"""Você é {IA_NOME}..."""
```

---

## 📊 Dados

### Armazenamento
- **Session State** (local, durante a sessão)
- Pode ser integrado com:
  - Google Sheets
  - Firebase
  - PostgreSQL
  - SQLite

### Exportação
- ✅ CSV
- ✅ Excel
- 🔜 PDF
- 🔜 Google Sheets automático

---

## 🔗 Integração com Telegram (Próximo)

Exemplo de como conectar:

```python
from telegram.ext import Application
from telegram import Update

# Receive messages from Telegram
# Send to Streamlit via API
# Create agendamentos
```

Em desenvolvimento...

---

## 🐛 Troubleshooting

### Erro: "GEMINI_API_KEY not found"
- ✅ Adicione em `.streamlit/secrets.toml` (local)
- ✅ Ou em "Settings → Secrets" (Streamlit Cloud)

### Erro: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### App muito lento
- Streamlit Cloud Free pode ser lento
- Upgrade para Pro ($9/mês) para melhor performance

---

## 📱 Mobile

O app é **totalmente responsivo**:
- ✅ Desktop
- ✅ Tablet
- ✅ Mobile
- ✅ Landscape

---

## 🔒 Segurança

- ✅ Secrets criptografados no Streamlit Cloud
- ✅ GitHub privado (se necessário)
- ✅ HTTPS automático
- ✅ Sem dados sensíveis em code

**Nunca:**
- ❌ Compartilhe `.streamlit/secrets.toml`
- ❌ Coloque credenciais no código
- ❌ Faça commit de secrets

---

## 💰 Custos

**100% GRATUITO:**
- ✅ Streamlit Cloud: gratuito
- ✅ GitHub: gratuito
- ✅ Gemini API: 60 req/min gratuito
- ✅ Domínio: gratuito (`.streamlit.app`)

**Upgrade opcional:**
- Streamlit Pro: $9/mês
- Gemini API pago: por uso

---

## 🚀 Roadmap

- ✅ Interface web
- ✅ Chat IA
- ✅ Agendamentos
- 🔜 Integração Telegram
- 🔜 Google Calendar sync
- 🔜 Gmail automático
- 🔜 SMS/WhatsApp
- 🔜 Pagamento PIX
- 🔜 Programa de fidelidade

---

## 📚 Recursos

- [Documentação Streamlit](https://docs.streamlit.io)
- [Gemini API Docs](https://ai.google.dev)
- [GitHub](https://github.com)

---

## 📄 Licença

100% Open Source — Use livremente! 🎉

---

**Versão 1.0** | Junho 2026

✂️ Agente IA Salão de Beleza
