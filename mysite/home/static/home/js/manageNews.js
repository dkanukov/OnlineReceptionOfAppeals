async function fetchNews() {
    const res = await fetch("http://127.0.0.1/api/news", {
        method: 'POST',
        body: {
            "id": "2"
        }
    })
    console.log(await res.json());
}
document.addEventListener("DOMContentLoaded", () => {
    console.log("Answer is");
    fetchNews();
})

