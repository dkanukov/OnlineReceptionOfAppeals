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

function manageCurrentTab() {
	const currentTab = document.querySelector(".tab-pane.active.show");
	if (currentTab) {
		submitBtn.disabled = !(nameInput.value.trim() !== "" && surnameInput.value.trim() !== "" && phoneInput.value.length === 16 && personalDataValidstionCheckbox.checked)
	}
}

document.addEventListener("DOMContentLoaded", () => {
	submitBtn.addEventListener("click", async (e) => {
		e.preventDefault();
		const appealForm = {
			data: 123
		}

		await fetch("http://127.0.0.1:8000/api/appeal", {
			method: "POST", headers: {
				'Accept': 'application/json', 'Content-Type': 'application/json'
			}, body: JSON.stringify(appealForm)
		})
			.then(res => {
				const modal = document.getElementsByClassName("modal-content");
				const modalBody = document.createElement("div");
				modalBody.classList.add("display-4", "text-success", "modal-body");
				modalBody.textContent = "Форма отправлена";
				modal[0].innerHTML = "";
				modal[0].append(modalBody);
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
