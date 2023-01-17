const btnSendDonate = document.getElementById('btnSendDonate')
const inputSendDonate = document.getElementById('inputSendDonate')
document.addEventListener("DOMContentLoaded", () => {
	if (inputSendDonate.value === '') {
		btnSendDonate.disabled = true;
	}

	inputSendDonate.addEventListener('input', () => {
		btnSendDonate.disabled = inputSendDonate.value === '';
	})

	btnSendDonate.addEventListener('click', async () => {
		const ans = await fetch(`/api/pay?value=${inputSendDonate.value}`, {
			mode: 'no-cors',
			method: 'GET',
		});
		const res = await ans.json()
		window.location.href = res.redirect_url
	})

	switch (window.location.hash) {
		case "#help-tab": document.getElementById("help-tab").click(); break;
		case "#docs-tab": document.getElementById("docs-tab").click(); break;
		case "#requisites-tab": document.getElementById("requisites-tab").click(); break;
		case "#feedbacks-tab": document.getElementById("feedbacks-tab").click(); break;
		default: document.getElementById("about-tab").click();
	}

	window.onhashchange = () => {
		switch (window.location.hash) {
			case "#help-tab": document.getElementById("help-tab").click(); break;
			case "#docs-tab": document.getElementById("docs-tab").click(); break;
			case "#requisites-tab": document.getElementById("requisites-tab").click(); break;
			case "#feedbacks-tab": document.getElementById("feedbacks-tab").click(); break;
			default: document.getElementById("about-tab").click();
		}
	}
});
