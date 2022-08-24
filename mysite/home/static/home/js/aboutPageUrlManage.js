document.addEventListener("DOMContentLoaded", () => {
	console.log(window.location.hash)

	if (window.location.hash === "#help-tab") {
		console.log("help")
		document.getElementById("help-tab").click();
	}
});
