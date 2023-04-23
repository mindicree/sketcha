function base_url(endpoint="") {
    return window.location.origin + endpoint
}

function player_string(player) {
    return `${player['name']}#${player['id']}`
}