const area = document.getElementById('newsArea');
const newElem = document.createElement('div');
const link = document.createElement('a');
const card = document.createElement('div');
const img = document.createElement('img');
const cardBody = document.createElement('div');
const cardTitle = document.createElement('h5');
newElem.className = 'col';
link.href = './news.html?id=' + 1;
newElem.appendChild(link);
card.className = 'card';
card.style.outline = '1px solid gray'
link.appendChild(card);
img.src = '../../static/img/news_' + 1 + '.png';
img.className = 'card-img-top';
card.appendChild(img);
cardBody.className = 'card-body';
cardTitle.className = 'card-title text-dark';
cardTitle.innerText = "lorem ipsum";
cardBody.append(cardTitle)
card.appendChild(cardBody);

(function () {
    area.appendChild(newElem);
})();
