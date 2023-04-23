function load_panel(reload=true) {
    toggle_loading()
    let curr_player = get_player_from_local()
    if (!reload) {
        update_panel_ui()
        toggle_loading()
        transition(screen_home_panel)
        return
    }
    fetch(base_url(`/get-player-data?id=${curr_player['id']}`))
    .then(res => res.json())
    .then(data => {
        player_data = data['data']
        update_panel_ui()
        toggle_loading()
        transition(screen_home_panel)
    })
    .catch(err => {
        console.log(err)
    })
}

function update_panel_ui() {

}