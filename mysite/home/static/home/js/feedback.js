const feedbackForm = document.getElementById("offcanvasRight");
const ratingStars = [...document.getElementsByClassName("rating__star")];
const feedbackName = document.getElementById("feedbackNameInput");
const feedbackText = document.getElementById("feedbackTextInput");
const feedbackSubmitBtn = document.getElementById("feedbackSubmitBtn");

const starsObserver = new MutationObserver(mutationsRecords => {
	mutationsRecords.forEach((mutation) => {
		if (mutation.type === "attributes") feedbackSubmitBtn.disabled = !(feedbackText.value.trim() !== "" && feedbackName.value.trim() !== "" && [...document.getElementsByClassName("rating__star__active")].length !== 0);
	});
});

ratingStars.forEach(star => {
	starsObserver.observe(star, {attributes: true});
})

document.addEventListener("DOMContentLoaded", () => {
	//managed star rating mark
	for (let i = 0; i < ratingStars.length; ++i) {
		ratingStars[i].addEventListener("mouseover", () => {
			let j = i;
			while (j >= 0) {
				ratingStars[j].classList.add("rating__star__active");
				j--;
			}
		});

		ratingStars[i].addEventListener("click", () => {
			let j = i + 1;
			while (j <= 5) {
				ratingStars[j].classList.remove("rating__star__active");
				j++;
			}
		});
	}

	feedbackName.addEventListener("input", () => {
		feedbackSubmitBtn.disabled = !(feedbackText.value.trim() !== "" && feedbackName.value.trim() !== "" && [...document.getElementsByClassName("rating__star__active")].length !== 0);
	});

	feedbackText.addEventListener("input", () => {
		feedbackSubmitBtn.disabled = !(feedbackText.value.trim() !== "" && feedbackName.value.trim() !== "" && [...document.getElementsByClassName("rating__star__active")].length !== 0);
	});

	feedbackSubmitBtn.addEventListener("click", () => {
		//TODO: manage form sending

		// const offcanvasBody = document.createElement("div");
		// offcanvasBody.classList.add("display-4", "text-success", "offcanvas-body");
		// offcanvasBody.textContent = "Форма отправлена";
		// feedbackForm.innerHTML = "";
		// feedbackForm.append(offcanvasBody);

	});

});


