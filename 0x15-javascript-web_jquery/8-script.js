$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (DATA) {
      $.each(DATA.results, function (i, Movie) {
        $('UL#list_movies').append('<li>' + Movie.title + '</li>');
      });
    }
  });
});
