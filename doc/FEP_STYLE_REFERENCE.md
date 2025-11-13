# 🎨 FEP - Guia de Referência de Estilos e Layout

> **Fundamentos e Engenharia de Prompt**
> Sistema de Design Completo para Desenvolvimento de Interfaces

**Versão:** 1.0 | **Data:** 2025-11-04 | **Autor:** FEP Team

---

## 📋 Índice Rápido

- [Visão Geral](#visão-geral)
- [Identidade Visual](#identidade-visual)
- [Sistema de Cores](#sistema-de-cores)
- [Tipografia](#tipografia)
- [Espaçamento e Grid](#espaçamento-e-grid)
- [Componentes](#componentes)
- [Animações](#animações)
- [Responsividade](#responsividade)
- [Código de Exemplo](#código-de-exemplo)

---

## 🎯 Visão Geral

### Sobre o Projeto

**FEP** é um curso de **Engenharia de Prompt** com 3 níveis progressivos de aprendizado.

### Princípios de Design

1. ✅ **Clareza** - Interface limpa e fácil de navegar
2. ✅ **Progressão Visual** - Cada nível tem sua identidade
3. ✅ **Acessibilidade** - WCAG 2.1 AA compliant
4. ✅ **Performance** - Animações suaves
5. ✅ **Mobile-First** - Design responsivo

### Stack Tecnológico

```
Framework CSS:  Tailwind CSS 3.x (CDN)
JavaScript:     Vanilla JS
Fontes:         Google Fonts - Inter
Build:          HTML puro (sem build process)
```

---

## 🎨 Identidade Visual

### Logo e Marca

```
Nome:     FEP
Fonte:    Inter Bold (700)
Cor:      Blue 600 (#3B82F6)
Tagline:  "Engenharia de Prompt"
```

### Personalidade

- **Tom**: Profissional, educacional, acessível
- **Estilo**: Moderno, minimalista, tecnológico
- **Emoção**: Confiança, clareza, progresso

---

## 🌈 Sistema de Cores

### Cores por Nível (PRINCIPAL)

```css
/* 3 Níveis de Aprendizado */
🌟 Nível Iniciante:   #10B981  /* Verde Emerald 500 */
⚡ Nível Técnico:      #3B82F6  /* Azul Blue 500 */
👑 Nível Masterclass:  #8B5CF6  /* Roxo Purple 500 */
```

### Paleta Completa

```css
/* Primárias */
--primary:        #3B82F6;  /* Blue 600 - Botões, links */
--primary-dark:   #2563EB;  /* Blue 700 - Hover */
--accent:         #6366F1;  /* Indigo 500 - Destaques */
--accent-dark:    #4F46E5;  /* Indigo 600 - Hover */

/* Níveis */
--iniciante:      #10B981;  /* Verde */
--tecnico:        #3B82F6;  /* Azul */
--masterclass:    #8B5CF6;  /* Roxo */

/* Escala de Cinzas */
--gray-50:        #F9FAFB;  /* Backgrounds */
--gray-100:       #F3F4F6;  /* Cards alternativos */
--gray-200:       #E5E7EB;  /* Bordas leves */
--gray-300:       #D1D5DB;  /* Bordas padrão */
--gray-600:       #6B7280;  /* Texto secundário */
--gray-700:       #374151;  /* Texto principal */
--gray-900:       #1F2937;  /* Títulos */
```

### Gradientes

```css
/* Hero Section */
background: linear-gradient(to bottom right, #3B82F6, #2563EB, #8B5CF6);
/* Blue → Blue Dark → Purple */

/* Progress Bar */
background: linear-gradient(90deg, #3B82F6, #8B5CF6);
/* Azul → Roxo */

/* Cards de Nível */
.iniciante-card {
  background: linear-gradient(to bottom right, #ECFDF5, #FFFFFF);
  /* from-emerald-50 to-white */
}

.tecnico-card {
  background: linear-gradient(to bottom right, #EFF6FF, #FFFFFF);
  /* from-blue-50 to-white */
}

.masterclass-card {
  background: linear-gradient(to bottom right, #FAF5FF, #FFFFFF);
  /* from-purple-50 to-white */
}
```

### Uso por Contexto

| Elemento | Nível Iniciante | Nível Técnico | Nível Masterclass |
|----------|-----------------|---------------|-------------------|
| **Badge** | `bg-emerald-500` | `bg-blue-500` | `bg-purple-500` |
| **Borda** | `border-emerald-200` | `border-blue-200` | `border-purple-200` |
| **Hover** | `border-emerald-400` | `border-blue-400` | `border-purple-400` |
| **Botão** | `bg-emerald-500` | `bg-blue-500` | `bg-purple-500` |

---

## 📝 Tipografia

### Família de Fontes

```html
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

```css
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

### Hierarquia Tipográfica

#### Desktop
```css
H1 (Hero):      4rem (64px) | font-weight: 700
H2 (Section):   2.5rem (40px) | font-weight: 700
H3 (Card):      1.875rem (30px) | font-weight: 700
H4 (Subtitle):  1.5rem (24px) | font-weight: 600
Body Large:     1.25rem (20px) | font-weight: 400
Body:           1rem (16px) | font-weight: 400
Small:          0.875rem (14px) | font-weight: 400
```

#### Mobile (< 640px)
```css
H1:  2rem (32px)
H2:  1.75rem (28px)
H3:  1.5rem (24px)
```

### Classes Tailwind

```html
<!-- Hero Title -->
<h1 class="text-4xl sm:text-6xl font-bold">Título</h1>

<!-- Section Title -->
<h2 class="text-3xl sm:text-4xl font-bold">Seção</h2>

<!-- Card Title -->
<h3 class="text-2xl font-bold">Card</h3>

<!-- Body Text -->
<p class="text-base text-gray-700">Texto</p>

<!-- Secondary Text -->
<p class="text-sm text-gray-600">Secundário</p>
```

---

## 📏 Espaçamento e Grid

### Sistema de Espaçamento (Base: 1rem = 16px)

```
xs:   0.25rem   (4px)   - Espaços mínimos
sm:   0.5rem    (8px)   - Gaps pequenos
md:   1rem      (16px)  - Padrão
lg:   1.5rem    (24px)  - Entre elementos
xl:   2rem      (32px)  - Entre seções
2xl:  3rem      (48px)  - Padding de seções
3xl:  4rem      (64px)  - Espaços grandes
```

### Container Padrão

```html
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <!-- Conteúdo -->
</div>
```

**Comportamento:**
- Max width: 1280px
- Padding horizontal responsivo:
  - Mobile: 16px (`px-4`)
  - Tablet: 24px (`sm:px-6`)
  - Desktop: 32px (`lg:px-8`)

### Grids Responsivos

```html
<!-- 1 col → 3 cols -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">

<!-- 1 col → 2 cols -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-6">

<!-- 2 cols → 4 cols -->
<div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
```

### Breakpoints

```
sm:  640px   - Smartphone landscape
md:  768px   - Tablets
lg:  1024px  - Desktop
xl:  1280px  - Large desktop
```

---

## 🧩 Componentes

### 1. Navegação

```html
<nav class="sticky top-0 z-50 bg-white shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between items-center h-16">
      <!-- Logo -->
      <a href="/" class="text-2xl font-bold text-blue-600">
        FEP
      </a>

      <!-- Desktop Menu -->
      <div class="hidden md:flex space-x-8">
        <a href="#" class="text-gray-700 hover:text-blue-600">Início</a>
        <a href="#" class="text-gray-700 hover:text-blue-600">Níveis</a>
        <a href="#" class="text-gray-700 hover:text-blue-600">Sobre</a>
      </div>

      <!-- Mobile Menu Button -->
      <button class="md:hidden">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>
  </div>
</nav>
```

**Propriedades:**
- Posição: `sticky top-0`
- Z-index: `50`
- Altura: `h-16` (64px)
- Shadow: `shadow-sm`

---

### 2. Hero Section

```html
<section class="bg-gradient-to-br from-blue-600 via-blue-700 to-purple-700 py-20">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
    <h1 class="text-4xl sm:text-6xl font-bold mb-6">
      Domine a Engenharia de Prompt
    </h1>
    <p class="text-xl sm:text-2xl mb-8 text-white/90">
      Do iniciante ao masterclass em 3 níveis
    </p>
    <button class="bg-white text-blue-600 px-8 py-4 rounded-lg font-bold text-lg hover:bg-gray-100">
      Começar Agora
    </button>
  </div>
</section>
```

**Propriedades:**
- Gradiente: Blue 600 → Blue 700 → Purple 700
- Padding vertical: `py-20` (5rem)
- Texto branco com opacidade 90% para subtítulo

---

### 3. Level Cards (Cards de Nível)

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">

  <!-- Card Iniciante -->
  <div class="bg-gradient-to-br from-emerald-50 to-white border-2 border-emerald-200 hover:border-emerald-400 rounded-2xl p-8 transition-all hover:-translate-y-1 hover:shadow-xl">
    <div class="text-4xl mb-4">🌟</div>
    <h3 class="text-2xl font-bold text-gray-900 mb-2">Iniciante</h3>

    <!-- Badge -->
    <span class="inline-block px-3 py-1 bg-emerald-500 text-white text-sm font-semibold rounded-full mb-4">
      30 horas
    </span>

    <p class="text-gray-600 mb-6">
      Fundamentos de prompt engineering
    </p>

    <!-- Lista de tópicos -->
    <ul class="space-y-2 mb-6">
      <li class="flex items-start">
        <span class="text-emerald-500 mr-2">✓</span>
        <span class="text-gray-700">Conceitos básicos</span>
      </li>
      <li class="flex items-start">
        <span class="text-emerald-500 mr-2">✓</span>
        <span class="text-gray-700">Técnicas essenciais</span>
      </li>
    </ul>

    <!-- Botão -->
    <button class="w-full bg-emerald-500 text-white py-3 rounded-lg font-semibold hover:bg-emerald-600">
      Começar
    </button>
  </div>

  <!-- Repita para Técnico (blue) e Masterclass (purple) -->

</div>
```

**Efeitos:**
- Hover: `translateY(-4px)` + `shadow-xl`
- Transition: `0.3s ease`
- Border radius: `rounded-2xl`

---

### 4. Botões

```html
<!-- Primário -->
<button class="bg-blue-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-600 active:scale-98">
  Clique Aqui
</button>

<!-- Secundário -->
<button class="bg-transparent border-2 border-blue-500 text-blue-500 px-6 py-3 rounded-lg font-semibold hover:bg-blue-50">
  Ver Mais
</button>

<!-- Com Ícone -->
<button class="bg-blue-500 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-600 flex items-center gap-2">
  <span>📖</span>
  <span>Ver em Modal</span>
</button>
```

---

### 5. Badges

```html
<!-- Verde (Iniciante) -->
<span class="inline-block px-3 py-1 bg-emerald-500 text-white text-sm font-semibold rounded-full">
  30 horas
</span>

<!-- Azul (Técnico) -->
<span class="inline-block px-3 py-1 bg-blue-500 text-white text-sm font-semibold rounded-full">
  40 horas
</span>

<!-- Roxo (Masterclass) -->
<span class="inline-block px-3 py-1 bg-purple-500 text-white text-sm font-semibold rounded-full">
  50 horas
</span>
```

---

### 6. Tópicos Expansíveis (Accordion)

```html
<div class="module-card bg-white rounded-xl shadow-md p-6">
  <h2 class="text-2xl font-bold mb-4">Módulo 1</h2>

  <ul class="topics-list space-y-2">
    <li class="topic-item">
      <button class="topic-button w-full text-left px-4 py-3 bg-gray-50 hover:bg-gray-100 rounded-lg transition-colors font-medium">
        📌 Tópico 1: Conceito
      </button>

      <div class="topic-explanation hidden ml-6 mt-2 p-4 bg-blue-50 rounded-lg border-l-4 border-blue-500">
        <p class="text-sm mb-2">
          <strong class="text-blue-600">O que é:</strong> Explicação clara
        </p>
        <p class="text-sm mb-2">
          <strong class="text-blue-600">Por que aprender:</strong> Benefícios
        </p>
        <p class="text-sm">
          <strong class="text-blue-600">Conceitos chave:</strong> Termos importantes
        </p>
      </div>
    </li>
  </ul>
</div>
```

**JavaScript:**
```javascript
document.addEventListener('click', function(e) {
  const topicButton = e.target.closest('.topic-button');

  if (topicButton) {
    const topicItem = topicButton.closest('.topic-item');
    const explanation = topicItem.querySelector('.topic-explanation');

    if (explanation) {
      // Fechar outros tópicos (accordion behavior)
      const moduleCard = topicItem.closest('.module-card');
      moduleCard.querySelectorAll('.topic-explanation').forEach(exp => {
        if (exp !== explanation) {
          exp.classList.add('hidden');
        }
      });

      // Toggle atual
      explanation.classList.toggle('hidden');
    }
  }
});
```

**Espaçamento:**
- Entre botões: `space-y-2` (8px)
- Padding dos botões: `py-3` (12px)
- Entre parágrafos: `mb-2` (8px)

---

### 7. Modal

```html
<div id="modal-exemplo" class="modal hidden fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center">
  <div class="modal-content bg-white rounded-xl max-w-4xl max-h-[90vh] overflow-hidden shadow-2xl">

    <!-- Header -->
    <div class="modal-header flex justify-between items-center p-6 border-b border-gray-200">
      <h2 class="text-2xl font-bold text-gray-900">Título do Modal</h2>
      <button class="close-modal text-gray-400 hover:text-red-500 text-3xl font-bold">
        &times;
      </button>
    </div>

    <!-- Body -->
    <div class="modal-body p-6 overflow-y-auto">
      <p>Conteúdo aqui...</p>
    </div>

  </div>
</div>
```

**JavaScript:**
```javascript
// Abrir modal
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  modal.classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}

// Fechar modal
function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  modal.classList.add('hidden');
  document.body.style.overflow = 'auto';
}

// Fechar ao clicar fora
document.addEventListener('click', function(e) {
  if (e.target.classList.contains('modal')) {
    e.target.classList.add('hidden');
    document.body.style.overflow = 'auto';
  }

  if (e.target.classList.contains('close-modal')) {
    const modal = e.target.closest('.modal');
    modal.classList.add('hidden');
    document.body.style.overflow = 'auto';
  }
});

// Fechar com ESC
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    const activeModal = document.querySelector('.modal:not(.hidden)');
    if (activeModal) {
      activeModal.classList.add('hidden');
      document.body.style.overflow = 'auto';
    }
  }
});
```

---

### 8. Progress Bar

```html
<div class="progress-bar w-full h-2 bg-gray-200 rounded-full overflow-hidden">
  <div class="progress-fill h-full bg-gradient-to-r from-blue-500 to-purple-500 transition-all duration-500" style="width: 60%">
  </div>
</div>
```

---

### 9. Footer

```html
<footer class="bg-gray-900 text-white py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

      <!-- Coluna 1 -->
      <div>
        <h3 class="text-xl font-bold mb-4">FEP</h3>
        <p class="text-gray-400 text-sm">
          Fundamentos e Engenharia de Prompt
        </p>
      </div>

      <!-- Coluna 2 -->
      <div>
        <h4 class="font-semibold mb-4">Links</h4>
        <ul class="space-y-2 text-sm">
          <li><a href="#" class="text-gray-400 hover:text-white">Início</a></li>
          <li><a href="#" class="text-gray-400 hover:text-white">Níveis</a></li>
        </ul>
      </div>

      <!-- Coluna 3 -->
      <div>
        <h4 class="font-semibold mb-4">Contato</h4>
        <p class="text-gray-400 text-sm">email@exemplo.com</p>
      </div>

    </div>

    <div class="border-t border-gray-800 mt-8 pt-8 text-center text-sm text-gray-400">
      <p>&copy; 2025 FEP. Todos os direitos reservados.</p>
    </div>
  </div>
</footer>
```

---

## ✨ Animações

### Princípios

1. Usar apenas `transform` e `opacity` (performance)
2. Duração: 0.2s-0.8s
3. Easing: `ease-out` ou `cubic-bezier(0.4, 0, 0.2, 1)`
4. Respeitar `prefers-reduced-motion`

### Animações Definidas

```css
/* Fade In */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.8s ease-out;
}

/* Card Hover */
.card {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
}

/* Button Active */
button:active {
  transform: scale(0.98);
}

/* Spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.spinner {
  animation: spin 0.6s linear infinite;
}
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 📱 Responsividade

### Estratégia: Mobile-First

```
Base (Mobile):     < 640px
Tablet (sm):       >= 640px
Desktop (md):      >= 768px
Large Desktop (lg): >= 1024px
XL Desktop (xl):   >= 1280px
```

### Padrões Comuns

```html
<!-- Texto responsivo -->
<h1 class="text-4xl lg:text-6xl">Título</h1>
<p class="text-base lg:text-lg">Texto</p>

<!-- Grid responsivo -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">

<!-- Padding responsivo -->
<section class="py-12 lg:py-20">

<!-- Visibilidade -->
<div class="hidden md:block">Só desktop</div>
<div class="md:hidden">Só mobile</div>

<!-- Flex direction -->
<div class="flex flex-col sm:flex-row gap-4">
```

---

## 🎬 Código de Exemplo Completo

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FEP - Fundamentos e Engenharia de Prompt</title>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    body {
      font-family: 'Inter', sans-serif;
    }
  </style>
</head>
<body class="bg-gray-50">

  <!-- Navegação -->
  <nav class="sticky top-0 z-50 bg-white shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <a href="/" class="text-2xl font-bold text-blue-600">FEP</a>
        <div class="hidden md:flex space-x-8">
          <a href="#" class="text-gray-700 hover:text-blue-600">Início</a>
          <a href="#" class="text-gray-700 hover:text-blue-600">Níveis</a>
        </div>
      </div>
    </div>
  </nav>

  <!-- Hero -->
  <section class="bg-gradient-to-br from-blue-600 via-blue-700 to-purple-700 py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-white">
      <h1 class="text-4xl sm:text-6xl font-bold mb-6">
        Domine a Engenharia de Prompt
      </h1>
      <p class="text-xl sm:text-2xl mb-8 text-white/90">
        Do iniciante ao masterclass
      </p>
      <button class="bg-white text-blue-600 px-8 py-4 rounded-lg font-bold hover:bg-gray-100">
        Começar Agora
      </button>
    </div>
  </section>

  <!-- Cards de Nível -->
  <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

      <!-- Card Iniciante -->
      <div class="bg-gradient-to-br from-emerald-50 to-white border-2 border-emerald-200 hover:border-emerald-400 rounded-2xl p-8 transition-all hover:-translate-y-1 hover:shadow-xl">
        <div class="text-4xl mb-4">🌟</div>
        <h3 class="text-2xl font-bold text-gray-900 mb-2">Iniciante</h3>
        <span class="inline-block px-3 py-1 bg-emerald-500 text-white text-sm font-semibold rounded-full mb-4">
          30 horas
        </span>
        <p class="text-gray-600 mb-6">Fundamentos essenciais</p>
        <button class="w-full bg-emerald-500 text-white py-3 rounded-lg font-semibold hover:bg-emerald-600">
          Começar
        </button>
      </div>

      <!-- Repita para Técnico e Masterclass -->

    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-gray-900 text-white py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <p class="text-gray-400">&copy; 2025 FEP</p>
    </div>
  </footer>

</body>
</html>
```

---

## 📚 Quick Reference

### Classes Mais Usadas

```css
/* Containers */
.container       → max-w-7xl mx-auto px-4 sm:px-6 lg:px-8

/* Cards */
.card            → bg-white rounded-xl shadow-md p-6

/* Buttons */
.btn-primary     → bg-blue-500 text-white px-6 py-3 rounded-lg hover:bg-blue-600
.btn-secondary   → border-2 border-blue-500 text-blue-500 px-6 py-3 rounded-lg hover:bg-blue-50

/* Text */
.title           → text-4xl lg:text-6xl font-bold
.subtitle        → text-xl lg:text-2xl text-gray-600

/* Spacing */
.section-padding → py-12 lg:py-20
.card-gap        → gap-6 lg:gap-8
```

---

## ✅ Checklist de Implementação

- [ ] Incluir Tailwind CSS CDN
- [ ] Incluir Google Fonts (Inter)
- [ ] Usar cores corretas por nível (verde/azul/roxo)
- [ ] Aplicar espaçamento consistente
- [ ] Testar responsividade (mobile, tablet, desktop)
- [ ] Adicionar animações suaves
- [ ] Implementar acessibilidade (ARIA, focus)
- [ ] Testar com prefers-reduced-motion
- [ ] Validar contraste de cores (WCAG AA)

---

**Última atualização:** 2025-11-04
**Versão:** 1.0
**Autor:** FEP Team

---

