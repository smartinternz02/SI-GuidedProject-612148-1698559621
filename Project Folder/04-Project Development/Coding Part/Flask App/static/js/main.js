function showPreview() {
    var fileInput = document.getElementById('imageInput');
    var recognizeButton = document.getElementById('recognizeButton');
    var imagePreview = document.getElementById('imagePreview');

    if (fileInput.files.length > 0) {
        recognizeButton.style.display = 'block';

        var reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.src = e.target.result;
        };

        reader.readAsDataURL(fileInput.files[0]);
    } else {
        recognizeButton.style.display = 'none';
        imagePreview.src = ''; // Clear the preview if no file is selected
    }
}