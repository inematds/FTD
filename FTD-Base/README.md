# FTD Base - Site Estático

> **Versão gratuita e de validação do curso FTD**
>
> Este é o site estático do FTD (Formação da Transformação Digital), hospedado no GitHub Pages.

---

## 📋 Sobre o FTD Base

O **FTD Base** é a versão gratuita e simplificada do curso FTD, criada para:

1. **Validar o mercado** - Testar interesse e demanda antes de investir no sistema completo
2. **Gerar leads** - Capturar contatos interessados no FTD Pro
3. **Apresentar conteúdo** - Disponibilizar material introdutório gratuitamente
4. **SEO e Alcance** - Posicionar a marca nos mecanismos de busca
5. **Prova de conceito** - Demonstrar a qualidade e estrutura do curso

---

## 🎯 Diferenças: Base vs Pro

| Característica | FTD Base | FTD Pro |
|----------------|----------|---------|
| **Hospedagem** | GitHub Pages (grátis) | Vercel + Supabase |
| **Tecnologia** | HTML + Tailwind CDN | Next.js 14 + TypeScript |
| **Vídeos** | Placeholders (teasers) | Aulas completas (100+ horas) |
| **Interatividade** | Básica (localStorage) | Completa (autenticação, progresso, certificados) |
| **Pagamentos** | Não tem | Stripe integrado |
| **Comunidade** | Link externo | Fórum integrado |
| **Custo** | R$ 0 | R$ 61k+ desenvolvimento |

---

## 🏗️ Estrutura do Projeto

```
FTD-Base/
├── index.html              # Landing page principal
├── modulos/                # Páginas dos módulos
│   ├── modulo-1-1.html     # Impacto da IA na Vida Real
│   ├── modulo-1-2.html     # Navegando no Novo Mundo Digital
│   ├── modulo-1-3.html     # Engenharia de Prompts
│   ├── modulo-1-4.html     # Assistentes e Agentes
│   ├── modulo-1-5.html     # Criatividade Visual com IA
│   ├── modulo-1-6.html     # Marketing e Vendas
│   ├── modulo-1-7.html     # Começando com Automação
│   ├── modulo-1-8.html     # Inteligência Avançada (RAG)
│   └── modulo-1-9.html     # Negócios e Oportunidades
├── assets/
│   ├── css/
│   │   └── styles.css      # Estilos customizados
│   ├── js/
│   │   └── main.js         # JavaScript (tracking, interações)
│   └── images/             # Imagens e logos
├── recursos/               # PDFs e materiais para download
├── sobre.html              # Página Sobre
├── faq.html                # FAQ
└── README.md               # Este arquivo
```

---

## 🚀 Tecnologias Utilizadas

### Frontend:
- **HTML5** - Estrutura semântica
- **Tailwind CSS** (via CDN) - Estilização responsiva
- **Vanilla JavaScript** - Interatividade leve
- **Google Fonts** (Inter) - Tipografia

### Funcionalidades JavaScript:
- ✅ **Progress Tracking** - Salvamento local de progresso (localStorage)
- ✅ **Mobile Menu** - Navegação responsiva
- ✅ **Smooth Scroll** - Navegação suave entre seções
- ✅ **Form Validation** - Validação de formulários de lead
- ✅ **Task Checkboxes** - Marcar atividades como concluídas
- ✅ **Accordions** - Seções expansíveis de conteúdo

### Design System:
```css
/* Cores dos níveis */
--color-iniciante: #10B981   (Verde Emerald)
--color-tecnico: #3B82F6     (Azul Blue)
--color-masterclass: #8B5CF6 (Roxo Purple)

/* Gradientes */
--gradient-hero: linear-gradient(135deg, #3B82F6 → #1E40AF → #8B5CF6)
```

---

## 📦 Como Rodar Localmente

### Opção 1: Abrir diretamente no navegador
```bash
# Navegue até a pasta
cd FTD-Base

# Abra o index.html no navegador
open index.html
# ou
xdg-open index.html  # Linux
# ou
start index.html     # Windows
```

### Opção 2: Servidor HTTP local
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js (npx)
npx http-server -p 8000

# Acesse: http://localhost:8000
```

---

## 🌐 Deploy no GitHub Pages

### Passo 1: Criar repositório no GitHub
```bash
# Inicializar Git
git init

# Adicionar remote
git remote add origin https://github.com/SEU-USUARIO/ftd-base.git

# Commit inicial
git add .
git commit -m "feat: Adiciona estrutura inicial do FTD Base"

# Push para main
git branch -M main
git push -u origin main
```

### Passo 2: Ativar GitHub Pages
1. Vá em **Settings** do repositório
2. Navegue até **Pages**
3. Em **Source**, selecione `main` branch e `/` (root)
4. Clique em **Save**
5. Aguarde alguns minutos

### Passo 3: Acessar o site
```
https://SEU-USUARIO.github.io/ftd-base/
```

### Passo 4: (Opcional) Domínio customizado
1. Compre um domínio (ex: `ftdcurso.com.br`)
2. Configure DNS:
   - Adicione registro `CNAME` apontando para `SEU-USUARIO.github.io`
3. No GitHub Pages, adicione o custom domain
4. Aguarde propagação DNS (até 24h)

---

## 📊 Funcionalidades Principais

### 1. Progress Tracking
- Salva progresso localmente (localStorage)
- Marca módulos e tarefas como concluídos
- Barra de progresso visual
- Persiste entre sessões

```javascript
// Exemplo de uso
progressTracker.markModuleComplete('modulo-1-1');
progressTracker.getCompletionPercentage(); // Retorna 0-100
```

### 2. Lead Capture
- Formulário de cadastro na landing page
- Validação de email
- Salva localmente (preparado para integração futura)

### 3. Mobile-First Design
- Totalmente responsivo
- Menu hambúrguer em mobile
- Touch-friendly
- Performance otimizada

---

## 🎨 Customização

### Alterar Cores
Edite `assets/css/styles.css`:
```css
:root {
    --color-iniciante: #10B981;   /* Verde */
    --color-tecnico: #3B82F6;     /* Azul */
    --color-masterclass: #8B5CF6; /* Roxo */
}
```

### Adicionar Novos Módulos
1. Copie um arquivo de módulo existente (ex: `modulo-1-1.html`)
2. Renomeie (ex: `modulo-1-10.html`)
3. Atualize conteúdo, título e navegação
4. Adicione link no `index.html` e na sidebar

### Integrar Analytics
Adicione no `<head>` de todas as páginas:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 📈 Métricas para Validação

### O que medir (primeiros 30 dias):

1. **Tráfego**
   - Visitantes únicos
   - Pageviews
   - Taxa de rejeição
   - Tempo na página

2. **Leads**
   - Número de cadastros
   - Taxa de conversão (visitantes → leads)
   - Origem do tráfego

3. **Engajamento**
   - Módulos mais acessados
   - Taxa de conclusão de atividades
   - Tempo médio por módulo

4. **Feedback**
   - Comentários via formulário
   - Compartilhamentos sociais
   - Pedidos de informação sobre FTD Pro

### Meta de Validação:
- ✅ **100+ visitantes únicos/semana** = Interesse inicial
- ✅ **50+ leads cadastrados** = Demanda real
- ✅ **10+ pedidos de informação Pro** = Validação de mercado
- ✅ **Taxa conversão > 3%** = Funil saudável

**Se atingir essas metas → Seguir com FTD Pro!**

---

## 🔄 Migração para FTD Pro

Quando validar o mercado, a transição será:

### 1. Manter FTD Base
- Continua no ar como versão gratuita
- Serve de funil de entrada
- Gera leads continuamente

### 2. Desenvolver FTD Pro
- Sistema completo (Next.js + Supabase)
- Videoaulas completas
- Pagamentos integrados
- Certificados e gamificação

### 3. Integração
```
FTD Base (gratuito)
    ↓
Lead capture
    ↓
Email marketing
    ↓
Lançamento FTD Pro
    ↓
Conversão para pago
```

---

## 📞 Próximos Passos

### Imediatos (Esta Semana):
1. ✅ Estrutura HTML criada
2. ✅ CSS e JavaScript implementados
3. ✅ Primeiros 3 módulos prontos
4. ⏳ Completar os 9 módulos
5. ⏳ Criar páginas Sobre e FAQ
6. ⏳ Testar responsividade
7. ⏳ Deploy no GitHub Pages

### Primeira Semana Pós-Lançamento:
1. ⏳ Configurar Google Analytics
2. ⏳ Integrar formulário com serviço de email (Mailchimp/ConvertKit)
3. ⏳ Criar sequência de emails automática
4. ⏳ Anunciar nas redes sociais
5. ⏳ Buscar primeiros 100 visitantes

### Primeiro Mês:
1. ⏳ Coletar feedback de usuários
2. ⏳ Ajustar conteúdo baseado em métricas
3. ⏳ Criar conteúdo de blog (SEO)
4. ⏳ Validar interesse em FTD Pro
5. ⏳ Decidir sobre desenvolvimento do Pro

---

## 🐛 Issues Conhecidos

### Limitações do FTD Base:
- [ ] Vídeos são apenas placeholders (não há conteúdo real ainda)
- [ ] Progress tracking é local (não sincroniza entre dispositivos)
- [ ] Formulário salva localmente (precisa integração com backend para email)
- [ ] Sem autenticação real
- [ ] Sem certificados automatizados

**Essas limitações são INTENCIONAIS para manter o projeto simples e validar antes de investir!**

---

## 🤝 Contribuindo

Este é um projeto privado, mas se você for parte da equipe:

1. Crie um branch para sua feature
2. Faça commit com mensagens claras
3. Abra Pull Request
4. Aguarde review

### Padrão de commits:
```
feat: Adiciona novo módulo X
fix: Corrige bug no formulário
docs: Atualiza README
style: Ajusta espaçamento do header
refactor: Melhora código do progress tracker
```

---

## 📝 Licença

© 2025 INEMA TDS - Todos os direitos reservados.

Conteúdo proprietário para uso no curso FTD.

---

## 🎉 Status Atual

### ✅ Concluído:
- [x] Estrutura de pastas
- [x] Landing page (index.html)
- [x] Design system completo
- [x] CSS customizado (styles.css)
- [x] JavaScript principal (main.js)
- [x] Módulo 1.1 - Impacto da IA
- [x] Módulo 1.2 - Mundo Digital
- [x] Módulo 1.3 - Engenharia de Prompts

### ⏳ Em Andamento:
- [ ] Módulo 1.4 - Assistentes e Agentes
- [ ] Módulo 1.5 - Criatividade Visual
- [ ] Módulo 1.6 - Marketing e Vendas
- [ ] Módulo 1.7 - Automação
- [ ] Módulo 1.8 - Inteligência Avançada
- [ ] Módulo 1.9 - Negócios

### 📅 Próximos:
- [ ] Páginas auxiliares (sobre.html, faq.html)
- [ ] Adicionar PDFs na pasta recursos/
- [ ] Testes de responsividade
- [ ] Deploy GitHub Pages
- [ ] Configurar Analytics

---

**Pronto para validar o mercado e transformar vidas com educação digital! 🚀**

---

<p align="center">
  <strong>Dúvidas?</strong><br>
  Consulte a <a href="../docs/ARQUITETURA_TECNICA.md">Arquitetura Técnica</a> ou o <a href="../PLANO_IMPLEMENTACAO.md">Plano de Implementação</a>
</p>

<p align="center">
  Criado com 💙 por <strong>INEMA TDS</strong>
</p>
