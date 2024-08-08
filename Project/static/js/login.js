console.log("register is working");

const emailField = document.querySelector('#emailField');
const emailFeedback = document.querySelector('#emailFeedback');
const showPasswordToggle = document.querySelector('#showPasswordToggle');
const passwordField = document.querySelector('#passwordField');


const handleToggleInput = (e) => {
    if(showPasswordToggle.textContent === 'Show password'){
        showPasswordToggle.textContent='Hide password';
        passwordField.setAttribute("type", "text");
    }
    else{
        showPasswordToggle.textContent='Show password';
        passwordField.setAttribute("type", "password");
    }
}
showPasswordToggle.addEventListener("click", handleToggleInput);


