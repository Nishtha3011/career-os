const canvas = document.getElementById('particles-canvas');
const ctx = canvas.getContext('2d');

let particlesArray;

// Set canvas size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Handle resize
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    init();
});

// Mouse interaction
const mouse = {
    x: null,
    y: null,
    radius: 150
}

window.addEventListener('mousemove', (event) => {
    mouse.x = event.clientX ?? event.x;
    mouse.y = event.clientY ?? event.y;
});

// Brighter colors (opacity 0.8)
const colors = [
    'rgba(139, 92, 246, 0.8)',   // Violet
    'rgba(192, 132, 252, 0.8)',  // Purple
    'rgba(99, 102, 241, 0.8)',   // Indigo
    'rgba(16, 185, 129, 0.8)'    // Emerald
];

class Particle {
    constructor(x, y, directionX, directionY, size, color) {
        this.x = x;
        this.y = y;
        this.directionX = directionX;
        this.directionY = directionY;
        this.size = size;
        this.color = color;
    }

    // Draw method
    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2, false);

        // Solid fill for visibility with soft glow
        ctx.fillStyle = this.color;
        ctx.shadowBlur = 6; // Reduced blur for "neat" look
        ctx.shadowColor = this.color;

        ctx.fill();
        ctx.shadowBlur = 0; // Reset
    }

    // Update method
    update() {
        // Check if particle is still within canvas
        if (this.x > canvas.width || this.x < 0) {
            this.directionX = -this.directionX;
        }
        if (this.y > canvas.height || this.y < 0) {
            this.directionY = -this.directionY;
        }

        // Mouse interaction - gentle attraction toward cursor
        if (mouse.x != null && mouse.y != null) {
            const dx = mouse.x - this.x;
            const dy = mouse.y - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            // Gentle attraction when within radius
            if (distance < mouse.radius && distance > 0) {
                const force = (mouse.radius - distance) / mouse.radius;
                this.x += (dx / distance) * force * 2;
                this.y += (dy / distance) * force * 2;
            }
        }

        // Move particle
        this.x += this.directionX;
        this.y += this.directionY;

        // Draw particle
        this.draw();
    }
}

function init() {
    particlesArray = [];
    let numberOfParticles = (canvas.height * canvas.width) / 7000; // Increased density

    for (let i = 0; i < numberOfParticles; i++) {
        let size = (Math.random() * 3) + 2; // Reduced size: 2-5px
        let x = (Math.random() * ((canvas.width - size * 2) - (size * 2)) + size * 2);
        let y = (Math.random() * ((canvas.height - size * 2) - (size * 2)) + size * 2);
        let directionX = (Math.random() * 0.4) - 0.2; // Slow speed
        let directionY = (Math.random() * 0.4) - 0.2;
        let color = colors[Math.floor(Math.random() * colors.length)];

        particlesArray.push(new Particle(x, y, directionX, directionY, size, color));
    }
}

function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = 0; i < particlesArray.length; i++) {
        particlesArray[i].update();
    }
}

init();
animate();
