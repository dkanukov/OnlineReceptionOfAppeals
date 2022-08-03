document.addEventListener('DOMContentLoaded', async function () {
    const params = new URLSearchParams(window.location.search).get('id');
    const res = await fetch("http://127.0.0.1:8000/api/programs?id=" + params, {method: 'GET'});
    const data = await res.json();
    console.log(data);
});
