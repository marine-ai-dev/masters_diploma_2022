
// UPLOAD AN IMAGE
var previewImage = function(event) {
	var preview = document.getElementById('my-image');
	preview.src = URL.createObjectURL(event.target.files[0]);
	preview.style.display = "block";
};


// DELETE A FLASH MESSAGE
function delete_flash_no_image_uploaded () {
// var close_button = document.getElementsByClassName("close_button");
	$('.flash-processing-image').remove();
}


// SHOW LOADING ICON (LOADING DIV)
function showLoadingIcon (){
	// $('#loading-div-icon').style.visibility = "visible";
	var elems = document.getElementsByClassName('loading-div-icon');
	for(var i=0; i<elems.length; i++)
		elems[i].style.display='flex';
}









