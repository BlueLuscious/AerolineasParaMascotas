const modal = document.getElementById("modal");
const sheet = modal.querySelector("#bottom_sheet");
const sliderBar = sheet.querySelector("#slider_bar")
const modalContent = sheet.querySelector("#content_modal")
const cards = document.querySelectorAll(".card");

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

function openModalWithData(name) {
	Unicorn.call("modal", "select_destination", name)
	setTimeout(() => {
		openModal()
	}, 200);
}

document.addEventListener("click", (e) => {
	const clickedInsideSheet = sheet.contains(e.target);
	const clickedOnCard = Array.from(cards).some(card => card.contains(e.target));
	if (!clickedInsideSheet && !clickedOnCard) {
		closeModal()
	}
});


function openModal() {
	modal.classList.remove("hidden");
	document.body.classList.add("overflow-hidden");

	setTimeout(() => {
		sheet.classList.remove("translate-y-full");
	}, 200);
}

function closeModal() {
	sheet.classList.add("translate-y-full");
	document.body.classList.remove("overflow-hidden");

	setTimeout(() => {
		modal.classList.add("hidden");
	}, 200);
}


// Pointer events
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
			setTimeout(() => closeModal(), 200);
		});
	} else {
		sheet.style.transform = "";
	}
});
