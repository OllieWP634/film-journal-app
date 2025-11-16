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