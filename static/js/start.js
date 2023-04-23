// TODO check localstorage for variable

// if present, load into current player variable

// else just load new home screen

// play music

setTimeout(() => {
    game_screen_container.classList.remove('opacity-0')
    update_ui()
    transition_screen(screen_loading, screen_home_new)
}, 2000);