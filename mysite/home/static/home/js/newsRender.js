const header = document.getElementById('mainHeader');
const date = document.getElementById('date');
const textBeforePhoto = document.getElementById('textBeforePhoto');
const img = document.getElementById('img');
const textAfterPhoto = document.getElementById('textAfterPhoto');
document.addEventListener('DOMContentLoaded', async function () {
    const params = new URLSearchParams(window.location.search).get('id');
    const res = await fetch("http://127.0.0.1:8000/api/news?id=" + params, {method: 'GET'})
        .then((res) => res.json())
        .then(function(data) {
            console.log(data);
            header.innerText = data.caption;
            date.innerText = data.date;
            img.src = data.image_url;
            textBeforePhoto.innerText = data.text_before_photo;
            textAfterPhoto.innerText = data.text_after_photo;
        })
});
