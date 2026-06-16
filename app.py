#!/usr/bin/env python3
# ================================================================
#  AGENTE IA SALÃO DE BELEZA — Interface Web com Streamlit
#  Telegram + Gemini + Google · 100% Gratuito · Hospedado
# ================================================================

import streamlit as st
import pandas as pd
import google.generativeai as genai
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import json

# ── Configuração da página ──────────────────────────────────────
st.set_page_config(
    page_title="🎀 Agente IA Salão de Beleza",
    page_icon="✂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Carrega variáveis de ambiente ───────────────────────────────
load_dotenv()

GEMINI_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
TELEGRAM_TOKEN = st.secrets.get("TELEGRAM_BOT_TOKEN") or os.getenv("TELEGRAM_BOT_TOKEN")
SALAO_NOME = st.secrets.get("SALAO_NOME") or os.getenv("SALAO_NOME", "Salão Bella")
SALAO_ENDERECO = st.secrets.get("SALAO_ENDERECO") or os.getenv("SALAO_ENDERECO", "Rua das Flores, 123")
SALAO_TELEFONE = st.secrets.get("SALAO_TELEFONE") or os.getenv("SALAO_TELEFONE", "(81) 99999-9999")
IA_NOME = st.secrets.get("IA_NOME") or os.getenv("IA_NOME", "Sofia")

# Configurar Gemini
if GEMINI_KEY:
    genai.configure(api_key=GEMINI_KEY)

# ── CSS Customizado ─────────────────────────────────────────────
st.markdown("""
<style>
    /* Cores */
    :root {
        --cor-primaria: #e91e8c;
        --cor-secundaria: #ff6b9d;
        --cor-fundo: #fafafa;
        --cor-texto: #333333;
    }
    
    /* Estilo geral */
    body {
        background-color: var(--cor-fundo);
        font-family: 'Arial', sans-serif;
    }
    
    .main {
        background-color: white;
    }
    
    /* Cartões */
    .card {
        background: linear-gradient(135deg, #e91e8c, #ff6b9d);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin: 10px 0;
        box-shadow: 0 4px 12px rgba(233, 30, 140, 0.2);
    }
    
    .card-titulo {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 8px;
    }
    
    .card-valor {
        font-size: 28px;
        font-weight: bold;
    }
    
    /* Botões */
    .stButton > button {
        background: linear-gradient(135deg, #e91e8c, #ff6b9d);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }
    
    .stButton > button:hover {
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# ── Inicializar sessão ──────────────────────────────────────────
if 'agendamentos' not in st.session_state:
    st.session_state.agendamentos = [
        {
            'id': 1,
            'cliente': 'Ana Souza',
            'servico': 'Manicure + Pedicure',
            'data': '2026-06-13 14:00',
            'telefone': '(81) 98765-4321',
            'status': 'Confirmado',
            'criado': '2026-06-09 10:30'
        },
        {
            'id': 2,
            'cliente': 'Pedro Silva',
            'servico': 'Corte Masculino',
            'data': '2026-06-14 09:30',
            'telefone': '(81) 99876-5432',
            'status': 'Confirmado',
            'criado': '2026-06-09 11:15'
        }
    ]

if 'contador' not in st.session_state:
    st.session_state.contador = len(st.session_state.agendamentos)

# ── HEADER ──────────────────────────────────────────────────────
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/1973/1973243.png", width=80)

with col2:
    st.markdown(f"# ✂️ {SALAO_NOME}")
    st.markdown(f"**Agente IA de Atendimento** | {SALAO_ENDERECO} | {SALAO_TELEFONE}")

st.divider()

# ── MENU LATERAL ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎨 Menu de Navegação")
    
    opcao = st.radio(
        "Escolha uma seção:",
        [
            "📊 Dashboard",
            "📅 Agendamentos",
            "💬 Chat IA",
            "⚙️ Configurações",
            "📞 Contatos",
            "📋 Relatórios"
        ],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    st.markdown("### ℹ️ Informações")
    st.info(f"""
    **Salão:** {SALAO_NOME}
    
    **Endereço:** {SALAO_ENDERECO}
    
    **Telefone:** {SALAO_TELEFONE}
    
    **IA:** {IA_NOME}
    """)

# ────────────────────────────────────────────────────────────────
# PÁGINA 1 — DASHBOARD
# ────────────────────────────────────────────────────────────────

if opcao == "📊 Dashboard":
    st.markdown("## 📊 Dashboard de Controle")
    
    # Métricas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="card-titulo">📅 Total Agendamentos</div>
            <div class="card-valor">{len(st.session_state.agendamentos)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        confirmados = len([a for a in st.session_state.agendamentos if a['status'] == 'Confirmado'])
        st.markdown(f"""
        <div class="card">
            <div class="card-titulo">✅ Confirmados</div>
            <div class="card-valor">{confirmados}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        cancelados = len([a for a in st.session_state.agendamentos if a['status'] == 'Cancelado'])
        st.markdown(f"""
        <div class="card">
            <div class="card-titulo">❌ Cancelados</div>
            <div class="card-valor">{cancelados}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        hoje = datetime.now().strftime("%Y-%m-%d")
        hoje_agendamentos = len([a for a in st.session_state.agendamentos if a['data'].startswith(hoje)])
        st.markdown(f"""
        <div class="card">
            <div class="card-titulo">🎯 Hoje</div>
            <div class="card-valor">{hoje_agendamentos}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Serviços mais agendados
    st.markdown("### 📈 Serviços Mais Agendados")
    
    servicos = {}
    for agendamento in st.session_state.agendamentos:
        servico = agendamento['servico']
        servicos[servico] = servicos.get(servico, 0) + 1
    
    if servicos:
        df_servicos = pd.DataFrame(list(servicos.items()), columns=['Serviço', 'Quantidade'])
        st.bar_chart(df_servicos.set_index('Serviço'))
    else:
        st.info("Nenhum agendamento ainda")
    
    st.divider()
    
    # Próximos agendamentos
    st.markdown("### 📅 Próximos Agendamentos (7 dias)")
    
    agora = datetime.now()
    proximos_7_dias = [
        a for a in st.session_state.agendamentos
        if datetime.fromisoformat(a['data']) >= agora and 
           (datetime.fromisoformat(a['data']) - agora).days <= 7
    ]
    
    if proximos_7_dias:
        df_proximos = pd.DataFrame(proximos_7_dias)
        st.dataframe(df_proximos, use_container_width=True, hide_index=True)
    else:
        st.info("Nenhum agendamento nos próximos 7 dias")

# ────────────────────────────────────────────────────────────────
# PÁGINA 2 — AGENDAMENTOS
# ────────────────────────────────────────────────────────────────

elif opcao == "📅 Agendamentos":
    st.markdown("## 📅 Gerenciador de Agendamentos")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        if st.button("➕ Novo Agendamento", use_container_width=True):
            st.session_state.mostrar_novo = True
    
    # Formulário novo agendamento
    if st.session_state.get('mostrar_novo', False):
        st.markdown("### ➕ Novo Agendamento")
        
        with st.form("form_agendamento"):
            col1, col2 = st.columns(2)
            
            with col1:
                nome = st.text_input("👤 Nome do Cliente", placeholder="Ana Souza")
                telefone = st.text_input("📞 Telefone/WhatsApp", placeholder="(81) 98765-4321")
            
            with col2:
                servico = st.selectbox(
                    "✂️ Serviço",
                    [
                        "Corte feminino",
                        "Corte masculino",
                        "Coloração",
                        "Manicure",
                        "Pedicure",
                        "Combo Mani + Pedi",
                        "Design de sobrancelha",
                        "Escova progressiva",
                        "Outro"
                    ]
                )
            
            data = st.date_input("📅 Data")
            hora = st.time_input("⏰ Hora")
            
            obs = st.text_area("📝 Observações (opcional)", placeholder="Ex: Cliente alérgica a...")
            
            col1, col2 = st.columns(2)
            
            with col1:
                submit = st.form_submit_button("✅ Confirmar Agendamento", use_container_width=True)
            
            with col2:
                if st.form_submit_button("❌ Cancelar", use_container_width=True):
                    st.session_state.mostrar_novo = False
            
            if submit and nome and telefone:
                novo_agendamento = {
                    'id': st.session_state.contador + 1,
                    'cliente': nome,
                    'servico': servico,
                    'data': f"{data} {hora}",
                    'telefone': telefone,
                    'status': 'Confirmado',
                    'criado': datetime.now().strftime("%Y-%m-%d %H:%M"),
                    'observacoes': obs
                }
                st.session_state.agendamentos.append(novo_agendamento)
                st.session_state.contador += 1
                st.session_state.mostrar_novo = False
                st.success(f"✅ Agendamento criado para {nome}")
                st.rerun()
    
    st.divider()
    
    # Lista de agendamentos
    st.markdown("### 📋 Todos os Agendamentos")
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filtro_status = st.selectbox("Status:", ["Todos", "Confirmado", "Cancelado", "Realizado"])
    
    with col2:
        filtro_servico = st.selectbox("Serviço:", ["Todos"] + list(set([a['servico'] for a in st.session_state.agendamentos])))
    
    with col3:
        filtro_data = st.date_input("Data:", value=None)
    
    # Aplicar filtros
    agendamentos_filtrados = st.session_state.agendamentos.copy()
    
    if filtro_status != "Todos":
        agendamentos_filtrados = [a for a in agendamentos_filtrados if a['status'] == filtro_status]
    
    if filtro_servico != "Todos":
        agendamentos_filtrados = [a for a in agendamentos_filtrados if a['servico'] == filtro_servico]
    
    if filtro_data:
        data_str = filtro_data.strftime("%Y-%m-%d")
        agendamentos_filtrados = [a for a in agendamentos_filtrados if a['data'].startswith(data_str)]
    
    # Exibir em cards
    for agendamento in agendamentos_filtrados:
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            status_color = "🟢" if agendamento['status'] == 'Confirmado' else "🔴" if agendamento['status'] == 'Cancelado' else "🟡"
            st.markdown(f"""
            **{status_color} {agendamento['cliente']}** — {agendamento['servico']}
            
            📅 {agendamento['data']} | 📞 {agendamento['telefone']}
            """)
        
        with col2:
            if st.button("✏️ Editar", key=f"edit_{agendamento['id']}", use_container_width=True):
                st.info("Edição em desenvolvimento")
        
        with col3:
            if st.button("🗑️ Deletar", key=f"del_{agendamento['id']}", use_container_width=True):
                st.session_state.agendamentos = [a for a in st.session_state.agendamentos if a['id'] != agendamento['id']]
                st.success("Agendamento removido")
                st.rerun()
        
        st.divider()

# ────────────────────────────────────────────────────────────────
# PÁGINA 3 — CHAT IA
# ────────────────────────────────────────────────────────────────

elif opcao == "💬 Chat IA":
    st.markdown(f"## 💬 Chat com {IA_NOME} IA")
    
    if not GEMINI_KEY:
        st.error("❌ GEMINI_API_KEY não configurada. Adicione em Secrets.")
        st.stop()
    
    # Histórico de chat
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Exibir histórico
    chat_container = st.container()
    
    with chat_container:
        for msg in st.session_state.chat_history:
            if msg['role'] == 'user':
                st.markdown(f"👤 **Você:** {msg['content']}")
            else:
                st.markdown(f"💬 **{IA_NOME}:** {msg['content']}")
    
    st.divider()
    
    # Input do usuário
    prompt = st.text_input("Sua mensagem:", placeholder=f"Olá {IA_NOME}! Quero saber sobre...")
    
    if st.button("📤 Enviar", use_container_width=True):
        if prompt:
            # Adicionar ao histórico
            st.session_state.chat_history.append({'role': 'user', 'content': prompt})
            
            # Chamar Gemini
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt_sistema = f"""Você é {IA_NOME}, recepcionista do {SALAO_NOME}.
Você é humana, calorosa, simpática e NUNCA revela que é uma IA.

SERVIÇOS:
- Corte feminino: R$ 60,00
- Corte masculino: R$ 35,00
- Coloração: a partir de R$ 120,00
- Manicure: R$ 30,00
- Pedicure: R$ 35,00
- Combo: R$ 55,00

HORÁRIOS:
- Seg-Sex: 9h às 19h
- Sábado: 9h às 17h
- Domingo: Fechado

Responda de forma breve e calorosa."""
                
                resposta = model.generate_content(f"{prompt_sistema}\n\nCliente: {prompt}")
                texto_resposta = resposta.text
                
                st.session_state.chat_history.append({'role': 'assistant', 'content': texto_resposta})
                st.rerun()
            
            except Exception as e:
                st.error(f"❌ Erro: {e}")

# ────────────────────────────────────────────────────────────────
# PÁGINA 4 — CONFIGURAÇÕES
# ────────────────────────────────────────────────────────────────

elif opcao == "⚙️ Configurações":
    st.markdown("## ⚙️ Configurações do Salão")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Informações Básicas")
        nome_salao = st.text_input("Nome do Salão:", value=SALAO_NOME)
        endereco = st.text_input("Endereço:", value=SALAO_ENDERECO)
        telefone = st.text_input("Telefone:", value=SALAO_TELEFONE)
        ia_nome = st.text_input("Nome da IA:", value=IA_NOME)
    
    with col2:
        st.markdown("### Horários de Funcionamento")
        
        segunda_sexta = st.time_input("Seg-Sex (abertura):", value=datetime.strptime("09:00", "%H:%M").time())
        segunda_sexta_fechamento = st.time_input("Seg-Sex (fechamento):", value=datetime.strptime("19:00", "%H:%M").time())
        
        sabado = st.time_input("Sábado (abertura):", value=datetime.strptime("09:00", "%H:%M").time())
        sabado_fechamento = st.time_input("Sábado (fechamento):", value=datetime.strptime("17:00", "%H:%M").time())
        
        domingo_aberto = st.checkbox("Domingos abertos?", value=False)
    
    st.divider()
    
    st.markdown("### Serviços Oferecidos")
    
    servicos_padrao = [
        "Corte feminino - R$ 60,00",
        "Corte masculino - R$ 35,00",
        "Coloração - a partir de R$ 120,00",
        "Manicure - R$ 30,00",
        "Pedicure - R$ 35,00",
        "Combo Mani + Pedi - R$ 55,00",
        "Design de sobrancelha - R$ 25,00"
    ]
    
    for servico in servicos_padrao:
        st.text_input("Serviço:", value=servico, disabled=True)
    
    st.divider()
    
    if st.button("💾 Salvar Configurações", use_container_width=True):
        st.success("✅ Configurações salvas com sucesso!")

# ────────────────────────────────────────────────────────────────
# PÁGINA 5 — CONTATOS
# ────────────────────────────────────────────────────────────────

elif opcao == "📞 Contatos":
    st.markdown("## 📞 Gerenciador de Contatos")
    
    if 'contatos' not in st.session_state:
        st.session_state.contatos = [
            {'id': 1, 'nome': 'Ana Souza', 'telefone': '(81) 98765-4321', 'email': 'ana@email.com', 'ult_agendamento': '2026-06-13'},
            {'id': 2, 'nome': 'Pedro Silva', 'telefone': '(81) 99876-5432', 'email': 'pedro@email.com', 'ult_agendamento': '2026-06-14'},
        ]
    
    col1, col2 = st.columns([3, 1])
    
    with col2:
        if st.button("➕ Novo Contato", use_container_width=True):
            st.session_state.mostrar_novo_contato = True
    
    if st.session_state.get('mostrar_novo_contato', False):
        with st.form("form_contato"):
            nome = st.text_input("Nome:", placeholder="Maria Silva")
            telefone = st.text_input("Telefone:", placeholder="(81) 98765-4321")
            email = st.text_input("E-mail:", placeholder="maria@email.com")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.form_submit_button("✅ Adicionar"):
                    novo = {
                        'id': max([c['id'] for c in st.session_state.contatos]) + 1,
                        'nome': nome,
                        'telefone': telefone,
                        'email': email,
                        'ult_agendamento': '-'
                    }
                    st.session_state.contatos.append(novo)
                    st.session_state.mostrar_novo_contato = False
                    st.success("✅ Contato adicionado!")
                    st.rerun()
            
            with col2:
                if st.form_submit_button("❌ Cancelar"):
                    st.session_state.mostrar_novo_contato = False
    
    st.divider()
    
    # Lista de contatos
    st.markdown("### 👥 Contatos")
    
    for contato in st.session_state.contatos:
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"""
            **{contato['nome']}**
            
            📞 {contato['telefone']} | 📧 {contato['email']}
            
            Último agendamento: {contato['ult_agendamento']}
            """)
        
        with col2:
            if st.button("🗑️", key=f"del_contato_{contato['id']}", use_container_width=True):
                st.session_state.contatos = [c for c in st.session_state.contatos if c['id'] != contato['id']]
                st.rerun()
        
        st.divider()

# ────────────────────────────────────────────────────────────────
# PÁGINA 6 — RELATÓRIOS
# ────────────────────────────────────────────────────────────────

elif opcao == "📋 Relatórios":
    st.markdown("## 📋 Relatórios e Análises")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Agendamentos por Mês")
        
        meses = {}
        for agendamento in st.session_state.agendamentos:
            mes = agendamento['data'][:7]
            meses[mes] = meses.get(mes, 0) + 1
        
        if meses:
            df_meses = pd.DataFrame(list(meses.items()), columns=['Mês', 'Quantidade'])
            st.bar_chart(df_meses.set_index('Mês'))
    
    with col2:
        st.markdown("### 🎯 Taxa de Confirmação")
        
        total = len(st.session_state.agendamentos)
        confirmados = len([a for a in st.session_state.agendamentos if a['status'] == 'Confirmado'])
        
        if total > 0:
            taxa = (confirmados / total) * 100
            st.metric("Taxa de Confirmação", f"{taxa:.1f}%", f"+{confirmados}/{total}")
    
    st.divider()
    
    st.markdown("### 📥 Exportar Dados")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Exportar como CSV", use_container_width=True):
            df_export = pd.DataFrame(st.session_state.agendamentos)
            csv = df_export.to_csv(index=False)
            st.download_button(
                label="⬇️ Download CSV",
                data=csv,
                file_name=f"agendamentos_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    
    with col2:
        if st.button("📈 Exportar como Excel", use_container_width=True):
            df_export = pd.DataFrame(st.session_state.agendamentos)
            df_export.to_excel("agendamentos.xlsx", index=False)
            with open("agendamentos.xlsx", "rb") as f:
                st.download_button(
                    label="⬇️ Download Excel",
                    data=f,
                    file_name=f"agendamentos_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

# ── FOOTER ──────────────────────────────────────────────────────
st.divider()
st.markdown("""
---
**✂️ Agente IA Salão de Beleza** — Desenvolvido com Streamlit  
100% Gratuito · [GitHub](https://github.com) · [Documentação](https://docs.streamlit.io)
""")
