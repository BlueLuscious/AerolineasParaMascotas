// MD & Larger Screens //
let currentSlide = 0;
const carrousel = document.getElementById("carrousel-slides");
const totalSlides = carrousel.children.length;

function updateCarrousel() {
  carrousel.style.transform = `translateX(-${currentSlide * 100}vw)`;
  for (let i = 0; i < totalSlides; i++) {
    const dot = document.getElementById(`indicator-${i}`);
    dot.classList.remove("bg-primary-blue_extralight");
    dot.classList.add("bg-primary-blue_extralight/50");
  }
  const active = document.getElementById(`indicator-${currentSlide}`);
  active.classList.remove("bg-primary-blue_extralight/50");
  active.classList.add("bg-primary-blue_extralight");
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % totalSlides;
  updateCarrousel();
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
  updateCarrousel();
}

function goToSlide(index) {
  currentSlide = index;
  updateCarrousel();
}

setInterval(nextSlide, 5000);
updateCarrousel();


// Moblie //
let startX = 0;
let endX = 0;

carrousel.addEventListener("touchstart", (e) => {
  startX = e.touches[0].clientX;
});

carrousel.addEventListener("touchend", (e) => {
  endX = e.changedTouches[0].clientX;
  handleSwipe();
});

function handleSwipe() {
  const threshold = 50;
  const deltaX = endX - startX;

  if (Math.abs(deltaX) > threshold) {
    if (deltaX > 0) {
      prevSlide();
    } else {
      nextSlide();
    }
  }
}
