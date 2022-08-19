document.addEventListener('DOMContentLoaded', async function () {
    const params = new URLSearchParams(window.location.search).get('id');
    await fetch("http://127.0.0.1:8000/api/programs?id=" + params, {method: 'GET'})
        .then((res) => res.json())
        .then((data) => {
            console.log("Ура! файл обновился");
            document.getElementById('caption').innerText = data.title;
        })
    // const res = await fetch("http://127.0.0.1:8000/api/programs?id=" + params, {method: 'GET'});
    // const data = await res.json();
    // console.log(data);
});
