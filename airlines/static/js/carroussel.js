const track = document.querySelector(".carousel-track")
const items = document.querySelectorAll(".carousel-item")
let currentIndex = 0
const itemCount = items.length

function updateVisibleItems() {
    if (window.innerWidth >= 1024) {
        visibleItems = 3
    } else if (window.innerWidth >= 768 && window.innerWidth < 1024) {
        visibleItems = 2
    } else {
        visibleItems = 1
    }
}

function moveToNext() {  
    // Incrementamos el índice actual teniendo en cuenta los ítems visibles
    currentIndex = (currentIndex + 1) % (itemCount - visibleItems + 1)

    // Calculamos el ancho de los ítems
    const itemWidth = items[0].getBoundingClientRect().width

    // Movemos el track la cantidad adecuada de píxeles
    track.style.transform = `translateX(-${currentIndex * itemWidth}px)`
}

setInterval(() => {
    updateVisibleItems()
    moveToNext()
}, 3000)

window.addEventListener("resize", () => {
    currentIndex = 0
    track.style.transform = `translateX(0)`
    updateVisibleItems()
})

updateVisibleItems()
