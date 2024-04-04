$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (DATA) {
      $('DIV#hello').append(DATA.hello);
    }
  });
});
