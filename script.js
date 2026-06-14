document.addEventListener('DOMContentLoaded', function() {
    // ============ 移动端菜单 ============
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const closeMobileMenu = document.getElementById('close-mobile-menu');
    
    function openMobileMenu() {
        mobileMenu.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }
    
    function closeMobileMenuFn() {
        mobileMenu.classList.add('hidden');
        document.body.style.overflow = '';
    }
    
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', openMobileMenu);
    }
    
    if (closeMobileMenu) {
        closeMobileMenu.addEventListener('click', closeMobileMenuFn);
    }
    
    // 移动端菜单链接点击后关闭
    mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', closeMobileMenuFn);
    });
    
    // ============ 平滑滚动 ============
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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
    
    // ============ 滚动触发动画 ============
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // 可选：触发后不再观察
                // revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    revealElements.forEach(el => revealObserver.observe(el));
    
    // ============ 导航栏滚动效果 ============
    const navbar = document.querySelector('nav');
    let lastScrollY = window.scrollY;
    
    function handleScroll() {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > 100) {
            navbar.classList.add('shadow-xl');
            navbar.querySelector('div').classList.add('py-3');
            navbar.querySelector('div').classList.remove('py-5');
        } else {
            navbar.classList.remove('shadow-xl');
            navbar.querySelector('div').classList.remove('py-3');
            navbar.querySelector('div').classList.add('py-5');
        }
        
        lastScrollY = currentScrollY;
    }
    
    window.addEventListener('scroll', handleScroll);
    
    // ============ 项目弹窗 ============
    const travelModal = document.getElementById('travel-modal');
    const canalModal = document.getElementById('canal-modal');
    const closeTravelModal = document.getElementById('close-travel-modal');
    const closeCanalModal = document.getElementById('close-canal-modal');
    
    function openModal(modal) {
        if (modal) {
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }
    }
    
    function closeModal(modal) {
        if (modal) {
            modal.classList.add('hidden');
            document.body.style.overflow = '';
        }
    }
    
    // 打开弹窗
    const projectCards = document.querySelectorAll('.project-card');
    if (projectCards.length >= 2) {
        projectCards[0].addEventListener('click', () => openModal(travelModal));
        projectCards[1].addEventListener('click', () => openModal(canalModal));
    }
    
    // 关闭弹窗按钮
    if (closeTravelModal) {
        closeTravelModal.addEventListener('click', () => closeModal(travelModal));
    }
    if (closeCanalModal) {
        closeCanalModal.addEventListener('click', () => closeModal(canalModal));
    }
    
    // 点击背景关闭弹窗
    [travelModal, canalModal].forEach(modal => {
        if (modal) {
            modal.addEventListener('click', (e) => {
                if (e.target === modal.querySelector('.modal-backdrop')) {
                    closeModal(modal);
                }
            });
        }
    });
    
    // ESC键关闭弹窗
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeModal(travelModal);
            closeModal(canalModal);
            closeMobileMenuFn();
        }
    });
    
    // ============ 图片懒加载 ============
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                imageObserver.unobserve(img);
            }
        });
    });
    
    lazyImages.forEach(img => imageObserver.observe(img));
    
    // ============ 技能标签动画 ============
    const skillTags = document.querySelectorAll('.skill-tag');
    
    skillTags.forEach(tag => {
        tag.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.05)';
        });
        
        tag.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // ============ 打字机效果（可选） ============
    const typewriterElement = document.querySelector('.typewriter');
    if (typewriterElement) {
        const text = typewriterElement.textContent;
        typewriterElement.textContent = '';
        typewriterElement.style.width = 'auto';
        
        let i = 0;
        function typeWriter() {
            if (i < text.length) {
                typewriterElement.textContent += text.charAt(i);
                i++;
                setTimeout(typeWriter, 100);
            }
        }
        
        // 当元素进入视口时开始打字
        const typewriterObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                typeWriter();
                typewriterObserver.unobserve(typewriterElement);
            }
        });
        
        typewriterObserver.observe(typewriterElement);
    }
    
    // ============ 鼠标跟随效果（可选） ============
    const cursor = document.createElement('div');
    cursor.className = 'custom-cursor';
    cursor.style.cssText = `
        position: fixed;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: rgba(59, 130, 246, 0.3);
        pointer-events: none;
        z-index: 9999;
        transition: transform 0.1s ease;
        mix-blend-mode: difference;
        display: none;
    `;
    document.body.appendChild(cursor);
    
    // 只在桌面端显示自定义光标
    if (window.matchMedia('(pointer: fine)').matches) {
        cursor.style.display = 'block';
        
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX - 10 + 'px';
            cursor.style.top = e.clientY - 10 + 'px';
        });
        
        // 悬停在可点击元素上时放大
        const clickables = document.querySelectorAll('a, button, .project-card, .skill-tag');
        clickables.forEach(el => {
            el.addEventListener('mouseenter', () => {
                cursor.style.transform = 'scale(2)';
                cursor.style.background = 'rgba(59, 130, 246, 0.5)';
            });
            el.addEventListener('mouseleave', () => {
                cursor.style.transform = 'scale(1)';
                cursor.style.background = 'rgba(59, 130, 246, 0.3)';
            });
        });
    }
    
    // ============ 页面加载动画 ============
    window.addEventListener('load', () => {
        document.body.classList.add('loaded');
    });
    
    // ============ 滚动进度指示器 ============
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: linear-gradient(90deg, #3B82F6, #8B5CF6);
        z-index: 9999;
        transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);
    
    function updateProgress() {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = (scrollTop / docHeight) * 100;
        progressBar.style.width = progress + '%';
    }
    
    window.addEventListener('scroll', updateProgress);
    updateProgress();
});

// ============ 复制联系方式功能 ============
function copyContact(text, type) {
    // 使用现代 Clipboard API
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            showCopyToast(type);
        }).catch(() => {
            fallbackCopy(text, type);
        });
    } else {
        fallbackCopy(text, type);
    }
}

function fallbackCopy(text, type) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-9999px';
    document.body.appendChild(textArea);
    textArea.select();
    
    try {
        document.execCommand('copy');
        showCopyToast(type);
    } catch (err) {
        console.error('复制失败:', err);
    }
    
    document.body.removeChild(textArea);
}

function showCopyToast(type) {
    const toast = document.getElementById('copy-toast');
    const toastText = toast.querySelector('span');
    toastText.textContent = type + '已复制到剪贴板';
    
    toast.classList.remove('translate-y-20', 'opacity-0');
    toast.classList.add('translate-y-0', 'opacity-100');
    
    setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-20', 'opacity-0');
    }, 2500);
}