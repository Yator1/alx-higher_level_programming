$(function () {
    $.ajax({
      url: 'https://swapi-api.hbtn.io/api/films/?format=json',
      type: 'GET',
      success: function (films) {
        $.each(films.results, function (i, film) {
          $('#list_movies').append('<li>' + film.title + '</li>');
        });
      }
    });
  });