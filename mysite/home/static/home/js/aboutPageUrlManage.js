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
		case "#help-tab": document.getElementsByClassName("help-tab")[0].click(); break;
		case "#docs-tab": document.getElementsByClassName("docs-tab")[0].click(); break;
		case "#requisites-tab": document.getElementsByClassName("requisites-tab")[0].click(); break;
		case "#feedbacks-tab": document.getElementsByClassName("feedbacks-tab")[0].click(); break;
		default: {
			document.getElementsByClassName("about-tab")[0].click()
		}
	}

	document.getElementsByClassName("help-tab")[0].addEventListener('click', () => {
		location.hash = '#help-tab'
	})
	document.getElementsByClassName("docs-tab")[0].addEventListener('click', () => {
		location.hash = '#docs-tab'
	})
	document.getElementsByClassName("requisites-tab")[0].addEventListener('click', () => {
		location.hash = '#requisites-tab'
	})
	document.getElementsByClassName("feedbacks-tab")[0].addEventListener('click', () => {
		location.hash = '#requisites-tab'
	})
	document.getElementsByClassName("about-tab")[0].addEventListener('click', () => {
		location.hash = 'about-tab'
	})


	window.onhashchange = () => {
		switch (window.location.hash) {
			case "#help-tab": document.getElementsByClassName("help-tab")[0].click(); break;
			case "#docs-tab": document.getElementsByClassName("docs-tab")[0].click(); break;
			case "#requisites-tab": document.getElementsByClassName("requisites-tab")[0].click(); break;
			case "#feedbacks-tab": document.getElementsByClassName("feedbacks-tab")[0].click(); break;
			default: {
				document.getElementsByClassName("about-tab")[0].click()
			}
		}
	}
});
