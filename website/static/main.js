let updateAgeText = true;

function getAge() {
    return (Date.now() - new Date("2010-02-01T00:00:00Z").getTime()) / 31557600000;
}

function updateAge(age) {
    document.getElementById("age").textContent = 'I am ' + (age.toFixed(20)).toString() + ' years old';
}

document.querySelectorAll('.project').forEach(project => {
    project.style.backgroundImage = `url("${project.dataset.image}")`;
});

updateAge(0);

if (!updateAgeText) {
    console.log('Updating is currently paused due to development.\nIf you see this message, please email MrPsyghost at shivaypuri2000@gmail.com.\nThank You!');
} else {
    updateAge(getAge());
    setInterval(() => updateAge(getAge()), 50);
}

lucide.createIcons();