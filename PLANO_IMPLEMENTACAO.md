# 🚀 PLANO DE IMPLEMENTAÇÃO - FTD
## Do Planejamento ao Lançamento

> **Projeto:** Formação da Transformação Digital
> **Data:** 12/11/2025
> **Status:** Planejamento Completo
> **Próximo passo:** Iniciar desenvolvimento

---

## 📊 RESUMO EXECUTIVO

### O que Temos:
✅ **Estrutura completa do curso** (9 módulos + extras)
✅ **Conteúdo base** (PDF com 20 páginas, materiais de referência)
✅ **Design system** definido (cores, tipografia, componentes)
✅ **Arquitetura técnica** completa (stack, banco, fluxos)
✅ **Pesquisa de mercado** (tendências 2025)

### O que Precisamos Construir:
1. 🎨 **Plataforma Web** (frontend + backend)
2. 📹 **Conteúdo em Vídeo** (videoaulas gravadas)
3. 📄 **Materiais de Apoio** (PDFs, templates, exercícios)
4. 💳 **Sistema de Pagamentos** (integração Stripe)
5. 📢 **Estratégia de Lançamento** (marketing e vendas)

---

## 🎯 FASES DO PROJETO

## FASE 1: SETUP E MVP (Semanas 1-4)

### Objetivos:
- Setup completo do ambiente de desenvolvimento
- Autenticação funcionando
- Landing page publicada
- 1 módulo de exemplo disponível
- Sistema de pagamento integrado
- Deploy em produção (versão beta)

### Tarefas Detalhadas:

#### Semana 1: Setup e Infraestrutura
**Dias 1-2: Configuração Inicial**
- [ ] Criar repositório no GitHub
- [ ] Inicializar projeto Next.js 14
- [ ] Configurar Tailwind CSS + shadcn/ui
- [ ] Criar conta Supabase e configurar projeto
- [ ] Configurar variáveis de ambiente (.env.local)
- [ ] Setup do TypeScript e ESLint

**Dias 3-4: Banco de Dados**
- [ ] Criar schema no Supabase (SQL migrations)
- [ ] Configurar Row Level Security (RLS)
- [ ] Gerar tipos TypeScript do banco
- [ ] Testar conexão com Supabase Client

**Dia 5: Autenticação**
- [ ] Implementar Supabase Auth
- [ ] Criar páginas de login, cadastro, recuperação de senha
- [ ] Middleware para proteção de rotas
- [ ] Testes de fluxo de autenticação

**Weekend: Documentação**
- [ ] Documentar decisões técnicas
- [ ] Criar README com instruções de setup
- [ ] Atualizar gitignore e configurações

---

#### Semana 2: Landing Page e Design System
**Dias 1-2: Componentes Base**
- [ ] Implementar componentes shadcn/ui (Button, Card, Modal)
- [ ] Criar componentes customizados (LevelBadge, ProgressBar)
- [ ] Definir paleta de cores no Tailwind config
- [ ] Criar arquivo de constantes (níveis, cores, etc)

**Dias 3-5: Landing Page**
- [ ] Componente Hero com gradiente
- [ ] Seção de Níveis (cards verde, azul, roxo)
- [ ] Seção de Depoimentos (opcional: pegar do Notion ou criar fake)
- [ ] FAQ com accordions
- [ ] Footer com links
- [ ] Responsividade mobile

**Weekend: Refinamento**
- [ ] Ajustes de design (espaçamento, cores)
- [ ] Testes de acessibilidade (contraste, keyboard navigation)
- [ ] Performance (otimizar imagens, lazy loading)

---

#### Semana 3: Dashboard e Player de Aula
**Dias 1-2: Dashboard**
- [ ] Sidebar com navegação
- [ ] Página inicial do dashboard (progresso geral)
- [ ] Lista de cursos matriculados
- [ ] "Continuar Aprendendo" (última aula assistida)

**Dias 3-4: Player de Aula**
- [ ] Layout 2 colunas (vídeo + sidebar)
- [ ] Integrar player de vídeo (Plyr.io ou Video.js)
- [ ] Lista de aulas (accordion com módulos)
- [ ] Botão "Marcar como concluído"
- [ ] Sistema de progresso (salvar no banco)

**Dia 5: Recursos e Comentários**
- [ ] Seção de recursos (download de PDFs)
- [ ] Área de comentários (CRUD básico)
- [ ] Anotações pessoais (opcional para MVP)

**Weekend: Integração**
- [ ] Conectar dashboard → curso → aula
- [ ] Testes de navegação e fluxo

---

#### Semana 4: Pagamentos e Lançamento Beta
**Dias 1-2: Stripe**
- [ ] Criar conta Stripe (modo teste)
- [ ] Implementar Checkout Session
- [ ] Página de checkout com formulário
- [ ] Webhook para confirmar pagamento
- [ ] Ativar matrícula automaticamente

**Dia 3: Admin Básico**
- [ ] Criar flag de admin na tabela users
- [ ] Página de admin com proteção
- [ ] CRUD de curso básico (criar e editar)
- [ ] Upload de vídeo para Supabase Storage

**Dia 4: Conteúdo de Exemplo**
- [ ] Criar 1 curso completo (ex: Módulo 1.1 - Impacto da IA)
- [ ] Adicionar 3 aulas em vídeo (pode ser placeholder ou primeira gravação)
- [ ] Upload de 3 PDFs como recursos
- [ ] Configurar preço de teste (R$ 97)

**Dia 5: Deploy**
- [ ] Deploy no Vercel (conectar repo GitHub)
- [ ] Configurar domínio customizado (opcional)
- [ ] Testar em produção
- [ ] Corrigir bugs críticos

**Weekend: Testes Beta**
- [ ] Convidar 5-10 amigos/conhecidos para testar
- [ ] Coletar feedback
- [ ] Priorizar melhorias

---

## FASE 2: FUNCIONALIDADES CORE (Semanas 5-8)

### Objetivos:
- CRUD completo de cursos (admin)
- Todos os módulos do curso FTD disponíveis
- Sistema de quizzes
- Geração de certificados
- Comunidade ativa
- Emails transacionais

### Tarefas Detalhadas:

#### Semana 5: Admin Completo
- [ ] Dashboard admin com métricas (vendas, alunos, engajamento)
- [ ] CRUD de módulos e aulas
- [ ] Upload otimizado de vídeos (integrar Bunny.net ou Vimeo)
- [ ] Gestão de alunos (lista, busca, matrículas manuais)
- [ ] Sistema de cupons de desconto

#### Semana 6: Quizzes e Gamificação
- [ ] Criar tabela de quizzes e submissions
- [ ] Interface para criar quiz (admin)
- [ ] Player de quiz (aluno)
- [ ] Cálculo de score e feedback
- [ ] Liberação de certificado após atingir nota mínima

#### Semana 7: Certificados e Emails
- [ ] Geração de PDF de certificado (biblioteca: PDFKit ou Puppeteer)
- [ ] Design do certificado com branding FTD
- [ ] Envio automático por email quando disponível
- [ ] Download no dashboard
- [ ] Integração com Sendgrid/Resend para emails transacionais

#### Semana 8: Comunidade
- [ ] Feed de discussões
- [ ] Criar post/pergunta
- [ ] Comentários e respostas
- [ ] Reações (like, love)
- [ ] Moderação básica (admin)

---

## FASE 3: CONTEÚDO E PRODUÇÃO (Semanas 9-16)

### Objetivos:
- Gravar todas as videoaulas
- Criar todos os materiais de apoio
- Revisar e testar todo o conteúdo
- Preparar estratégia de lançamento

### Tarefas Detalhadas:

#### Semanas 9-12: Gravação de Vídeos
**Preparação:**
- [ ] Roteiro de todas as aulas (baseado na estrutura)
- [ ] Setup de gravação (câmera, microfone, iluminação, software)
- [ ] Template de slides (Canva, PowerPoint)

**Gravação (4 semanas):**
- **Semana 9:** Módulos 1.1, 1.2, 1.3
- **Semana 10:** Módulos 1.4, 1.5 (Imagens e Vídeos)
- **Semana 11:** Módulo 1.6 (Marketing e Vendas)
- **Semana 12:** Módulos 1.7, 1.8, 1.9

**Pós-produção:**
- [ ] Edição de vídeos (cortes, intro/outro, legendas)
- [ ] Upload para plataforma de vídeo
- [ ] Geração de thumbnails

#### Semanas 13-14: Materiais de Apoio
- [ ] Criar 50 PDFs (guias, checklists, templates)
- [ ] Biblioteca de 500+ prompts prontos
- [ ] Planilhas e ferramentas (Excel, Google Sheets)
- [ ] Recursos extras (links, ferramentas, integrações)

#### Semanas 15-16: Testes e Ajustes
- [ ] Convidar beta testers (100 pessoas)
- [ ] Coletar feedback estruturado (formulário)
- [ ] Corrigir erros de conteúdo
- [ ] Ajustar ritmo e profundidade das aulas
- [ ] Refinar UX da plataforma

---

## FASE 4: MARKETING E LANÇAMENTO (Semanas 17-20)

### Objetivos:
- Criar estratégia de marketing completa
- Construir audiência pré-lançamento
- Lançar oficialmente o curso
- Primeiros 100 alunos pagantes

### Tarefas Detalhadas:

#### Semana 17: Preparação de Marketing
- [ ] Definir posicionamento e mensagem
- [ ] Criar materiais de divulgação (posts, vídeos, stories)
- [ ] Landing page de pré-lançamento com lista de espera
- [ ] Oferta de early bird (desconto para primeiros alunos)
- [ ] Configurar pixel do Facebook e Google Ads

#### Semana 18: Construção de Audiência
- [ ] Conteúdo orgânico diário (Instagram, TikTok, LinkedIn)
- [ ] Artigos no Medium/LinkedIn sobre transformação digital
- [ ] Parcerias com influenciadores de tecnologia
- [ ] Lives educacionais (gratuitas) com CTA para lista de espera
- [ ] Email marketing para lista de espera

#### Semana 19: Pré-Lançamento
- [ ] Webinar ao vivo: "Transformação Digital em 2025"
- [ ] Oferta exclusiva para lista de espera (48h)
- [ ] Depoimentos de beta testers (vídeos curtos)
- [ ] Countdown nas redes sociais
- [ ] Preparar suporte (FAQ, chatbot, equipe)

#### Semana 20: LANÇAMENTO OFICIAL
- [ ] Abertura das matrículas
- [ ] Campanha de ads (Facebook, Instagram, Google)
- [ ] Lives diárias durante a semana de lançamento
- [ ] Email marketing (sequência de 7 emails)
- [ ] Programa de afiliados (15% de comissão)
- [ ] Monitoramento de métricas em tempo real

**Meta:** 100 alunos pagantes na primeira semana

---

## 📅 CRONOGRAMA VISUAL

```
Mês 1 (Semanas 1-4):    MVP + Beta
Mês 2 (Semanas 5-8):    Funcionalidades Core
Mês 3-4 (Semanas 9-16): Produção de Conteúdo
Mês 5 (Semanas 17-20):  Marketing + Lançamento
```

**Total:** 5 meses (20 semanas) até lançamento oficial

---

## 👥 EQUIPE NECESSÁRIA

### Fase 1-2 (MVP e Core):
- **1 Desenvolvedor Full-Stack** (Next.js + Supabase)
- **1 Designer UI/UX** (part-time para ajustes)

### Fase 3 (Produção):
- **1 Instrutor** (gravação das aulas)
- **1 Editor de Vídeo** (pós-produção)
- **1 Designer Gráfico** (materiais de apoio, thumbnails)

### Fase 4 (Marketing):
- **1 Gestor de Tráfego** (ads, campanhas)
- **1 Copywriter** (emails, landing pages, posts)
- **1 Community Manager** (suporte, engajamento)

### Alternativa Solo (1 pessoa fazendo tudo):
- **Tempo total:** Dobrar cronograma (10 meses)
- **Recomendação:** Terceirizar edição de vídeo e design gráfico

---

## 💰 INVESTIMENTO ESTIMADO

### Desenvolvimento (Fases 1-2):
- Desenvolvedor Full-Stack: R$ 20.000 (freelance) ou R$ 30.000 (contrato)
- Designer UI/UX: R$ 5.000 (ajustes pontuais)
- **Subtotal:** R$ 25.000 - R$ 35.000

### Produção de Conteúdo (Fase 3):
- Equipamento de gravação: R$ 5.000 (câmera, mic, luz - uma vez)
- Editor de vídeo: R$ 8.000 (100+ vídeos)
- Designer gráfico: R$ 3.000 (materiais)
- **Subtotal:** R$ 16.000

### Marketing (Fase 4):
- Ads (Facebook + Google): R$ 10.000 (teste inicial)
- Copywriter: R$ 3.000
- Influenciadores/Parcerias: R$ 5.000
- **Subtotal:** R$ 18.000

### Infraestrutura (5 meses):
- Hospedagem + SaaS: R$ 500/mês × 5 = R$ 2.500

### TOTAL ESTIMADO:
**R$ 61.500 - R$ 71.500**

---

## 📊 PROJEÇÃO DE RECEITA

### Cenário Conservador (Ano 1):
- **Mês 1 (Lançamento):** 100 alunos × R$ 997 = R$ 99.700
- **Mês 2-3:** 50 alunos/mês × R$ 997 = R$ 99.700
- **Mês 4-12:** 30 alunos/mês × R$ 997 × 9 meses = R$ 269.190

**Total Ano 1:** R$ 468.590
**Lucro (após custos):** R$ 400.000+

### Cenário Otimista (Ano 1):
- **Lançamento:** 300 alunos × R$ 997 = R$ 299.100
- **Crescimento médio:** 100 alunos/mês

**Total Ano 1:** R$ 1.200.000+

---

## 🎯 MÉTRICAS DE SUCESSO

### Indicadores-Chave (KPIs):
- **Taxa de conversão:** Visitantes → Compradores (meta: 3%)
- **Taxa de conclusão:** Alunos que terminam o curso (meta: 60%)
- **NPS:** Satisfação dos alunos (meta: > 80)
- **LTV:** Lifetime Value por aluno (meta: R$ 3.000)
- **CAC:** Custo de Aquisição de Cliente (meta: < R$ 300)

---

## 🚨 RISCOS E MITIGAÇÕES

### Riscos Identificados:
1. **Atraso na produção de vídeos**
   - Mitigação: Buffer de 2 semanas, contratar editor extra

2. **Baixa conversão no lançamento**
   - Mitigação: Lista de espera de 1.000+ pessoas, oferta irresistível

3. **Problemas técnicos na plataforma**
   - Mitigação: Testes extensivos, beta testers, suporte 24/7 no lançamento

4. **Competição forte**
   - Mitigação: Diferenciação (prático, atualizado, comunidade), garantia de 7 dias

5. **Evasão de alunos**
   - Mitigação: Gamificação, comunidade engajada, mentorias ao vivo

---

## 📋 CHECKLIST FINAL PRÉ-LANÇAMENTO

### Técnico:
- [ ] Todos os módulos disponíveis
- [ ] Vídeos carregam < 2s
- [ ] Pagamentos funcionando (Stripe testado)
- [ ] Certificados gerados corretamente
- [ ] Emails sendo enviados
- [ ] Backup configurado
- [ ] Testes de carga (1.000 usuários simultâneos)

### Conteúdo:
- [ ] 100+ videoaulas gravadas e editadas
- [ ] 50+ PDFs criados
- [ ] 500+ prompts na biblioteca
- [ ] Todos os exercícios revisados
- [ ] Quiz de cada módulo funcionando

### Marketing:
- [ ] Landing page otimizada (conversão > 3%)
- [ ] 1.000+ pessoas na lista de espera
- [ ] 10 depoimentos em vídeo
- [ ] Campanha de ads testada
- [ ] Programa de afiliados configurado

### Suporte:
- [ ] FAQ completo (50+ perguntas)
- [ ] Chatbot configurado
- [ ] Equipe treinada
- [ ] Scripts de atendimento prontos

---

## 🚀 PRÓXIMOS PASSOS IMEDIATOS

### Esta Semana:
1. ✅ **Definir equipe** (contratar dev ou fazer solo?)
2. ✅ **Criar repositório GitHub** privado
3. ✅ **Setup inicial do projeto** (Next.js + Supabase)
4. ✅ **Configurar Tailwind e shadcn/ui**
5. ✅ **Implementar autenticação** básica

### Próxima Semana:
1. ✅ **Finalizar landing page** (design system do FEP)
2. ✅ **Criar 1 módulo completo** (aula de exemplo)
3. ✅ **Integrar Stripe** (checkout teste)
4. ✅ **Deploy MVP** no Vercel
5. ✅ **Testar com 5 pessoas**

---

## 📞 CONTATO E SUPORTE

### Para Dúvidas Técnicas:
- GitHub Issues (quando repo estiver criado)
- Email: dev@ftd.com (configurar)

### Para Parcerias:
- Email: parcerias@ftd.com

---

**Criado por:** INEMA TDS
**Data:** 12/11/2025
**Próxima Revisão:** Após Fase 1 (Semana 4)
**Status:** Pronto para Execução 🚀
