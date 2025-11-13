/* ========================================
   FTD - JavaScript Principal
   ======================================== */

document.addEventListener('DOMContentLoaded', function() {

  // Remove classe preload após carregar
  document.body.classList.remove('preload');

  /* ========================================
     DARK MODE SYSTEM
     ======================================== */

  const themeToggle = document.getElementById('theme-toggle');
  const themeToggleMobile = document.getElementById('theme-toggle-mobile');
  const html = document.documentElement;

  // Carregar preferência salva
  const currentTheme = localStorage.getItem('theme');

  if (currentTheme === 'dark') {
    html.classList.add('dark');
    updateThemeIcon(true);
  } else if (currentTheme === 'light') {
    html.classList.remove('dark');
    updateThemeIcon(false);
  } else {
    // Detectar preferência do sistema
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      html.classList.add('dark');
      localStorage.setItem('theme', 'dark');
      updateThemeIcon(true);
    } else {
      updateThemeIcon(false);
    }
  }

  // Toggle desktop
  if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
  }

  // Toggle mobile
  if (themeToggleMobile) {
    themeToggleMobile.addEventListener('click', toggleTheme);
  }

  function toggleTheme() {
    const isDark = html.classList.toggle('dark');
    const newTheme = isDark ? 'dark' : 'light';
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(isDark);
  }

  function updateThemeIcon(isDark) {
    // Desktop icons
    const darkIcon = document.getElementById('theme-toggle-dark-icon');
    const lightIcon = document.getElementById('theme-toggle-light-icon');

    if (darkIcon && lightIcon) {
      if (isDark) {
        lightIcon.classList.remove('hidden');
        darkIcon.classList.add('hidden');
      } else {
        darkIcon.classList.remove('hidden');
        lightIcon.classList.add('hidden');
      }
    }

    // Mobile icons
    const darkIconMobile = document.querySelector('.theme-icon-dark-mobile');
    const lightIconMobile = document.querySelector('.theme-icon-light-mobile');

    if (darkIconMobile && lightIconMobile) {
      if (isDark) {
        lightIconMobile.classList.remove('hidden');
        darkIconMobile.classList.add('hidden');
      } else {
        darkIconMobile.classList.remove('hidden');
        lightIconMobile.classList.add('hidden');
      }
    }
  }

  /* ========================================
     MOBILE MENU SYSTEM
     ======================================== */

  const mobileMenuButton = document.getElementById('mobile-menu-button');
  const mobileMenu = document.getElementById('mobile-menu');

  if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener('click', function() {
      mobileMenu.classList.toggle('hidden');
    });

    // Fechar menu ao clicar em um link
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
      link.addEventListener('click', function() {
        mobileMenu.classList.add('hidden');
      });
    });
  }

  /* ========================================
     TOPIC EXPANSION SYSTEM (FEP Pattern - Compact)
     ======================================== */

  document.addEventListener('click', function(e) {
    const topicButton = e.target.closest('.topic-button');

    if (topicButton) {
      const topicItem = topicButton.closest('.topic-item');
      const explanation = topicItem.querySelector('.topic-explanation');

      if (explanation) {
        const wasHidden = explanation.classList.contains('hidden');

        // Fechar todos os outros tópicos (accordion behavior)
        const chapterCard = topicItem.closest('.chapter-card');
        if (chapterCard) {
          chapterCard.querySelectorAll('.topic-explanation').forEach(exp => {
            exp.classList.add('hidden');
          });
        }

        // Toggle tópico atual
        if (wasHidden) {
          explanation.classList.remove('hidden');
        }
      }
    }
  });

  /* ========================================
     MODAL SYSTEM
     ======================================== */

  // Fechar modal ao clicar no X
  document.addEventListener('click', function(e) {
    if (e.target.classList.contains('close-modal')) {
      const modal = e.target.closest('.modal');
      if (modal) {
        closeModal(modal.id);
      }
    }

    // Fechar ao clicar fora do modal
    if (e.target.classList.contains('modal')) {
      closeModal(e.target.id);
    }
  });

  // Fechar modal com ESC
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      const activeModal = document.querySelector('.modal.active');
      if (activeModal) {
        closeModal(activeModal.id);
      }
    }
  });

  /* ========================================
     FORM HANDLING (Lead Form)
     ======================================== */

  const leadForm = document.getElementById('lead-form-element');
  if (leadForm) {
    leadForm.addEventListener('submit', function(e) {
      e.preventDefault();

      const name = leadForm.querySelector('input[name="name"]').value;
      const email = leadForm.querySelector('input[name="email"]').value;

      // Aqui você pode adicionar integração com backend/API
      console.log('Lead capturado:', { name, email });

      // Feedback visual
      alert('Obrigado! Você será notificado quando o FTD PRO for lançado.');
      leadForm.reset();
    });
  }

});

/* ========================================
   FUNÇÕES GLOBAIS (Modal)
   ======================================== */

function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
  }
}
