<script>
function myFunction() {
  var canvas = document.getElementById('myCanvas');
  var context = canvas.getContext('2d');
  var imageObj = new Image();

  imageObj.onload = function() {
    context.drawImage(imageObj, 320, 240);
  };
  imageObj.src = '/static/thewinner.jpg';
 }
</script>

