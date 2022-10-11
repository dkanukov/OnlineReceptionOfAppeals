const header = document.getElementById('mainHeader');
const date = document.getElementById('date');
const textBeforePhoto = document.getElementById('textBeforePhoto');
const img = document.getElementById('img');
const textAfterPhoto = document.getElementById('textAfterPhoto');
document.addEventListener('DOMContentLoaded', async function () {
    const params = new URLSearchParams(window.location.search).get('id');
    await fetch("https://dfvrn.pythonanywhere.com/api/news?id=" + params, {method: 'GET'})
        .then((res) => res.json())
        .then(function(data) {
            header.innerText = data.caption;
            date.innerText = data.date;
            img.src = data.imageUrl;
            textBeforePhoto.innerText = data.textBeforePhoto;
            textAfterPhoto.innerText = data.textAfterPhoto;
        })
});
