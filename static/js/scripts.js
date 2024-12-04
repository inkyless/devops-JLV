
const ImageUpload = document.getElementById('images');
const fileInput = document.querySelector("#output")
fileInput.style.display = "none";


ImageUpload.addEventListener('change', function() {
   const file = ImageUpload.files[0];

  const reader = new FileReader();

  reader.onload = function(e) {
    const imageDataUrl = e.target.result;

    const imagepreview = document.getElementById("image-preview")
    const submitButton = document.getElementById("submit")
    const submitBox = document.getElementById("submit-wrap")

    imagepreview.innerHTML="Image Preview"
    submitButton.style.display="block"
    submitBox.style.visibility = 'visible'
    submitButton.innerText="Submit to Check"
    fileInput.src = imageDataUrl;
    fileInput.style.display = "block";

  };

  reader.readAsDataURL(file);
});
