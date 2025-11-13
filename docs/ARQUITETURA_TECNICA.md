# 🏗️ ARQUITETURA TÉCNICA DA PLATAFORMA FTD
## Sistema Completo de Educação Digital

> **Versão:** 1.0
> **Data:** 2025-11-12
> **Arquiteto:** INEMA TDS
> **Stack:** Next.js 14 + Tailwind CSS + Supabase + Stripe

---

## 📋 VISÃO GERAL

### Objetivo da Plataforma
Criar uma **plataforma educacional moderna, escalável e performática** para entregar o curso FTD com experiência excepcional para os alunos.

### Requisitos Principais
- ✅ Interface responsiva e acessível (mobile-first)
- ✅ Sistema de autenticação e gestão de usuários
- ✅ Conteúdo em vídeo com player avançado
- ✅ Acompanhamento de progresso
- ✅ Sistema de pagamentos
- ✅ Comunidade e interação
- ✅ Painel administrativo completo
- ✅ Performance otimizada (SEO, velocidade)

---

## 🎨 DESIGN SYSTEM

### Referência de Estilos (FEP_STYLE_REFERENCE.md)

#### Cores por Nível:
```css
🌟 Nível Iniciante:   #10B981  (Verde Emerald 500)
⚡ Nível Técnico:      #3B82F6  (Azul Blue 500)
👑 Nível Masterclass:  #8B5CF6  (Roxo Purple 500)
```

#### Paleta Completa:
```css
--primary:        #3B82F6   /* Blue 600 */
--primary-dark:   #2563EB   /* Blue 700 */
--accent:         #6366F1   /* Indigo 500 */
--iniciante:      #10B981   /* Verde */
--tecnico:        #3B82F6   /* Azul */
--masterclass:    #8B5CF6   /* Roxo */
--gray-50:        #F9FAFB
--gray-900:       #1F2937
```

#### Tipografia:
```css
Fonte: 'Inter' (Google Fonts)
H1: 4rem (64px) - font-weight: 700
H2: 2.5rem (40px) - font-weight: 700
H3: 1.875rem (30px) - font-weight: 700
Body: 1rem (16px) - font-weight: 400
```

#### Componentes Principais:
- Navegação sticky
- Hero com gradiente
- Cards de nível com hover effects
- Botões primários e secundários
- Modais
- Progress bars
- Accordions (tópicos expansíveis)
- Badges
- Footer responsivo

---

## 🏛️ ARQUITETURA GERAL

### Stack Tecnológico

#### **Frontend:**
- **Framework:** Next.js 14 (App Router)
- **Linguagem:** TypeScript
- **Estilização:** Tailwind CSS 3.x
- **UI Components:** shadcn/ui
- **Ícones:** Lucide React
- **Animações:** Framer Motion
- **Forms:** React Hook Form + Zod
- **State Management:** Zustand
- **Player de Vídeo:** Plyr.io ou Video.js

#### **Backend:**
- **BaaS:** Supabase
  - Authentication (Auth)
  - Database (PostgreSQL)
  - Storage (Arquivos/Vídeos)
  - Realtime (Comentários, Chat)
  - Edge Functions (Serverless)

#### **Pagamentos:**
- **Stripe** (Cartão de crédito, Pix via API)
- **Webhooks** para confirmação automática

#### **Hospedagem:**
- **Frontend:** Vercel (deploy automático)
- **Vídeos:** Supabase Storage ou Vimeo API
- **CDN:** Cloudflare (cache e performance)

#### **Analytics:**
- Google Analytics 4
- Hotjar (heatmaps)
- Mixpanel (eventos customizados)

---

## 🗄️ MODELO DE DADOS

### Schema do Banco de Dados (Supabase/PostgreSQL)

```sql
-- Tabela: users (gerenciada pelo Supabase Auth)
-- id, email, created_at, etc.

-- Tabela: profiles
CREATE TABLE profiles (
  id UUID REFERENCES auth.users PRIMARY KEY,
  full_name TEXT,
  avatar_url TEXT,
  bio TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela: courses
CREATE TABLE courses (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  title TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  description TEXT,
  level TEXT CHECK (level IN ('iniciante', 'tecnico', 'masterclass')),
  price NUMERIC(10, 2),
  duration_hours INT,
  thumbnail_url TEXT,
  status TEXT DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'archived')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela: modules
CREATE TABLE modules (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  course_id UUID REFERENCES courses(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  description TEXT,
  order_index INT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela: lessons
CREATE TABLE lessons (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  module_id UUID REFERENCES modules(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  description TEXT,
  video_url TEXT,
  video_duration INT, -- em segundos
  content TEXT, -- Markdown
  order_index INT NOT NULL,
  is_free BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela: resources (PDFs, Templates, etc.)
CREATE TABLE resources (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  file_url TEXT NOT NULL,
  file_type TEXT,
  file_size INT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela: enrollments (matrículas)
CREATE TABLE enrollments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  course_id UUID REFERENCES courses(id) ON DELETE CASCADE,
  enrolled_at TIMESTAMPTZ DEFAULT NOW(),
  expires_at TIMESTAMPTZ, -- NULL = vitalício
  payment_status TEXT CHECK (payment_status IN ('pending', 'paid', 'refunded')),
  payment_amount NUMERIC(10, 2),
  stripe_payment_id TEXT,
  UNIQUE(user_id, course_id)
);

-- Tabela: progress (progresso do aluno)
CREATE TABLE progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
  completed BOOLEAN DEFAULT FALSE,
  watched_duration INT DEFAULT 0, -- segundos assistidos
  last_watched_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id, lesson_id)
);

-- Tabela: quizzes
CREATE TABLE quizzes (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  questions JSONB NOT NULL, -- Array de perguntas
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela: quiz_submissions
CREATE TABLE quiz_submissions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  quiz_id UUID REFERENCES quizzes(id) ON DELETE CASCADE,
  answers JSONB NOT NULL,
  score NUMERIC(5, 2),
  submitted_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela: comments (comentários em aulas)
CREATE TABLE comments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  lesson_id UUID REFERENCES lessons(id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  parent_id UUID REFERENCES comments(id) ON DELETE CASCADE, -- para respostas
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabela: certificates
CREATE TABLE certificates (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
  course_id UUID REFERENCES courses(id) ON DELETE CASCADE,
  certificate_url TEXT,
  issued_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id, course_id)
);

-- Tabela: admin_users (permissões de admin)
CREATE TABLE admin_users (
  user_id UUID REFERENCES auth.users(id) PRIMARY KEY,
  role TEXT CHECK (role IN ('super_admin', 'instructor', 'support')),
  granted_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Índices para Performance:
```sql
CREATE INDEX idx_lessons_module ON lessons(module_id);
CREATE INDEX idx_progress_user ON progress(user_id);
CREATE INDEX idx_enrollments_user ON enrollments(user_id);
CREATE INDEX idx_comments_lesson ON comments(lesson_id);
```

---

## 🎯 FUNCIONALIDADES POR MÓDULO

### **1. Landing Page (Pública)**
- Hero com CTA (Call-to-Action)
- Apresentação dos 3 níveis de curso
- Depoimentos de alunos
- FAQ
- Seção "Para quem é"
- Garantia e políticas
- Footer com links

### **2. Autenticação**
- Cadastro (email + senha)
- Login (email + senha ou OAuth Google)
- Recuperação de senha
- Verificação de email
- Logout

### **3. Dashboard do Aluno**
- Visão geral de progresso
- Cursos matriculados
- Próxima aula
- Certificados disponíveis
- Acesso à comunidade

### **4. Página do Curso**
- Informações gerais
- Grade de módulos e aulas
- Avaliações e comentários
- Botão de matrícula (se não matriculado)
- Progresso (se matriculado)

### **5. Player de Aula**
- Vídeo com controles avançados
- Velocidade de reprodução (0.5x - 2x)
- Marcação automática de progresso
- Navegação entre aulas (próxima/anterior)
- Barra lateral com módulos
- Seção de recursos (PDFs, templates)
- Área de comentários
- Anotações pessoais

### **6. Comunidade**
- Feed de discussões
- Criar post/pergunta
- Responder e reagir
- Filtros por tópico
- Busca

### **7. Perfil do Usuário**
- Foto e bio
- Histórico de cursos
- Certificados
- Configurações
- Alterar senha

### **8. Checkout e Pagamentos**
- Carrinho (se múltiplos cursos)
- Formulário de pagamento
- Integração Stripe
- Confirmação e recibo
- Webhook para ativar acesso

### **9. Painel Admin**
#### Gestão de Cursos
- CRUD de cursos
- CRUD de módulos
- CRUD de aulas
- Upload de vídeos
- Upload de recursos

#### Gestão de Usuários
- Lista de alunos
- Matrículas manuais
- Reembolsos
- Bannir/Desativar

#### Relatórios
- Vendas por período
- Taxa de conclusão
- Engagement (tempo assistido)
- Comentários pendentes de moderação

#### Configurações
- Preços e cupons
- Emails transacionais
- Integrações

---

## 🚀 FLUXOS PRINCIPAIS

### Fluxo de Cadastro e Compra:
```
1. Usuário acessa landing page
2. Clica em "Começar Agora"
3. Escolhe nível (Iniciante/Técnico/Masterclass)
4. Redirecionado para cadastro (se não logado)
5. Após login, vai para checkout
6. Preenche dados de pagamento (Stripe)
7. Pagamento processado
8. Webhook ativa matrícula no banco
9. Email de boas-vindas enviado
10. Redirecionado para dashboard com acesso liberado
```

### Fluxo de Assistir Aula:
```
1. Aluno acessa dashboard
2. Clica em "Continuar Aprendendo"
3. Abre player de vídeo
4. Vídeo carrega e reproduz
5. Progresso salvo a cada 10 segundos
6. Ao completar 90% do vídeo, marca como concluído
7. Atualiza barra de progresso no dashboard
8. Libera próxima aula
```

### Fluxo de Emissão de Certificado:
```
1. Aluno completa 100% do curso
2. Sistema verifica todos os critérios:
   - Todas as aulas assistidas
   - Quizzes com nota mínima
   - Projeto final submetido (se aplicável)
3. Gera PDF do certificado com dados do aluno
4. Salva URL no banco
5. Notifica aluno por email
6. Disponibiliza para download no dashboard
```

---

## 🎨 WIREFRAMES E ESTRUTURA DE PÁGINAS

### 1. Landing Page (`/`)
```
├── Header (sticky)
│   ├── Logo
│   ├── Menu (Início, Níveis, Sobre, Contato)
│   └── CTA "Entrar" / "Cadastrar"
├── Hero
│   ├── Título: "Domine a Transformação Digital"
│   ├── Subtítulo: "Do iniciante ao masterclass"
│   └── CTA "Começar Agora"
├── Seção Níveis
│   ├── Card Iniciante (Verde)
│   ├── Card Técnico (Azul)
│   └── Card Masterclass (Roxo)
├── Seção Depoimentos
├── Seção "Para Quem É"
├── Seção FAQ (Accordion)
└── Footer
```

### 2. Dashboard (`/dashboard`)
```
├── Sidebar
│   ├── Avatar e Nome
│   ├── Meus Cursos
│   ├── Comunidade
│   ├── Certificados
│   └── Configurações
├── Main Content
│   ├── "Bem-vindo, [Nome]"
│   ├── Progresso Geral (%)
│   ├── Continuar Aprendendo (Card)
│   ├── Cursos Matriculados (Grid)
│   └── Atividade Recente
```

### 3. Player de Aula (`/curso/[courseId]/aula/[lessonId]`)
```
├── Header Simples (Voltar ao Dashboard)
├── Layout 2 Colunas
│   ├── Coluna Esquerda (70%)
│   │   ├── Player de Vídeo
│   │   ├── Título da Aula
│   │   ├── Descrição
│   │   ├── Tabs:
│   │   │   ├── Recursos (Downloads)
│   │   │   ├── Anotações
│   │   │   └── Comentários
│   └── Coluna Direita (30%)
│       ├── Progresso do Módulo
│       ├── Lista de Aulas (Accordion)
│       └── Próxima Aula (CTA)
```

### 4. Checkout (`/checkout/[courseId]`)
```
├── Header Simples
├── Layout 2 Colunas
│   ├── Coluna Esquerda (60%)
│   │   ├── Resumo do Pedido
│   │   ├── Formulário Stripe
│   │   └── Botão "Finalizar Compra"
│   └── Coluna Direita (40%)
│       ├── Thumbnail do Curso
│       ├── Título e Nível
│       ├── Preço
│       ├── Garantia de 7 dias
│       └── Itens Inclusos
```

### 5. Painel Admin (`/admin`)
```
├── Sidebar Admin
│   ├── Dashboard
│   ├── Cursos
│   ├── Alunos
│   ├── Pagamentos
│   ├── Relatórios
│   └── Configurações
├── Main Content (varia por seção)
```

---

## 📁 ESTRUTURA DE PASTAS (Next.js 14)

```
/ftd-platform
├── /app                          # App Router (Next.js 14)
│   ├── /(auth)
│   │   ├── /login
│   │   │   └── page.tsx
│   │   ├── /cadastro
│   │   │   └── page.tsx
│   │   └── /recuperar-senha
│   │       └── page.tsx
│   ├── /(public)
│   │   ├── /page.tsx             # Landing page
│   │   ├── /niveis
│   │   │   └── page.tsx
│   │   └── /sobre
│   │       └── page.tsx
│   ├── /(dashboard)
│   │   ├── /dashboard
│   │   │   └── page.tsx
│   │   ├── /curso
│   │   │   └── /[courseId]
│   │   │       ├── page.tsx      # Visão geral do curso
│   │   │       └── /aula
│   │   │           └── /[lessonId]
│   │   │               └── page.tsx  # Player
│   │   ├── /comunidade
│   │   │   └── page.tsx
│   │   ├── /certificados
│   │   │   └── page.tsx
│   │   └── /perfil
│   │       └── page.tsx
│   ├── /(checkout)
│   │   └── /checkout
│   │       └── /[courseId]
│   │           └── page.tsx
│   ├── /(admin)
│   │   └── /admin
│   │       ├── /dashboard
│   │       │   └── page.tsx
│   │       ├── /cursos
│   │       │   ├── page.tsx
│   │       │   ├── /novo
│   │       │   │   └── page.tsx
│   │       │   └── /[id]
│   │       │       └── /editar
│   │       │           └── page.tsx
│   │       ├── /alunos
│   │       │   └── page.tsx
│   │       └── /relatorios
│   │           └── page.tsx
│   ├── /api                      # API Routes
│   │   ├── /webhooks
│   │   │   └── /stripe
│   │   │       └── route.ts
│   │   └── /auth
│   │       └── /[...supabase]
│   │           └── route.ts
│   ├── layout.tsx                # Root layout
│   └── globals.css               # Estilos globais (Tailwind)
│
├── /components
│   ├── /ui                       # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── modal.tsx
│   │   ├── progress.tsx
│   │   └── ...
│   ├── /auth
│   │   ├── LoginForm.tsx
│   │   ├── SignupForm.tsx
│   │   └── PasswordReset.tsx
│   ├── /course
│   │   ├── CourseCard.tsx
│   │   ├── LevelBadge.tsx
│   │   ├── ModuleAccordion.tsx
│   │   └── VideoPlayer.tsx
│   ├── /dashboard
│   │   ├── Sidebar.tsx
│   │   ├── ProgressBar.tsx
│   │   └── ContinueLearning.tsx
│   ├── /landing
│   │   ├── Hero.tsx
│   │   ├── LevelCards.tsx
│   │   ├── Testimonials.tsx
│   │   └── FAQ.tsx
│   └── /admin
│       ├── CourseForm.tsx
│       ├── UserTable.tsx
│       └── StatsCard.tsx
│
├── /lib
│   ├── supabase.ts               # Supabase client
│   ├── stripe.ts                 # Stripe client
│   ├── utils.ts                  # Utilities
│   └── constants.ts              # Constantes globais
│
├── /hooks
│   ├── useAuth.ts                # Hook de autenticação
│   ├── useProgress.ts            # Hook de progresso
│   └── useCourse.ts              # Hook de curso
│
├── /types
│   ├── database.types.ts         # Tipos gerados do Supabase
│   ├── course.types.ts
│   └── user.types.ts
│
├── /styles
│   └── globals.css               # Tailwind + custom CSS
│
├── /public
│   ├── /images
│   ├── /icons
│   └── /videos
│
├── /supabase
│   ├── /migrations               # SQL migrations
│   └── /functions                # Edge Functions
│
├── .env.local                    # Variáveis de ambiente
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

---

## 🔐 SEGURANÇA

### Autenticação e Autorização:
- Supabase Auth (JWT)
- Row Level Security (RLS) no PostgreSQL
- Proteção de rotas no Next.js (middleware)
- CSRF protection
- Rate limiting em APIs sensíveis

### Políticas RLS (Exemplos):
```sql
-- Alunos só veem seus próprios dados de progresso
CREATE POLICY "Users can view own progress"
  ON progress FOR SELECT
  USING (auth.uid() = user_id);

-- Apenas admins podem criar cursos
CREATE POLICY "Only admins can create courses"
  ON courses FOR INSERT
  WITH CHECK (
    EXISTS (
      SELECT 1 FROM admin_users
      WHERE user_id = auth.uid()
    )
  );

-- Alunos só acessam aulas de cursos em que estão matriculados
CREATE POLICY "Enrolled users can view lessons"
  ON lessons FOR SELECT
  USING (
    EXISTS (
      SELECT 1 FROM enrollments e
      JOIN modules m ON lessons.module_id = m.id
      WHERE e.user_id = auth.uid()
        AND e.course_id = m.course_id
        AND e.payment_status = 'paid'
    )
    OR lessons.is_free = true
  );
```

---

## ⚡ PERFORMANCE E OTIMIZAÇÕES

### Frontend:
- **Next.js Image** para otimização automática de imagens
- **Lazy loading** de componentes pesados
- **Code splitting** automático (App Router)
- **Caching** com SWR ou React Query
- **Service Worker** para offline (opcional)

### Backend:
- **Connection pooling** no Supabase
- **Índices** nas queries mais frequentes
- **CDN** para assets estáticos (Cloudflare)
- **Edge Functions** para lógica próxima ao usuário

### Vídeos:
- **Streaming adaptativo** (HLS ou DASH)
- **CDN** para distribuição global
- **Compressão** em múltiplas resoluções (360p, 720p, 1080p)
- **Lazy loading** do player

---

## 📊 ANALYTICS E MÉTRICAS

### Eventos Customizados (Mixpanel/GA4):
- `user_signup` - Cadastro
- `course_enroll` - Matrícula
- `lesson_start` - Início de aula
- `lesson_complete` - Conclusão de aula
- `quiz_submit` - Envio de quiz
- `certificate_issued` - Emissão de certificado
- `comment_post` - Comentário publicado

### Métricas-Chave:
- Taxa de conversão (visita → compra)
- Taxa de conclusão por curso
- Tempo médio por aula
- NPS (Net Promoter Score)
- Churn rate
- LTV (Lifetime Value)

---

## 🔄 INTEGRAÇÕES

### Stripe (Pagamentos):
- Checkout Session
- Webhooks (`payment_intent.succeeded`)
- Customer Portal (gerenciar assinaturas)
- Refunds

### Sendgrid/Resend (Emails):
- Email de boas-vindas
- Confirmação de pagamento
- Lembrete de aulas
- Certificado disponível
- Recuperação de senha

### Vimeo/Bunny.net (Vídeos):
- Upload de vídeos
- Streaming otimizado
- Proteção de conteúdo (domain restriction)

### Zapier/Make (Automações):
- Novo aluno → CRM
- Certificado emitido → LinkedIn
- Comentário → Slack (moderação)

---

## 🧪 TESTES

### Tipos de Teste:
- **Unitários:** Vitest + Testing Library
- **Integração:** Playwright
- **E2E:** Playwright (fluxo completo de compra)
- **Performance:** Lighthouse CI

---

## 🚀 CI/CD

### Pipeline (GitHub Actions):
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - Checkout code
      - Install dependencies
      - Run tests
      - Build Next.js
      - Deploy to Vercel
      - Run migrations (Supabase)
```

---

## 📅 ROADMAP DE IMPLEMENTAÇÃO

### Fase 1: MVP (4 semanas)
- [ ] Setup do projeto (Next.js + Supabase)
- [ ] Autenticação funcionando
- [ ] Landing page responsiva
- [ ] 1 curso de exemplo com 3 aulas
- [ ] Player de vídeo básico
- [ ] Sistema de progresso
- [ ] Integração Stripe (checkout simples)
- [ ] Deploy em produção

### Fase 2: Funcionalidades Core (4 semanas)
- [ ] CRUD completo de cursos (admin)
- [ ] Comunidade (feed + comentários)
- [ ] Sistema de quizzes
- [ ] Geração de certificados
- [ ] Dashboard de analytics
- [ ] Emails transacionais
- [ ] Otimizações de performance

### Fase 3: Melhorias e Escala (4 semanas)
- [ ] Mobile app (React Native - opcional)
- [ ] Gamificação (badges, pontos)
- [ ] Recomendações personalizadas (IA)
- [ ] Comunidade avançada (grupos, eventos)
- [ ] Programa de afiliados
- [ ] Multi-idioma (i18n)

---

## 💰 ESTIMATIVA DE CUSTOS MENSAIS

### Infraestrutura (até 1.000 alunos):
- **Vercel:** $0 (hobby plan) ou $20 (pro)
- **Supabase:** $25 (pro plan)
- **Stripe:** 3.99% + R$0,39 por transação
- **Vimeo/Bunny.net:** $50-100/mês
- **Cloudflare:** $0 (free plan)
- **Emails (Sendgrid):** $15/mês

**Total:** ~$110/mês + taxas de transação

### Escalando (10.000 alunos):
- **Vercel:** $20
- **Supabase:** $99
- **Vídeos:** $300-500
- **Cloudflare:** $20
- **Emails:** $50

**Total:** ~$500/mês + taxas

---

## 🎯 PRÓXIMOS PASSOS

1. ✅ Arquitetura definida
2. ⏳ Criar repositório Git
3. ⏳ Setup inicial do projeto
4. ⏳ Configurar Supabase
5. ⏳ Implementar autenticação
6. ⏳ Desenvolver landing page
7. ⏳ Criar dashboard e player
8. ⏳ Integrar Stripe
9. ⏳ Testes e deploy MVP

---

**Arquiteto:** INEMA TDS
**Versão:** 1.0
**Data:** 12/11/2025
**Status:** Arquitetura Completa - Pronta para Desenvolvimento
