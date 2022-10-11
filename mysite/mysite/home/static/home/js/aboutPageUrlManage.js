document.addEventListener("DOMContentLoaded", () => {
	// console.log(window.location.hash)

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
