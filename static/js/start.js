setTimeout(() => {
    // TODO check localstorage for variable
    if (player = get_player_from_local()) {
        set_bl_player_text()
        transition_screen(screen_loading, screen_home_continue)
    } else {
        transition_screen(screen_loading, screen_home_new)
    }
    game_screen_container.classList.remove('opacity-0')
}, 1000);