//dropdown menu js for role and company
dropdown.addEventListener('change', () => {
    const selectedValue = dropdown.value;

    fetch(`/${selectedValue}`)
    .then(response => response.text())
    .then(data => {
        document.getElementById('result').innerHTML = data;
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('roleDropdown').addEventListener('change', () => {
    const selectedValue = document.getElementById('roleDropdown').value;

    fetch(`/${selectedValue}`)
    .then(response => response.text())
    .then(data => {
        document.getElementById('result').innerHTML = data;
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('companyDropdown').addEventListener('change', () => {
    const selectedValue = document.getElementById('companyDropdown').value;

    fetch(`/${selectedValue}`)
    .then(response => response.text())
    .then(data => {
        document.getElementById('result').innerHTML = data;
    })
    .catch(error => console.error('Error:', error));
});
