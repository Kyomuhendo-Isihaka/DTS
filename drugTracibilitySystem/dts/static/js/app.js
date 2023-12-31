document.addEventListener('DOMContetLoaded', () => {
    const selectDrop = document.querySelector('#countries');
    fetch('https://restcountries.eu/rest/v2/all').then(res => {
        return res.json();

    }).then(data => {
        let output = "";
        data.forEach(country => {
            output += `<option value="${country.name}">${country.name}</option>`;
        })
        selectDrop.innerHTML=output;
    }).catch(err => {
        console.log(err);
    })
});