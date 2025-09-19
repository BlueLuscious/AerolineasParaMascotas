export class CarrouselController {

    constructor(carrousel, autoplay=false, autoplayInterval=5000) {
        if (!carrousel) return console.error("Carrousel Element doesn't exists");
        
        this.carrousel = carrousel;
        this.track = this.carrousel.querySelector(`#${this.carrousel.id}_track`);
        this.slidesLength = this.track ? this.track.children.length : 0;
        this.indicators = this.carrousel.querySelector(`#${this.carrousel.id}_indicators`);
        this.previousButton = this.carrousel.querySelector(`#${this.carrousel.id}_previous_button`);
        this.nextButton = this.carrousel.querySelector(`#${this.carrousel.id}_next_button`);
        
        this.currentSlide = 0;
        this.autoplay = autoplay;
        this.autoplayInterval = autoplayInterval;

        if (this.previousButton && this.nextButton) {
            this.previousButton.addEventListener("click", () => this.moveSlide(-1));
            this.nextButton.addEventListener("click", () => this.moveSlide(1));
        }

        if (this.indicators) {
            Array.from(this.indicators.children).forEach((indicator, index) => {
                indicator.addEventListener("click", () => this.goToSlide(index));
            });
        }

        this.initAutoplay();
        this.updateUI();
    }

    goToSlide(index) {
        if (this.slidesLength <= 1) return;

        this.currentSlide = index;
        this.updateUI();
    }

    moveSlide(dir) {
        if (this.slidesLength <= 1) return;

        this.currentSlide = (this.currentSlide + dir + this.slidesLength) % this.slidesLength;
        this.updateUI();
    }

    updateUI() {
        if (this.track) {
            this.track.style.transform = `translateX(-${this.currentSlide * 100}%)`;
        }

        if (this.indicators?.children?.length) {
            Array.from(this.indicators.children).forEach((el, index) => {
                el.classList.toggle('bg-white/70', index === this.currentSlide);
                el.classList.toggle('bg-white/40', index !== this.currentSlide);
            });
        }

        if (this.currentSlide === 0) {
            this.previousButton?.classList.remove("opacity-100");
            this.previousButton?.classList.add("opacity-0", "pointer-events-none");
        } else {
            this.previousButton?.classList.remove("opacity-0", "pointer-events-none");
            this.previousButton?.classList.add("opacity-100");
        }

        if (this.currentSlide === this.slidesLength - 1) {
            this.nextButton?.classList.remove("opacity-100");
            this.nextButton?.classList.add("opacity-0", "pointer-events-none");
        } else {
            this.nextButton?.classList.remove("opacity-0", "pointer-events-none");
            this.nextButton?.classList.add("opacity-100");
        }
    }

    initAutoplay() {
        if (this.autoplay) {
            this.startAutoplay();
            this.carrousel.addEventListener("mouseenter", () => this.pauseAutoplay());
            this.carrousel.addEventListener("mouseleave", () => this.resumeAutoplay());
        }
    }

    startAutoplay() {
        if (this.slidesLength <= 1) return;

        this.autoplayDirection = this.autoplayDirection || 1;
        this.intervalId = setInterval(() => {
            let nextSlide = this.currentSlide + this.autoplayDirection;

            if (nextSlide < 0 || nextSlide >= this.slidesLength) {
                this.autoplayDirection *= -1;
                nextSlide = this.currentSlide + this.autoplayDirection;
            }

            this.moveSlide(this.autoplayDirection);
        }, this.autoplayInterval);
    }

    pauseAutoplay() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    resumeAutoplay() {
        if (!this.intervalId) {
            this.startAutoplay();
        }
    }

}
