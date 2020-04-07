ads.forEach(element => {
    document.getElementById('example').innerHTML += "<h2>" + element.fields.name + "</h2>" + "<h2>" + element.fields.clicks + "</h2>";
});
