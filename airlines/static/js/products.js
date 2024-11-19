export function swipeCards() {
    return {
        init() {
            let isDown = false;
            let startX;
            let scrollLeft;
            this.$el.addEventListener('mousedown', (e) => {
                isDown = true;
                startX = e.pageX - this.$el.offsetLeft;
                scrollLeft = this.$el.scrollLeft;
            });
            this.$el.addEventListener('mouseleave', () => {
                isDown = false;
            });
            this.$el.addEventListener('mouseup', () => {
                isDown = false;
            });
            this.$el.addEventListener('mousemove', (e) => {
                if (!isDown) return;
                e.preventDefault();
                const x = e.pageX - this.$el.offsetLeft;
                const walk = (x - startX) * 1;
                this.$el.scrollLeft = scrollLeft - walk;
            });
        }
    };
}

