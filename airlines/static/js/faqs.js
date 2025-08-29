document.addEventListener("DOMContentLoaded", () => {
    const accordion = document.getElementById("faq_accordion");
    const questions = accordion.querySelectorAll(".question");

    questions.forEach((question) => {
        question.addEventListener("click", () => {
            const content = question.nextElementSibling;
            const icon = question.querySelector("svg");

            // Cerrar todos
            accordion.querySelectorAll(".answer").forEach((el) => {
                if (el !== content) {
                    el.style.maxHeight = "0px";
                    el.previousElementSibling.querySelector("svg").classList.remove("rotate-180");
                }
            });

            // Alternar el actual
            const isOpen = content.style.maxHeight && content.style.maxHeight !== "0px";
            if (isOpen) {
                content.style.maxHeight = "0px";
                icon.classList.remove("rotate-180");
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
                icon.classList.add("rotate-180");
            }
        });
    });
});
