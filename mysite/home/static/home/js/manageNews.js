async function fetchNews() {
    const res = await fetch("http://127.0.0.1:8001/api/news?id=7", {
        method: 'GET',
    })
    console.log(await res.json());
}
document.addEventListener("DOMContentLoaded", () => {
    console.log("Answer is");
    fetchNews();
})

