document.querySelectorAll('.poster').forEach(card => {
  card.addEventListener('click', () => {
    document.getElementById('filmModal').style.display = 'flex';
  });
});

document.getElementById('filmModal').addEventListener('click', (e) => {
  if (e.target.id === "filmModal") {
    document.getElementById('filmModal').style.display = 'none';
  }
});
