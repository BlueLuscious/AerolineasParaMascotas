export class FabController {

    constructor(element_id) {
        this.element = document.getElementById(element_id);
        if (!this.element) return;

        this.fabButton = this.element.querySelector(`#${element_id}_button`);
        this.optionsContainer = this.element.querySelector(`#${element_id}_options`);
        this.isOpen = false;

        document.addEventListener("click", (e) => {
            if (!this.fabButton.contains(e.target)) this.close();
        })
        this.fabButton.addEventListener("click", () => this.toggle());

        if (this.optionsContainer?.children?.length) {
            Array.from(this.optionsContainer.children).forEach((opt) => {
                opt.addEventListener("click", () => this.toggle());
            });
        }
    }

    toggle() {
        this.isOpen = !this.isOpen;
        this.optionsContainer.classList.toggle("opacity-0", !this.isOpen);
        this.optionsContainer.classList.toggle("pointer-events-none", !this.isOpen);
        this.optionsContainer.classList.toggle("opacity-100", this.isOpen);
    }

    close() {
        this.isOpen = false;
        this.optionsContainer.classList.add("opacity-0", "pointer-events-none");
        this.optionsContainer.classList.remove("opacity-100");
    }

}
