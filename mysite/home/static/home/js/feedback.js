const ratingStars = [...document.getElementsByClassName("rating__star")];

for (let i = 0; i < ratingStars.length; ++i) {
	ratingStars[i].addEventListener("mouseover", () => {
		let j = i;
		while (j >= 0) {
			ratingStars[j].classList.add("rating__star__active");
			j--;
		}
	});

	ratingStars[i].addEventListener("click", (e) => {
		let j = i + 1;
		while (j <= 5) {
			ratingStars[j].classList.remove("rating__star__active");
			j++;
		}
	});
}
