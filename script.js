#script.js
function showContact(contactId) {
  const contacts = ['brother', 'friend1', 'friend2'];
  contacts.forEach(id => {
    document.getElementById(id).style.display = (id === contactId) ? 'block' : 'none';
  });
}

document.querySelectorAll('.button').forEach(button => {
         button.addEventListener('click', (event) => {
             event.preventDefault();
             const buttonText = event.target.innerText;
             alert(`You clicked on: ${buttonText}`);
         });
     });