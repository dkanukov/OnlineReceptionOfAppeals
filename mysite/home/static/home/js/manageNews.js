// async function fetchNews() {
//     const res = await fetch("http://127.0.0.1:8000/api/news?id=1", {
//         method: 'GET',
//     })
//     return await res.json()
// }
// document.addEventListener("DOMContentLoaded", () => {
//     fetchNews().then(r => console.log(r));
// })

(function () {
    const link = document.querySelectorAll("#pageLink");
    link.forEach(el => {
      el.addEventListener("click", () => {
          window.location.href = el.getAttribute("href");
      });
    });
})();

