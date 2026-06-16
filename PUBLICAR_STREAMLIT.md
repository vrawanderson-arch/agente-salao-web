# 🚀 Publicar Agente IA na Web — Grátis em 5 Minutos

## ✨ O que você vai ter:

- ✅ Interface web profissional
- ✅ Dashboard com métricas
- ✅ Gerenciador de agendamentos
- ✅ Chat com IA
- ✅ Hospedado GRÁTIS no Streamlit Cloud
- ✅ Seu próprio domínio `.streamlit.app`
- ✅ SSL/HTTPS automático

---

## 📋 Pré-requisitos

1. **GitHub** — conta gratuita (para armazenar código)
2. **Streamlit Cloud** — conta gratuita
3. **GEMINI_API_KEY** — obtido em https://aistudio.google.com

---

## 🎯 Passo a Passo — Publicar em 5 Minutos

### 1️⃣ Prepare o repositório GitHub

```bash
# Clone ou crie um repositório
mkdir agente-salao-web
cd agente-salao-web

# Copie os arquivos
cp app.py .
cp requirements.txt .
cp .streamlit_secrets_example.toml .

# Git
git init
git add .
git commit -m "Initial commit - Agente IA Salão"
git branch -M main
git remote add origin https://github.com/seu-usuario/agente-salao-web.git
git push -u origin main
```

**Ou use GitHub Web:**
1. Acesse [github.com/new](https://github.com/new)
2. Crie um novo repositório: `agente-salao-web`
3. Upload dos arquivos via web
4. Commit

### 2️⃣ Obtenha sua GEMINI_API_KEY

1. Acesse [aistudio.google.com](https://aistudio.google.com)
2. Clique em **"Get API Key"** → **"Create API Key"**
3. Copie a chave (começa com `AIza...`)
4. Guarde em local seguro

### 3️⃣ Publique no Streamlit Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Faça login com GitHub
3. Clique em **"New app"**
4. Selecione:
   - **Repository:** seu-usuario/agente-salao-web
   - **Branch:** main
   - **Main file path:** app.py
5. Clique em **"Deploy"**

### 4️⃣ Configure as Credenciais (Secrets)

Após deploy, Streamlit mostra a URL. Para adicionar secrets:

1. Na página do app, clique em **"三"** (menu)
2. Vá em **"Settings"** → **"Secrets"**
3. Cole seu GEMINI_API_KEY:

```toml
GEMINI_API_KEY = "AIza..."
SALAO_NOME = "Salão Bella"
SALAO_ENDERECO = "Rua das Flores, 123"
SALAO_TELEFONE = "(81) 99999-9999"
IA_NOME = "Sofia"
```

4. Clique em **"Save"**
5. O app vai redeployar automaticamente

### 5️⃣ Pronto! 🎉

Seu app está no ar em:
```
https://seu-usuario-agente-salao-web.streamlit.app
```

---

## 🎮 Como Usar Sua Interface Web

### Dashboard
- Métricas em tempo real
- Total de agendamentos
- Taxa de confirmação
- Gráficos de serviços

### Agendamentos
- ➕ Criar novo agendamento
- 📋 Listar todos
- 🔍 Filtrar por status/serviço/data
- ✏️ Editar (em desenvolvimento)
- 🗑️ Deletar

### Chat IA
- Conversa com Sofia (IA Gemini)
- Respostas sobre serviços
- Sugestões de agendamento

### Configurações
- Nome do salão
- Endereço
- Telefone
- Horários de funcionamento
- Serviços oferecidos

### Contatos
- 👥 Lista de clientes
- 📞 Telefones e e-mails
- Histórico de agendamentos
- ➕ Adicionar novo

### Relatórios
- 📊 Gráficos de agendamentos
- 📥 Exportar CSV/Excel
- 📈 Análises

---

## 🔒 Segurança

### Nunca compartilhe:
- GEMINI_API_KEY
- Arquivo `.streamlit/secrets.toml`
- Repositório privado (se tiver dados sensíveis)

### Segredos no Streamlit Cloud:
- Automaticamente criptografados
- Variáveis de ambiente seguras
- Não aparecem em logs

---

## 🆘 Erros Comuns

| Erro | Solução |
|------|---------|
| `GEMINI_API_KEY not found` | Adicione em Secrets no dashboard |
| `Module not found` | Verifique `requirements.txt` |
| `App crashes` | Verifique os logs em "Manage app" |
| `Lento` | Streamlit Cloud Free pode ser lento (aguarde) |

---

## 📱 Acessar de Qualquer Lugar

Compartilhe o link:
```
https://seu-usuario-agente-salao-web.streamlit.app
```

- ✅ Funciona em desktop
- ✅ Funciona em mobile
- ✅ Sem instalação
- ✅ 24/7

---

## 🔄 Atualizar o App

Para fazer mudanças:

```bash
# Edite app.py
nano app.py

# Commit e push
git add app.py
git commit -m "Atualização: novo recurso"
git push

# O Streamlit detecta e redeployar automaticamente!
```

---

## 💰 Custos

**100% GRATUITO!**

- ✅ Streamlit Cloud: gratuito
- ✅ GitHub: gratuito
- ✅ Domínio `.streamlit.app`: gratuito
- ✅ SSL/HTTPS: gratuito
- ✅ Sem limites de usuários

---

## 📊 Performance

Streamlit Cloud Free é otimizado para:
- ✅ Aplicações leves
- ✅ Uso ocasional
- ✅ Poucos usuários simultâneos

Se precisar mais:
- **Streamlit Cloud Pro** — $9/mês
- **Deploy em Heroku/Railway** — $5-10/mês

---

## 🎯 Próximos Passos

1. ✅ Publicar na web (este guia)
2. 🔜 Integrar com Telegram Bot (em desenvolvimento)
3. 🔜 Integração com Google Calendar
4. 🔜 Integração com Gmail automático
5. 🔜 Dashboard avançado

---

## 📞 Suporte

Dúvidas?
- [Documentação Streamlit](https://docs.streamlit.io)
- [Community Streamlit](https://discuss.streamlit.io)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

---

**Sucesso! Seu agente IA está no ar! 🚀**
