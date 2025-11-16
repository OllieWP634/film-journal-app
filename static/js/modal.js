function openModal(index) {
    const modal = document.getElementById('poster');
    modal.style.display = 'block';
    modal.dataset.cardIndex = index;
}

function saveFilm() {
    const index = document.getElementById('film-modal').dataset.cardIndex;
    const filmName = document.getElementById('film-input').value;
    selectedFilms[index] = filmName;
    document.getElementById(`card-${index}`).innerText = filmName;
    closeModal();
}

function generateRecommendations() {
    fetch('/submit-films', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ films: selectedFilms })
    })
    .then(res => res.json())
    .then(data => {
        displayRecommendations(data.recommended);
    });
}