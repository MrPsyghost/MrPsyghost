const ua = navigator.userAgent || navigator.vendor;

if (/android/i.test(ua) || /iPhone|iPad|iPod/i.test(ua)) {
    const unavailable = document.getElementById('unavailable');
    unavailable.style.display = 'flex';
}

const updateAgeText = true;

function getAge() {
    return (Date.now() - new Date("2010-02-01T00:00:00Z").getTime()) / 31557600000;
}

function updateAge(age) {
    document.getElementById("age").textContent = 'I am ' + (age.toFixed(20)).toString() + ' years old';
}

updateAge(0);

if (!updateAgeText) {
    console.log('Updating the age is currently paused due to development.\nIf you see this message, please email MrPsyghost at shivaypuri2000@gmail.com.\nThank You!');
} else {
    updateAge(getAge());
    setInterval(() => updateAge(getAge()), 50);
}

lucide.createIcons();