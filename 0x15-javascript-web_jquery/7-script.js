// function that fetches the character name from this URL:
// https://swapi-api.alx-tools.com/api/people/5/?format=json
$(function () {
    $.ajax({
      url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
      type: 'GET',
      success: function (data) {
        $('#character').text(data.name);
      }
    });
  });