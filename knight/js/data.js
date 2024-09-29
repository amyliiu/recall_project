// function handleSubmit(event) {
//     event.preventDefault();
  
//     const data = new FormData(event.target);
  
//     const value = data.get('email');
  
//     console.log({ value });
//   }
  
//   const form = document.querySelector('form');
//   form.addEventListener('submit', handleSubmit);

// document.addEventListener('DOMContentLoaded', 
export function handleSubmit() {
const form = document.getElementById('myForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevents the default form submission

        const state = document.getElementById('state').value;
        const email = document.getElementById('email').value;

        console.log('Email:', email);
        console.log('State:', state);
        
        // You can add further processing here, like sending data to a server
    });
};

// module.exports = { handleSubmit };
