function create_new_player() {
    let name = document.querySelector('#input_new_player').value
    if (name.length < 2) {
        alert('Please enter a name longer than two characters.')
        return
    }
    toggle_loading()
}