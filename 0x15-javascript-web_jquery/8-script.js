$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', data => {
     data.results.forEach(mov => {
     $("#list_movies").append(`<li>${mov.title}</li>`);
     });
});
