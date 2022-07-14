const btnSubmit = document.getElementById('submitForm');
const nameInput = document.getElementById('nameFormInput');
const phoneInput = document.getElementById('phoneFormInput');
const emailInput = document.getElementById('mailFormInput');
const messageInput = document.getElementById('messageFormInput');
const checkBox = document.getElementById('checkboxForm');

document.addEventListener('DOMContentLoaded', () => {
    IMask(phoneInput, {mask: '+{7}(000)000-00-00'});
});

function isValid() {
    console.log(phoneInput.value.length);
    if (nameInput.value.length > 0 && (phoneInput.value.length > 0 && phoneInput.value.length === 16)
        && (emailInput.value.length > 0 && emailInput.value.toLowerCase().match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/))
        && checkBox.checked) {
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
    btnSubmit.addEventListener('click', function () {
        //    here will be form sending dont forget about trim() for inputs
        nameInput.value = '';
        phoneInput.value = '';
        emailInput.value = '';
        messageInput.value = '';
    });
})();

