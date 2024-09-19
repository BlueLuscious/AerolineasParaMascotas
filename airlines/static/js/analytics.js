const targets = [
    { element: document.getElementById('countries'), count: 20, suffix: '+' },
    { element: document.getElementById('pets'), count: 50, suffix: '+' },
    { element: document.getElementById('years'), count: 5, suffix: '+' }
  ];

  const maxCount = Math.max(...targets.map(target => target.count));

  function animateCountUp(target, duration) {
    let currentCount = 0;
    const increment = Math.ceil(target.count / (duration / 10));

    const interval = setInterval(() => {
      currentCount += increment;
      if (currentCount >= target.count) {
        clearInterval(interval);
        currentCount = target.count;
        target.element.textContent = currentCount + target.suffix;
      } else {
        target.element.textContent = currentCount;
      }
    }, 50);
  }

  function handleIntersection(entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        targets.forEach(target => {
          animateCountUp(target, maxCount / 0.1); 
        });
        observer.unobserve(entry.target);
      }
    });
  }
  const observer = new IntersectionObserver(handleIntersection, {
    threshold: 1 
  });

  observer.observe(document.getElementById('statsSection'));