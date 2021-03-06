var i = 0;
$(document).ready(function() {
  $(".add-step").click(function() {
    i++;
    $(".step-list").append('<li><textarea class="form-control" name = "' + i + '" rows="3" placeholder="Add Step" style="margin-top:10px;" required></textarea></li>');
    var x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText = x;
  });
});

$(document).on('change', ':file', function() {
  var input = $(this),
    numFiles = input.get(0).files ? input.get(0).files.length : 1,
    label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);

  document.getElementById('add-t-image').innerText = 'Change image';
  var img = document.getElementsByClassName('imagepreview');
  console.log(img);
  img[0].style.display = 'block';
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('#preview').attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]);
  }
}

$('input[type="file"]').change(function() {
  readURL(this);
});

$(document).ready(function() {
  var text_max = 500;
  $('#feedback').html(text_max + '/' + text_max);
  $('#commentarea').keyup(function() {
    document.getElementById('feedback').style.display = 'block';
    var text_length = $('#commentarea').val().length;
    var text_remaining = text_max - text_length;
    $('#feedback').html(text_remaining + '/' + text_max);
  });
});

$(".more").shorten({
	"showChars" : 150,
	"moreText"	: "more",
	"lessText"	: "less",
});
