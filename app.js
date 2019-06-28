$('#serachimge').mousemove(() => {
	$('#serachimge').attr('src', 'icons/icons8-google-blog-search-64.png');
});
$('#serachimge').mouseout(function() {
	$('#serachimge').attr('src', 'icons/icons864.png');
});

$('#dolist').keyup((e) => {
	const li = document.createElement('li');

	if (e.keyCode == 13 && $('#dolist').val().trim() != '') {
		li.textContent = $('#dolist').val();
		$('.inputes').append(li);
		$('#dolist').val('');
	}
	li.addEventListener('dblclick', () => {
		li.remove(li);
	});
	li.addEventListener('click', () => {
		li.style.background = 'lightgreen';
	});
});
