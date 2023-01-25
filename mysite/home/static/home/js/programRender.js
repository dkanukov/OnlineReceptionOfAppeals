document.addEventListener('DOMContentLoaded', async function () {
    const params = new URLSearchParams(window.location.search).get('id');
    await fetch("http://158.160.35.42:8000/api/programs?id=" + params, {method: 'GET'})
        .then((res) => res.json())
        .then((data) => {
            document.getElementById('title').innerText = data.title;
            document.getElementById('description').innerText = data.description;
            document.getElementById('bgcImg').src = data.imageUrl;
        });
});




