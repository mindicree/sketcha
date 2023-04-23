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
            set_welcome_text(data['data'])
            transition_screen(screen_new_player, screen_new_welcome)
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

function set_welcome_text(info) {
    let welcome_text = document.querySelector('#welcome-text')
    welcome_text.innerHTML = `Welcome to Sketcha, <strong>${info['name']}</strong>! We hope that you will enjoy the infinite loop of addiction that we will inevitably inflict onto your life. For reference, your full id is <strong>${info['name']}#${info['id']}</strong>. Use this for data recovery in case of failure. <br><br>Have fun!`
}

function save_player_to_local(player_json) {
    localStorage.setItem('player', JSON.stringify(player_json));
}

function get_player_from_local() {
    if (localStorage.getItem('player')) {
        return JSON.parse(localStorage.getItem('player'))
    }
    return null
}

function remove_player_from_local() {
    localStorage.removeItem('player')
}