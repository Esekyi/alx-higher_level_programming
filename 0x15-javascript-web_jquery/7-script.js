$(document).ready(function () {
  var url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.ajax({
    url: url,
    method: 'GET',
    success: function (data) {
      var characterName = data.name;

      $('#character').text(characterName);
    },
    error: function () {
      $('#character').text('Failed to fetch character data.');
    }
  });
});
