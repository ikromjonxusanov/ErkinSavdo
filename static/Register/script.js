const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

// Prevent login and register buttons from throwing an error in codepen
const buttons = document.querySelectorAll('.form-container button')

buttons[0].addEventListener('click' , (e) => {
	e.preventDefault()
})
buttons[1].addEventListener('click' , (e) => {
	e.preventDefault()
})