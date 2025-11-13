# 🎯 ESTRATÉGIA: FTD BASE + FTD PRO

> **Data:** 12/11/2025
> **Estratégia:** Duas versões para validação rápida + escala profissional

---

## 📋 VISÃO GERAL

### Por que Dois Projetos?

**Vantagens da Abordagem:**
1. ✅ **Lançamento Rápido** - Base no ar em 1-2 semanas
2. ✅ **Validação de Mercado** - Testar interesse antes de investir pesado
3. ✅ **Custo Zero** - GitHub Pages é gratuito
4. ✅ **SEO e Conteúdo** - Indexar conteúdo no Google rapidamente
5. ✅ **Landing Page** - Base pode virar vitrine do Pro
6. ✅ **Risco Reduzido** - Não investir R$ 60k+ antes de validar

---

## 🌐 PROJETO 1: FTD BASE (GITHUB PAGES)

### Características:
- **Hospedagem:** GitHub Pages (gratuito)
- **Stack:** HTML puro + Tailwind CSS CDN + Vanilla JavaScript
- **Conteúdo:** Todo o curso em páginas estáticas
- **URL:** `https://username.github.io/FTD` ou domínio customizado
- **Funcionalidades:** Apenas leitura, sem login/pagamento
- **Objetivo:** Disponibilizar conteúdo + gerar interesse

### O que TEM no Base:
✅ Landing page linda (estilo FEP)
✅ Todos os 9 módulos em páginas HTML
✅ Navegação entre aulas
✅ Design responsivo (mobile-first)
✅ Progress bar (salvando no localStorage)
✅ Accordions para tópicos
✅ Downloads de PDFs/recursos
✅ Formulário de "Quero a versão PRO" (lead capture)
✅ FAQ e sobre

### O que NÃO TEM no Base:
❌ Sistema de login/autenticação
❌ Vídeos hospedados (apenas embeds do YouTube/Vimeo)
❌ Pagamentos
❌ Comentários/comunidade
❌ Certificados
❌ Progresso sincronizado (só local)
❌ Backend/banco de dados

---

## 🚀 PROJETO 2: FTD PRO (VERCEL)

### Características:
- **Hospedagem:** Vercel (deploy automático)
- **Stack:** Next.js 14 + Supabase + Stripe + TypeScript
- **Conteúdo:** Igual ao Base + funcionalidades premium
- **URL:** `https://ftd.com.br` (domínio customizado)
- **Funcionalidades:** Tudo do Base + sistema completo
- **Objetivo:** Monetização e experiência premium

### O que TEM no Pro (além do Base):
✅ Autenticação completa (Supabase Auth)
✅ Sistema de pagamentos (Stripe)
✅ Vídeos protegidos (apenas alunos pagantes)
✅ Dashboard personalizado
✅ Progresso sincronizado na nuvem
✅ Comunidade (feed, comentários, chat)
✅ Quizzes interativos
✅ Certificados gerados automaticamente
✅ Painel administrativo completo
✅ Analytics e métricas
✅ Suporte e mentoria
✅ Área de membros

---

## 📅 CRONOGRAMA COMPARADO

### FTD BASE (2 Semanas)
```
Semana 1: Setup + Landing + 3 Módulos
Semana 2: Restante dos Módulos + Polish + Deploy
```

### FTD PRO (20 Semanas)
```
Conforme PLANO_IMPLEMENTACAO.md
(Fase 1-4: MVP → Core → Conteúdo → Lançamento)
```

### Timeline Visual:
```
Semana 1-2:   FTD BASE 🟢 (Deploy GitHub Pages)
              ↓
              Validação de mercado (30 dias)
              ↓
Semana 3-22:  FTD PRO 🔵 (Desenvolvimento paralelo)
              ↓
Semana 23:    Migração Base → Pro (redirecionar tráfego)
```

---

## 💰 INVESTIMENTO COMPARADO

### FTD BASE:
- **Desenvolvimento:** R$ 0 (você mesmo) ou R$ 3.000 (freelancer)
- **Hospedagem:** R$ 0 (GitHub Pages grátis)
- **Domínio:** R$ 40/ano (opcional)
- **Total:** R$ 0 - R$ 3.040

### FTD PRO:
- **Desenvolvimento:** R$ 25k - R$ 35k
- **Produção:** R$ 16k
- **Marketing:** R$ 18k
- **Infraestrutura:** R$ 2.5k
- **Total:** R$ 61.500 - R$ 71.500

### Economia Inicial:
**R$ 61k+** adiados até validar com o Base

---

## 🎯 ESTRATÉGIA DE MIGRAÇÃO

### Fase 1: Lançar FTD BASE
1. Publicar conteúdo completo
2. Divulgar nas redes sociais
3. Capturar leads (email)
4. Medir métricas:
   - Visitantes/dia
   - Tempo médio de sessão
   - Páginas mais acessadas
   - Conversão email (lista de espera PRO)

### Fase 2: Validação (30 dias)
- **Meta:** 1.000+ visitantes
- **Meta:** 100+ emails capturados
- **Meta:** Feedback positivo (formulário)

### Fase 3: Decisão
**SE validação positiva (100+ interessados):**
- ✅ Iniciar desenvolvimento FTD Pro
- ✅ Base vira landing page oficial
- ✅ Seguir PLANO_IMPLEMENTACAO.md

**SE validação negativa (< 50 interessados):**
- ❌ Revisar conteúdo/posicionamento
- ❌ Testar outros canais de divulgação
- ❌ Ajustar estratégia antes de investir

### Fase 4: Transição Base → Pro
Quando PRO estiver pronto:
1. Base vira landing page/preview
2. CTAs "Fazer upgrade para PRO"
3. Conteúdo completo apenas no PRO
4. Manter Base como SEO e preview gratuito

---

## 📂 ESTRUTURA DOS REPOSITÓRIOS

### Repositório 1: FTD-Base (GitHub)
```
/FTD-Base
├── /index.html              # Landing page
├── /modulos
│   ├── /modulo-1-1.html     # Impacto da IA
│   ├── /modulo-1-2.html     # Navegando no Digital
│   ├── /modulo-1-3.html     # Engenharia de Prompts
│   └── ...
├── /assets
│   ├── /css
│   │   └── styles.css       # Tailwind + custom
│   ├── /js
│   │   ├── main.js          # Navegação, localStorage
│   │   └── progress.js      # Progress tracking
│   └── /images
│       └── ...
├── /recursos                # PDFs para download
│   └── ...
├── /about.html              # Sobre o FTD
├── /faq.html                # Perguntas frequentes
└── README.md
```

### Repositório 2: FTD-Pro (Vercel)
```
/FTD-Pro
├── /app                     # Next.js 14 App Router
├── /components
├── /lib
├── /public
├── /supabase
├── .env.local
├── next.config.js
└── README.md
```

**Repos Separados:** Facilita manutenção e deploy independente

---

## 🛠️ STACK TÉCNICO DETALHADO

### FTD BASE (GitHub Pages)

#### HTML:
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FTD - Formação da Transformação Digital</title>

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <!-- Custom CSS -->
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body class="bg-gray-50 font-inter">
  <!-- Conteúdo aqui -->

  <script src="/assets/js/main.js"></script>
</body>
</html>
```

#### JavaScript (Vanilla):
```javascript
// Progress Tracking (localStorage)
const progress = {
  save: (moduleId, lessonId) => {
    const data = JSON.parse(localStorage.getItem('ftd_progress') || '{}');
    data[`${moduleId}-${lessonId}`] = true;
    localStorage.setItem('ftd_progress', JSON.stringify(data));
  },
  get: () => {
    return JSON.parse(localStorage.getItem('ftd_progress') || '{}');
  },
  percentage: () => {
    const data = progress.get();
    const total = 50; // Total de aulas
    const completed = Object.keys(data).length;
    return Math.round((completed / total) * 100);
  }
};

// Accordion Toggle
document.querySelectorAll('.accordion-button').forEach(button => {
  button.addEventListener('click', () => {
    const content = button.nextElementSibling;
    content.classList.toggle('hidden');
  });
});

// CTA Lead Capture (enviar para Google Forms ou Typeform)
document.getElementById('lead-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const email = document.getElementById('email').value;

  // Enviar para Google Forms (ação do form)
  // Ou usar Fetch API para backend simples

  alert('Obrigado! Você será notificado quando o FTD PRO for lançado.');
});
```

#### CSS (Tailwind + Custom):
```css
/* styles.css */
body {
  font-family: 'Inter', sans-serif;
}

.gradient-hero {
  background: linear-gradient(to bottom right, #3B82F6, #2563EB, #8B5CF6);
}

.card-iniciante {
  background: linear-gradient(to bottom right, #ECFDF5, #FFFFFF);
  border: 2px solid #10B981;
}

.card-iniciante:hover {
  border-color: #059669;
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
}

/* Repetir para tecnico (blue) e masterclass (purple) */
```

---

### FTD PRO (Vercel)

#### Conforme ARQUITETURA_TECNICA.md:
- Next.js 14 + TypeScript
- Supabase (Auth + DB + Storage)
- Stripe (Pagamentos)
- Tailwind CSS + shadcn/ui
- Framer Motion (animações)

---

## 🎨 PÁGINAS DO FTD BASE

### Estrutura de Navegação:
```
Home (Landing)
├── Módulo 1.1 - Impacto da IA
│   ├── Introdução
│   ├── Conceitos Básicos
│   ├── Aplicações Práticas
│   └── Exercícios
├── Módulo 1.2 - Navegando no Digital
├── Módulo 1.3 - Engenharia de Prompts
├── Módulo 1.4 - Assistentes e Agentes
├── Módulo 1.5 - Criatividade Visual
├── Módulo 1.6 - Marketing e Vendas
├── Módulo 1.7 - Automação
├── Módulo 1.8 - Inteligência Avançada
├── Módulo 1.9 - Negócios e Oportunidades
├── Sobre
├── FAQ
└── [CTA] Quero a Versão PRO
```

### Template de Página de Módulo:
```html
<!-- modulo-1-1.html -->
<nav class="sticky top-0 bg-white shadow">
  <!-- Navegação global -->
</nav>

<div class="max-w-7xl mx-auto px-4 py-8">
  <!-- Breadcrumb -->
  <nav class="text-sm mb-4">
    <a href="/">Home</a> / <span>Módulo 1.1</span>
  </nav>

  <!-- Título -->
  <h1 class="text-4xl font-bold mb-6">
    Módulo 1.1: Impacto da IA na Vida Real
  </h1>

  <!-- Progress Bar -->
  <div class="w-full h-2 bg-gray-200 rounded-full mb-8">
    <div class="h-full bg-blue-500" style="width: 25%"></div>
  </div>

  <!-- Conteúdo -->
  <div class="prose max-w-none">
    <h2>Introdução</h2>
    <p>...</p>

    <!-- Vídeo Embed -->
    <div class="aspect-video">
      <iframe src="https://www.youtube.com/embed/..." class="w-full h-full"></iframe>
    </div>

    <!-- Tópicos Expansíveis -->
    <div class="accordion-item">
      <button class="accordion-button">
        📌 Tópico 1: O que é IA?
      </button>
      <div class="accordion-content hidden">
        <p>Conteúdo aqui...</p>
      </div>
    </div>

    <!-- Recursos para Download -->
    <div class="bg-blue-50 p-6 rounded-lg mt-8">
      <h3>📚 Recursos desta Aula</h3>
      <ul>
        <li><a href="/recursos/guia-definitivo-ia.pdf">Guia Definitivo de IA (PDF)</a></li>
        <li><a href="/recursos/biblioteca-prompts.pdf">Biblioteca de Prompts (PDF)</a></li>
      </ul>
    </div>

    <!-- Navegação entre aulas -->
    <div class="flex justify-between mt-8">
      <a href="/" class="btn-secondary">← Voltar ao Início</a>
      <a href="/modulos/modulo-1-2.html" class="btn-primary">Próxima Aula →</a>
    </div>
  </div>

  <!-- Sidebar (Desktop) -->
  <aside class="hidden lg:block">
    <div class="sticky top-20">
      <h3>Conteúdo do Módulo</h3>
      <ul>
        <li class="completed">✓ Introdução</li>
        <li class="current">→ Conceitos Básicos</li>
        <li>Aplicações Práticas</li>
        <li>Exercícios</li>
      </ul>

      <!-- CTA PRO -->
      <div class="bg-gradient-to-br from-purple-50 to-white p-4 rounded-lg mt-6">
        <h4 class="font-bold">Quer Mais?</h4>
        <p class="text-sm">Acesse certificados, comunidade e suporte na versão PRO.</p>
        <button class="btn-primary w-full mt-2">
          Conhecer FTD PRO
        </button>
      </div>
    </div>
  </aside>
</div>

<footer>
  <!-- Footer -->
</footer>
```

---

## 📊 MÉTRICAS E VALIDAÇÃO

### No FTD BASE, medir:
- **Google Analytics:**
  - Visitantes únicos/dia
  - Páginas mais visitadas
  - Tempo médio de sessão
  - Taxa de rejeição
  - Funil de navegação

- **Hotjar/Microsoft Clarity:**
  - Heatmaps de cliques
  - Gravações de sessão
  - Onde as pessoas abandonam

- **Lead Capture:**
  - Taxa de conversão (visitante → email)
  - Origem do tráfego (orgânico, redes sociais, etc)

### Metas de Validação (30 dias):
- ✅ 1.000+ visitantes únicos
- ✅ 100+ emails capturados (10% conversão)
- ✅ 5+ minutos de tempo médio de sessão
- ✅ 50%+ das pessoas visitam 3+ páginas

**SE atingir metas:** Luz verde para FTD Pro 🚀

---

## 🚀 VANTAGENS DESTA ESTRATÉGIA

### 1. **Risco Reduzido**
- Investir R$ 0-3k (Base) vs R$ 60k+ (Pro)
- Validar antes de comprometer recursos

### 2. **Lançamento Rápido**
- Base no ar em 2 semanas
- Começar a capturar leads imediatamente

### 3. **SEO e Autoridade**
- Conteúdo indexado no Google
- Gerar tráfego orgânico
- Construir autoridade no nicho

### 4. **Feedback Real**
- Entender o que as pessoas mais buscam
- Ajustar conteúdo antes do Pro
- Identificar gaps e oportunidades

### 5. **Dupla Monetização**
- Base: Gratuito (geração de leads)
- Pro: Pago (conversão de leads em clientes)

### 6. **Flexibilidade**
- Se Base falhar, parar sem grandes perdas
- Se Base funcionar, ter lista de espera já aquecida

---

## 🎯 PRÓXIMOS PASSOS IMEDIATOS

### ESTA SEMANA (FTD BASE):

#### Dia 1-2: Setup
- [ ] Criar repo GitHub "FTD-Base"
- [ ] Estrutura de pastas
- [ ] Template HTML base
- [ ] Configurar Tailwind CDN
- [ ] Landing page (hero + níveis + CTA)

#### Dia 3-4: Primeiros Módulos
- [ ] Converter Módulo 1.1 para HTML
- [ ] Converter Módulo 1.2 para HTML
- [ ] Converter Módulo 1.3 para HTML
- [ ] Testar navegação e responsividade

#### Dia 5: Deploy
- [ ] Configurar GitHub Pages
- [ ] Publicar em `username.github.io/FTD-Base`
- [ ] Testar em produção
- [ ] Ajustar bugs

#### Weekend: Conteúdo Restante
- [ ] Converter Módulos 1.4 a 1.9
- [ ] Criar página FAQ
- [ ] Criar página Sobre
- [ ] Formulário de lead capture

### PRÓXIMA SEMANA:
- [ ] Polish e refinamento
- [ ] Adicionar Google Analytics
- [ ] Adicionar Hotjar/Clarity
- [ ] Criar posts de divulgação
- [ ] Lançar nas redes sociais
- [ ] **FTD BASE LIVE** 🚀

---

## 📞 DECISÃO: QUANDO INICIAR FTD PRO?

### Critérios de Go/No-Go:

**GO (Iniciar Pro):**
- ✅ 100+ emails capturados em 30 dias
- ✅ Feedback positivo (80%+ dos comentários)
- ✅ Pessoas pedindo funcionalidades premium
- ✅ Tráfego crescente (curva ascendente)

**NO-GO (Revisar estratégia):**
- ❌ < 50 emails em 30 dias
- ❌ Feedback negativo ou indiferente
- ❌ Taxa de rejeição > 80%
- ❌ Tempo de sessão < 2 minutos

---

## 🎉 RESUMO EXECUTIVO

### Estratégia em 3 Frases:
1. **Lançar FTD Base** (GitHub Pages, gratuito, 2 semanas) para validar mercado
2. **Medir interesse** real por 30 dias (meta: 100+ leads)
3. **SE validado:** Investir em FTD Pro (Vercel, pago, 20 semanas)

### Benefícios:
- ✅ Custo inicial próximo de zero
- ✅ Validação antes de investir pesado
- ✅ SEO e autoridade desde o início
- ✅ Lista de espera aquecida para o Pro
- ✅ Flexibilidade para pivotar se necessário

---

**Quer que eu crie a estrutura inicial do FTD Base agora? Posso gerar os primeiros HTMLs! 🚀**
