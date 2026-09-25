const developing = false;

function getAge() {
    return (Date.now() - new Date("2010-02-01T00:00:00Z").getTime()) / 31557600000;
}

function updateAge(age) {
    const ageElement = document.getElementById("age");
    if (!ageElement) return;
    ageElement.textContent = 'I am ' + (age.toFixed(20)).toString() + ' years old';
}

function openProject(p) {
    window.location.href = '/projects/' + encodeURIComponent(p.dataset.name);
}

if (!developing) {
    const ua = navigator.userAgent || navigator.vendor;
    
    if (/android/i.test(ua) || /iPhone|iPad|iPod/i.test(ua)) {
        const unavailable = document.getElementById('unavailable');
        unavailable.style.display = 'flex';
    }

    updateAge(getAge());
    setInterval(() => updateAge(getAge()), 50);
} else {
    updateAge(0);
    console.log('If you see this message, please email MrPsyghost at shivaypuri2000@gmail.com.\nThank You!');
}

lucide.createIcons();