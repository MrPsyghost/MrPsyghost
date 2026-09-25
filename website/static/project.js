function selectImg(img) {
    document.getElementById('selected').removeAttribute('id');
    img.id = 'selected';
    document.getElementById('img').querySelector('img').src = img.querySelector('img').src;
}

function leftImg() {
    const selected = document.getElementById('selected');
    const previous = selected?.previousElementSibling;

    if (!previous || !previous.classList.contains('p-img')) return;

    selected.removeAttribute('id');
    previous.id = 'selected';

    document.getElementById('img').querySelector('img').src =
        previous.querySelector('img').src;

    previous.scrollIntoView({
        behavior: 'smooth',
        block: 'nearest',
        inline: 'center'
    });
}

function rightImg() {
    const selected = document.getElementById('selected');
    const next = selected?.nextElementSibling;

    if (!next || !next.classList.contains('p-img')) return;

    selected.removeAttribute('id');
    next.id = 'selected';

    document.getElementById('img').querySelector('img').src =
        next.querySelector('img').src;

    next.scrollIntoView({
        behavior: 'smooth',
        block: 'nearest',
        inline: 'center'
    });
}