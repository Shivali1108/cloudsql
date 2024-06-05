document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    let value1 = document.getElementById('value1').value;
    let value2 = document.getElementById('value2').value;

    if (validateForm(value1, value2)) {
        console.log('Form submitted with values:', value1, value2);
        // Further form submission logic here
    }
});

function validateForm(value1, value2) {
    if (!value1 || !value2) {
        alert('Both fields are required!');
        return false;
    }
    return true;
}

