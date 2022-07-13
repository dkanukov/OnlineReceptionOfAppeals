(function () {
    const formBtn = document.getElementById('formBtn');
    formBtn.addEventListener('click', function (e) {
        e.preventDefault();
        console.log('clicked');
    });
})();

// async function fetchData() {
//     const res = fetch('/api/donate', {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//             'ID': '12'
//         }
//     });
// }
