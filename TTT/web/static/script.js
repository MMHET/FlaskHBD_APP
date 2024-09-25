document.addEventListener('DOMContentLoaded', function () {
    launchStarDustAndPopGemini();

    function launchStarDustAndPopGemini() {
        const starDustCanvas = document.getElementById('starDust');
        const ctx = starDustCanvas.getContext('2d');
        starDustCanvas.width = window.innerWidth;
        starDustCanvas.height = window.innerHeight;

        const stars = [];
        const starCount = 100;

        function createStar() {
            return {
                x: Math.random() * starDustCanvas.width,
                y: Math.random() * starDustCanvas.height,
                size: Math.random() * 2 + 1,
                speed: Math.random() * 0.5 + 0.2
            };
        }

        for (let i = 0; i < starCount; i++) {
            stars.push(createStar());
        }

        function drawStars() {
            ctx.clearRect(0, 0, starDustCanvas.width, starDustCanvas.height);

            stars.forEach(star => {
                ctx.beginPath();
                ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
                ctx.fillStyle = 'White';
                ctx.fill();
            });

            updateStars();
        }

        function updateStars() {
            for (let star of stars) {
                star.y += star.speed;
                if (star.y > starDustCanvas.height) {
                    star.y = 0;
                    star.x = Math.random() * starDustCanvas.width;
                }
            }
        }

        drawStars();

        // Pop Gemini star with fade in and out after a delay
        setTimeout(popGemini, 1500);

        function popGemini() {
            const geminiElement = document.getElementById('gemini');
            geminiElement.classList.remove('gemini-hidden');
            geminiElement.classList.add('gemini-fade-in');
            setTimeout(() => {
                geminiElement.classList.remove('gemini-fade-in');
                geminiElement.classList.add('gemini-fade-out');
            }, 2000); // Fade out after 2 seconds
            setTimeout(startCrawl, 2000); // Start crawl animation after 3 seconds
        }

        setInterval(drawStars, 30); // Continue star dust animation
    }

    function startCrawl() {
        const crawlElement = document.getElementById('crawl');
        crawlElement.style.display = 'block'; // Show crawl element
        crawlElement.style.transform = 'translateY(100%)'; // Start from bottom of the screen
        crawlElement.style.transition = 'transform 60s linear'; // Slow transition with 60s duration

        // Move crawl text to the center of the screen
        setTimeout(() => {
            crawlElement.style.transform = 'translateY(calc(-100vh - 200px))'; // Move text upwards by 100vh + 200px
        }, 50);
    }
});