$(document).ready(function () {
	var url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.ajax({
    url: url,
    method: 'GET',
    success: function (data) {
      var characterName = data.name;

      $('#hello').text(characterName);
    },
    error: function () {
      $('#character').text('Failed to fetch character data.');
    }
  });
});
