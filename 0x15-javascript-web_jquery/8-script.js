$(document).ready(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
        if (textStatus === 'success'){
            for (const result of data.results) {
                $('#list_movies').append(`<li>${result.title}</li>`);
            }
        } 
    });
});
