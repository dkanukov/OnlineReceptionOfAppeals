const nameInput = document.getElementById("nameFormInput");
const surnameInput = document.getElementById("surnameFormInput");
const phoneInput = document.getElementById("phoneFormInput");
const typeOfHelpSelect = document.getElementById("typeOfHelp");
const typeOfConsultationSelect = document.getElementById("typeOfConsultation");
const personalDataValidstionCheckbox = document.getElementById("checkboxForm");
const tabs = [...document.querySelectorAll(".tab-pane.appeal")];
const submitBtn = document.getElementById("submitForm");

const tabObserver = new MutationObserver(mutationRecords => {
	mutationRecords.forEach(mutation => {
		if (mutation.type === "attributes") manageCurrentTab();
	})
});

tabs.forEach(tab => {
	tabObserver.observe(tab, {attributes: true});
})

const maskOptions = {
	mask: '+{7}(000)000-00-00'
};
const mask = IMask(phoneInput, maskOptions);

function createRequestAnswer(isOk) {
	const modal = document.getElementsByClassName("modal-content");
	const modalBody = document.createElement("div");
	if (isOk) {
		modalBody.classList.add("display-4", "text-success", "modal-body");
		modalBody.textContent = "Форма отправлена";
		modal[0].innerHTML = "";
		modal[0].append(modalBody);
	} else {
		modalBody.classList.add("display-4", "text-danger", "modal-body");
		modalBody.textContent = "Произошла ошибка. Обновите страницу";
		modal[0].innerHTML = "";
		modal[0].append(modalBody);
	}
}

function manageCurrentTab() {
	const currentTab = document.querySelector(".tab-pane.active.show");
	if (currentTab) {
		submitBtn.disabled = !(nameInput.value.trim() !== "" && surnameInput.value.trim() !== "" && phoneInput.value.length === 16 && personalDataValidstionCheckbox.checked)
	}
}

document.addEventListener("DOMContentLoaded", () => {
	submitBtn.addEventListener("click", async (e) => {
		e.preventDefault();
		const currentTab = document.querySelector(".tab-pane.active.show");
		let typeAppeal;
		let optionAppeal;
		switch (currentTab.id) {
			case "appealHelp": typeAppeal = 1; optionAppeal = typeOfHelpSelect.value; break;
			case "appealConsultation": typeAppeal = 2; optionAppeal = typeOfConsultationSelect.value; break;
			case "appealVolunteer": typeAppeal = 3; optionAppeal = 1; break;
			default: typeAppeal = null; optionAppeal = null;
		}
		const appealForm = {
			type: JSON.stringify(typeAppeal),
			name: nameInput.value,
			last_name: surnameInput.value,
			phone_number: phoneInput.value,
			option: optionAppeal
		}

		await fetch("http://dfvrn.pythonanywhere.com/api/appeal", {
			method: "POST", headers: {
				'Accept': 'application/json', 'Content-Type': 'application/json'
			}, body: JSON.stringify(appealForm)
		})
			.then(res => {
				createRequestAnswer(res.ok);
			})
			.catch(err => {
				createRequestAnswer(false);
				console.log("Error:" + err);
			})

	});

	nameInput.addEventListener("input", () => {
		manageCurrentTab();
	});

	surnameInput.addEventListener("input", () => {
		manageCurrentTab();
	});

	phoneInput.addEventListener("input", () => {
		manageCurrentTab();
	});

	typeOfHelpSelect.addEventListener("change", () => {
		manageCurrentTab();
	});

	typeOfConsultationSelect.addEventListener("change", () => {
		manageCurrentTab();
	});

	personalDataValidstionCheckbox.addEventListener("change", () => {
		manageCurrentTab();
	});

});
