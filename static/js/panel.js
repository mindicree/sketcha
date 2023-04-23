function load_panel() {
    toggle_loading()
    let curr_player = get_player_from_local()
    fetch(base_url(`/get-player-data?id=${curr_player['id']}`))
    .then(res => res.json())
    .then(data => {
        toggle_loading()
        console.log(data)
    })
    .catch(err => {
        console.log(err)
    })
}