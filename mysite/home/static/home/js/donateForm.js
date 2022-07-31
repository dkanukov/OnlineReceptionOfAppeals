const btnSubmit = document.getElementById('submitForm');
const nameInput = document.getElementById('nameFormInput');
const phoneInput = document.getElementById('phoneFormInput');
const emailInput = document.getElementById('mailFormInput');
const messageInput = document.getElementById('messageFormInput');
const checkBox = document.getElementById('checkboxForm');

function isValid() {
    if (nameInput.value.length > 0 && phoneInput.value.length > 0 && emailInput.value.length > 0 && checkBox.checked) {
        btnSubmit.disabled = false;
    } else {
        btnSubmit.disabled = true;
    }
}

(function () {
    nameInput.addEventListener('input', function () {
        isValid();
    });
    phoneInput.addEventListener('input', function (e) {
        isValid();
    });
    emailInput.addEventListener('input', function () {
        isValid();
    });
    checkBox.addEventListener('change', function () {
        isValid();
    });
})();

