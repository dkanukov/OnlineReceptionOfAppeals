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
});

function createRequestAns(isOk) {
	if (isOk) {
		const offcanvasBody = document.createElement("div");
		offcanvasBody.classList.add("display-4", "text-success", "offcanvas-body");
		offcanvasBody.textContent = "Форма отправлена";
		feedbackForm.innerHTML = "";
		feedbackForm.append(offcanvasBody);
	} else {
		const offcanvasBody = document.createElement("div");
		offcanvasBody.classList.add("display-4", "text-danger", "offcanvas-body");
		offcanvasBody.textContent = "Произошла ошибка, обновите страницу";
		feedbackForm.innerHTML = "";
		feedbackForm.append(offcanvasBody);
	}
}



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

	feedbackSubmitBtn.addEventListener("click", async (e) => {
		e.preventDefault()
		const feedbackJSON = {
			author: feedbackName.value.trim(),
			content: feedbackText.value.trim(),
			rating: [...document.getElementsByClassName("rating__star__active")].length
		}

		await fetch("http://127.0.0.1:8000/api/feedback", {
			method: "POST", headers: {
				'Accept': 'application/json', 'Content-Type': 'application/json'
			}, body: JSON.stringify(feedbackJSON)
		})
			.then(res => {
				createRequestAns(res.ok);
			})
			.catch(err => {
				createRequestAns(false);
				console.log("Error: " + err);
			})
	});

});


