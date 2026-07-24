/*
  IK Göta – delad presentationsmotor.
  Bygger navigering (piltangenter, klick, prickar) utifrån alla
  .slide-element som finns i .deck. Lägg inte presentationsinnehåll här.
*/
(function () {
  const deck = document.querySelector(".deck");
  if (!deck) return;

  const slides = Array.from(deck.querySelectorAll(".slide"));
  const dotsWrap = deck.querySelector(".dots");
  const progressFill = deck.querySelector(".progress-fill");
  const prevBtn = deck.querySelector(".nav-prev");
  const nextBtn = deck.querySelector(".nav-next");
  const counter = deck.querySelector(".slide-counter");

  let current = slides.findIndex((s) => s.classList.contains("active"));
  if (current < 0) current = 0;

  slides.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.className = "dot" + (i === current ? " active" : "");
    dot.setAttribute("aria-label", "Gå till bild " + (i + 1));
    dot.addEventListener("click", () => goTo(i));
    dotsWrap && dotsWrap.appendChild(dot);
  });

  function render() {
    slides.forEach((slide, i) => {
      slide.classList.toggle("active", i === current);
      slide.classList.toggle("exit-left", i < current);
    });
    if (dotsWrap) {
      Array.from(dotsWrap.children).forEach((dot, i) => {
        dot.classList.toggle("active", i === current);
      });
    }
    if (progressFill) {
      progressFill.style.width = ((current + 1) / slides.length) * 100 + "%";
    }
    if (counter) {
      counter.textContent = current + 1 + " / " + slides.length;
    }
    if (prevBtn) prevBtn.disabled = current === 0;
    if (nextBtn) nextBtn.disabled = current === slides.length - 1;
  }

  function goTo(index) {
    if (index < 0 || index >= slides.length) return;
    current = index;
    render();
  }

  function next() {
    goTo(current + 1);
  }

  function prev() {
    goTo(current - 1);
  }

  nextBtn && nextBtn.addEventListener("click", next);
  prevBtn && prevBtn.addEventListener("click", prev);

  document.addEventListener("keydown", (e) => {
    if (["ArrowRight", "ArrowDown", " ", "PageDown"].includes(e.key)) {
      e.preventDefault();
      next();
    } else if (["ArrowLeft", "ArrowUp", "PageUp"].includes(e.key)) {
      e.preventDefault();
      prev();
    } else if (e.key === "Home") {
      goTo(0);
    } else if (e.key === "End") {
      goTo(slides.length - 1);
    } else if (e.key === "f" || e.key === "F") {
      if (document.fullscreenElement) {
        document.exitFullscreen();
      } else {
        document.documentElement.requestFullscreen();
      }
    }
  });

  // Enkel svep-navigering för touch-skärmar
  let touchStartX = null;
  deck.addEventListener("touchstart", (e) => {
    touchStartX = e.touches[0].clientX;
  });
  deck.addEventListener("touchend", (e) => {
    if (touchStartX === null) return;
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 50) {
      dx < 0 ? next() : prev();
    }
    touchStartX = null;
  });

  render();
})();
