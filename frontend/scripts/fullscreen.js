let fullscreen;
const fullscreenIcon = document.getElementById('fullscreen-icon');
const dashboard = document.getElementById('dashboard');

fullscreenIcon.addEventListener('click', function (e) {
	e.preventDefault();

	if (!fullscreen) {
		fullscreen = true;
		document.documentElement.requestFullscreen();
		dashboard.style.width = '100%';
		dashboard.style.height = '100%';
	} else {
		fullscreen = false;
		document.exitFullscreen();
		dashboard.style.width = '370px';
		dashboard.style.height = '260px';
	}
});
