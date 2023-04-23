function create_new_player() {
    let name = document.querySelector('#input_new_player').value
    if (name.length < 2) {
        alert('Please enter a name longer than two characters.')
        return
    }
    toggle_loading()
    fetch(base_url(`/create-player?name=${name}`), {method: 'POST'})
    .then(res => res.json())
    .then((data) => {
        if (data['status'] === 'success') {
            save_player_to_local(data['data'])
            transition_screen(screen_new_player, screen_home_portal)
            toggle_loading()
            console.log(data)
        } else {
            alert(data['message'])
        }
    })
    .catch((err) => {
        console.log(err)
    })
}

function save_player_to_local(player_json) {
    localStorage.setItem('player', JSON.stringify(player_json));
}

function get_player_from_local() {
    return localStorage.getItem('player')
}

function remove_player_from_local() {
    localStorage.removeItem('player')
}