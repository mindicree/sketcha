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
    console.log(player_data)
    let rand_char = player_data['char_data'][Math.floor(Math.random() * player_data['char_data'].length)]
    if (rand_char) {
        document.querySelector('#panel_animation_1').src = rand_char['sprite_idle_1']
        document.querySelector('#panel_animation_2').src = rand_char['sprite_idle_2']
    }  
    document.querySelector('#view_count_chars').innerHTML = player_data['char_data'].length
    document.querySelector('#view_count_items').innerHTML = player_data['item_data'].length
    document.querySelector('#view_count_coins').innerHTML = player_data['player_data']['coins']
    document.querySelector('#view_count_streak').innerHTML = player_data['player_data']['streak']
}