// FTD - Formação da Transformação Digital
// Main JavaScript

// ===== MOBILE MENU =====
function initMobileMenu() {
    const menuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    if (menuButton && mobileMenu) {
        menuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('active');
        });
    }
}

// ===== SMOOTH SCROLL =====
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// ===== PROGRESS TRACKING =====
class ProgressTracker {
    constructor() {
        this.storageKey = 'ftd-progress';
        this.progress = this.loadProgress();
    }

    loadProgress() {
        const stored = localStorage.getItem(this.storageKey);
        return stored ? JSON.parse(stored) : {};
    }

    saveProgress() {
        localStorage.setItem(this.storageKey, JSON.stringify(this.progress));
    }

    markModuleComplete(moduleId) {
        this.progress[moduleId] = {
            completed: true,
            timestamp: new Date().toISOString()
        };
        this.saveProgress();
        this.updateUI();
    }

    isModuleComplete(moduleId) {
        return this.progress[moduleId]?.completed || false;
    }

    getCompletionPercentage() {
        const totalModules = 9; // Total de módulos principais
        const completedModules = Object.values(this.progress).filter(p => p.completed).length;
        return Math.round((completedModules / totalModules) * 100);
    }

    updateUI() {
        // Update progress bar if exists
        const progressBar = document.querySelector('.progress-bar-fill');
        if (progressBar) {
            progressBar.style.width = `${this.getCompletionPercentage()}%`;
        }

        // Update completion text
        const completionText = document.querySelector('.completion-text');
        if (completionText) {
            completionText.textContent = `${this.getCompletionPercentage()}% concluído`;
        }

        // Mark completed modules in sidebar
        document.querySelectorAll('[data-module-id]').forEach(el => {
            const moduleId = el.dataset.moduleId;
            if (this.isModuleComplete(moduleId)) {
                el.classList.add('completed');
                // Add checkmark icon
                if (!el.querySelector('.checkmark')) {
                    const checkmark = document.createElement('span');
                    checkmark.className = 'checkmark ml-auto text-green-500';
                    checkmark.innerHTML = '✓';
                    el.appendChild(checkmark);
                }
            }
        });
    }

    reset() {
        if (confirm('Tem certeza que deseja resetar todo o progresso?')) {
            localStorage.removeItem(this.storageKey);
            this.progress = {};
            this.updateUI();
            location.reload();
        }
    }
}

// ===== ACCORDION =====
function initAccordions() {
    document.querySelectorAll('.accordion-header').forEach(header => {
        header.addEventListener('click', () => {
            const content = header.nextElementSibling;
            const icon = header.querySelector('.accordion-icon');

            // Toggle active class
            content.classList.toggle('active');

            // Rotate icon
            if (icon) {
                icon.style.transform = content.classList.contains('active')
                    ? 'rotate(180deg)'
                    : 'rotate(0deg)';
            }
        });
    });
}

// ===== TASK CHECKBOXES =====
function initTaskCheckboxes() {
    const moduleId = document.body.dataset.moduleId;
    if (!moduleId) return;

    document.querySelectorAll('input[type="checkbox"][data-task]').forEach((checkbox, index) => {
        const storageKey = `${moduleId}-task-${index}`;

        // Load saved state
        checkbox.checked = localStorage.getItem(storageKey) === 'true';

        // Save on change
        checkbox.addEventListener('change', () => {
            localStorage.setItem(storageKey, checkbox.checked);
            updateModuleProgress(moduleId);
        });
    });
}

function updateModuleProgress(moduleId) {
    const checkboxes = document.querySelectorAll('input[type="checkbox"][data-task]');
    const total = checkboxes.length;
    const checked = Array.from(checkboxes).filter(cb => cb.checked).length;

    // If all tasks complete, mark module as complete
    if (total > 0 && checked === total) {
        window.progressTracker.markModuleComplete(moduleId);
    }
}

// ===== FORM VALIDATION =====
function initFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');

    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            let isValid = true;
            const formData = new FormData(form);

            // Validate email
            const email = formData.get('email');
            if (email && !isValidEmail(email)) {
                showError(form.querySelector('[name="email"]'), 'Email inválido');
                isValid = false;
            }

            // Validate required fields
            form.querySelectorAll('[required]').forEach(field => {
                if (!field.value.trim()) {
                    showError(field, 'Campo obrigatório');
                    isValid = false;
                }
            });

            if (isValid) {
                handleFormSubmit(form, formData);
            }
        });
    });
}

function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function showError(field, message) {
    // Remove existing error
    const existingError = field.parentElement.querySelector('.error-message');
    if (existingError) existingError.remove();

    // Add new error
    const error = document.createElement('p');
    error.className = 'error-message text-red-500 text-sm mt-1';
    error.textContent = message;
    field.parentElement.appendChild(error);
    field.classList.add('border-red-500');

    // Remove error on input
    field.addEventListener('input', () => {
        error.remove();
        field.classList.remove('border-red-500');
    }, { once: true });
}

function handleFormSubmit(form, formData) {
    const submitBtn = form.querySelector('[type="submit"]');
    const originalText = submitBtn.textContent;

    // Show loading
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="loading-spinner inline-block mr-2"></span> Enviando...';

    // Simulate API call (replace with actual API)
    setTimeout(() => {
        // Save to localStorage
        const email = formData.get('email');
        const name = formData.get('name');

        if (email) {
            localStorage.setItem('ftd-lead', JSON.stringify({
                email,
                name,
                timestamp: new Date().toISOString()
            }));
        }

        // Show success message
        showSuccessMessage(form);

        // Reset form
        form.reset();
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    }, 1500);
}

function showSuccessMessage(form) {
    const success = document.createElement('div');
    success.className = 'bg-green-50 border-2 border-green-500 text-green-800 px-6 py-4 rounded-lg mb-4 fade-in';
    success.innerHTML = `
        <div class="flex items-center gap-3">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
                <p class="font-semibold">Cadastro realizado com sucesso!</p>
                <p class="text-sm">Você receberá novidades sobre o FTD Pro em breve.</p>
            </div>
        </div>
    `;

    form.parentElement.insertBefore(success, form);

    setTimeout(() => {
        success.remove();
    }, 5000);
}

// ===== SCROLL ANIMATIONS =====
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.animate-on-scroll').forEach(el => {
        observer.observe(el);
    });
}

// ===== COPY TO CLIPBOARD =====
function initCopyButtons() {
    document.querySelectorAll('[data-copy]').forEach(btn => {
        btn.addEventListener('click', async () => {
            const text = btn.dataset.copy;
            try {
                await navigator.clipboard.writeText(text);
                showToast('Copiado para área de transferência!');
            } catch (err) {
                console.error('Failed to copy:', err);
            }
        });
    });
}

function showToast(message, duration = 3000) {
    const toast = document.createElement('div');
    toast.className = 'fixed bottom-4 right-4 bg-gray-900 text-white px-6 py-3 rounded-lg shadow-lg fade-in z-50';
    toast.textContent = message;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, duration);
}

// ===== VIDEO PLAYER =====
function initVideoPlayers() {
    document.querySelectorAll('.video-player').forEach(player => {
        const playBtn = player.querySelector('.play-button');
        const video = player.querySelector('video');

        if (playBtn && video) {
            playBtn.addEventListener('click', () => {
                if (video.paused) {
                    video.play();
                    playBtn.style.display = 'none';
                } else {
                    video.pause();
                    playBtn.style.display = 'block';
                }
            });

            video.addEventListener('ended', () => {
                playBtn.style.display = 'block';
            });
        }
    });
}

// ===== SEARCH FUNCTIONALITY =====
function initSearch() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    if (!searchInput || !searchResults) return;

    let debounceTimeout;

    searchInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimeout);

        debounceTimeout = setTimeout(() => {
            const query = e.target.value.toLowerCase().trim();

            if (query.length < 2) {
                searchResults.innerHTML = '';
                return;
            }

            performSearch(query, searchResults);
        }, 300);
    });
}

function performSearch(query, resultsContainer) {
    // Simple search implementation
    // In production, this would query an index or API
    const allContent = document.querySelectorAll('[data-searchable]');
    const results = [];

    allContent.forEach(element => {
        const text = element.textContent.toLowerCase();
        if (text.includes(query)) {
            results.push({
                title: element.dataset.title || 'Sem título',
                url: element.dataset.url || '#',
                excerpt: getExcerpt(text, query)
            });
        }
    });

    displaySearchResults(results, resultsContainer);
}

function getExcerpt(text, query, contextLength = 100) {
    const index = text.indexOf(query);
    const start = Math.max(0, index - contextLength);
    const end = Math.min(text.length, index + query.length + contextLength);

    return '...' + text.substring(start, end) + '...';
}

function displaySearchResults(results, container) {
    if (results.length === 0) {
        container.innerHTML = '<p class="text-gray-500 p-4">Nenhum resultado encontrado</p>';
        return;
    }

    container.innerHTML = results.map(result => `
        <a href="${result.url}" class="block p-4 hover:bg-gray-50 transition">
            <h4 class="font-semibold text-gray-800">${result.title}</h4>
            <p class="text-sm text-gray-600 mt-1">${result.excerpt}</p>
        </a>
    `).join('');
}

// ===== DARK MODE =====
function initDarkMode() {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    if (!darkModeToggle) return;

    // Check saved preference
    const isDark = localStorage.getItem('ftd-dark-mode') === 'true';
    if (isDark) {
        document.documentElement.classList.add('dark');
    }

    darkModeToggle.addEventListener('click', () => {
        document.documentElement.classList.toggle('dark');
        const isDarkNow = document.documentElement.classList.contains('dark');
        localStorage.setItem('ftd-dark-mode', isDarkNow);
    });
}

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', () => {
    // Initialize all features
    initMobileMenu();
    initSmoothScroll();
    initAccordions();
    initTaskCheckboxes();
    initFormValidation();
    initScrollAnimations();
    initCopyButtons();
    initVideoPlayers();
    initSearch();
    initDarkMode();

    // Initialize progress tracker
    window.progressTracker = new ProgressTracker();
    window.progressTracker.updateUI();

    console.log('FTD - Plataforma inicializada com sucesso! 🚀');
});

// ===== UTILITY FUNCTIONS =====
const utils = {
    // Format date
    formatDate(dateString) {
        const date = new Date(dateString);
        return new Intl.DateTimeFormat('pt-BR', {
            day: '2-digit',
            month: '2-digit',
            year: 'numeric'
        }).format(date);
    },

    // Format duration
    formatDuration(minutes) {
        const hours = Math.floor(minutes / 60);
        const mins = minutes % 60;
        return hours > 0 ? `${hours}h ${mins}min` : `${mins}min`;
    },

    // Slugify
    slugify(text) {
        return text
            .toLowerCase()
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '')
            .replace(/[^\w\s-]/g, '')
            .replace(/\s+/g, '-')
            .replace(/--+/g, '-')
            .trim();
    },

    // Truncate text
    truncate(text, maxLength) {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength).trim() + '...';
    }
};

// Export utilities to global scope
window.ftdUtils = utils;
