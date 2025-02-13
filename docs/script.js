
document.addEventListener("DOMContentLoaded", function () {
    fetch("content.json")
        .then(response => response.json())
        .then(data => {
            const slides = data.slides;
            let currentSlide = 0;

            function renderSlide(index) {
                const slide = slides[index];
                document.querySelector(".container").innerHTML = `
                    <div class="slide active">
                        <h1>${slide.title}</h1>
                        <p>${slide.text}</p>
                        ${slide.link ? `<p class="highlight"><a href="${slide.link}" target="_blank">${slide.highlight}</a></p>` : ""}
                        ${slide.image ? `<img src="${slide.image}" alt="Slide Image" class="slide-image">` : ""}
                        ${slide.code ? `<div class="code-box"><pre>${slide.code.join("\n")}</pre></div>` : ""}
                        <div>
                            ${slide.prev !== undefined ? `<button class="button" onclick="renderSlide(${slide.prev})">⬅️ Zurück</button>` : ""}
                            ${slide.next !== undefined ? `<button class="button" onclick="renderSlide(${slide.next})">Weiter 👉</button>` : ""}
                        </div>
                    </div>`;
            }

            window.renderSlide = renderSlide;
            renderSlide(currentSlide);
        });
});
