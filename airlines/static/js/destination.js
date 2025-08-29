const modal = document.getElementById("modal");
const sheet = modal.querySelector("#bottom_sheet");
const sliderBar = sheet.querySelector("#slider_bar")
const modalContent = sheet.querySelector("#content_modal")
const modalQuotationBtn = sheet.querySelector("#modal_quotation_button")
const cards = document.querySelectorAll(".card");

// Rotate Effect
cards.forEach(card => {
	card.addEventListener("mousemove", (e) => {
		const rect = card.getBoundingClientRect();
		const x = e.clientX - rect.left;
		const y = e.clientY - rect.top;
		const centerX = rect.width / 2;
		const centerY = rect.height / 2;
		const rotateX = -(y - centerY) / 10;
		const rotateY = (x - centerX) / 10;

		card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.1)`;
	});

	card.addEventListener("mouseleave", () => {
		card.style.transform = "rotateX(0deg) rotateY(0deg) scale(1)";
	});
});


// Open Modal when unicorn is updated.
window.addEventListener("DOMContentLoaded", (event) => {
    Unicorn.addEventListener("updated", (component) => {
		if (component.name === "modal" && component.data.destination && Object.keys(component.data.destination).length > 0) {
			openModal();
		}
	});
});

function updateDestination(name="") {
	setTimeout(() => {
		Unicorn.call("modal", "select_destination", name);
	}, 50);
};


modalQuotationBtn.addEventListener("click", () => {
	closeModal();
	updateDestination();
});

// Close Modal by touching outside of it
document.addEventListener("click", (e) => {
	const clickedInsideSheet = sheet.contains(e.target);
	const clickedOnCard = Array.from(cards).some(card => card.contains(e.target));
	if (!clickedInsideSheet && !clickedOnCard) {
		closeModal();
		updateDestination();
	}
});

// Open Modal
function openModal() {
	modal.classList.remove("hidden");
	document.body.classList.add("overflow-hidden");

	setTimeout(() => {
		sheet.classList.remove("translate-y-full");
	}, 300);
}


// Close Modal
function closeModal() {
	sheet.classList.add("translate-y-full");
	document.body.classList.remove("overflow-hidden");

	setTimeout(() => {
		modal.classList.add("hidden");
	}, 300);
}


// Pointer events (Slide modal)
let startY = 0;
let currentY = 0;
let isDragging = false;

sliderBar.addEventListener("pointerdown", (e) => {
	startY = e.clientY;
	isDragging = true;
	sliderBar.setPointerCapture(e.pointerId)
});

sliderBar.addEventListener("pointermove", (e) => {
	if (!isDragging) return;

	currentY = e.clientY;
	const diff = currentY - startY;

	if (diff > 0) {
		sheet.style.transform = `translate(-50%, ${diff}px)`;
	}
});

sliderBar.addEventListener("pointerup", () => {
	isDragging = false;

	const diff = currentY - startY;
	if (diff > 100 && sheet.scrollTop === 0) {
		sheet.style.transform = "";
		requestAnimationFrame(() => {
			sheet.classList.add("translate-y-full");
			setTimeout(() => {
				closeModal();
				updateDestination();
			}, 300);
		});
	} else {
		sheet.style.transform = "";
	}
});
