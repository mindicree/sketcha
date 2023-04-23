let battle_data = {
    char: null,
    char_hp: null,
    enemy: null,
    enemy_hp: null,
    success: null
}

let player_fighter_sprite_1 = document.querySelector('#player_fighter_sprite_1')
let enemy_fighter_sprite_1 = document.querySelector('#enemy_fighter_sprite_1')
setInterval(() => {
    player_fighter_sprite_1.classList.toggle('opacity-0')
}, 450)
setInterval(() => {
    enemy_fighter_sprite_1.classList.toggle('opacity-0')
}, 550)

function prepare_for_battle() {
    update_battle_select_ui()
    transition(screen_battle_select)
}

function update_battle_select_ui() {
    let characters = player_data['char_data']
    let list_container = document.querySelector('#battle_select_char')
    list_container.innerHTML = ''
    characters.forEach((char, index) => {
        list_container.innerHTML += `
        <div data-char-id="${index}" onclick="go_to_battle_with(this)" class="grid grid-cols-6 w-full gap-4 m-auto drop-shadow-lg hover:bg-gray-500 transition duration-100 drop-shadow-lg">
            <img src="${char['sprite_idle_1']}" class="col-span-2 w-3/4 max-w-[100px] aspect-square m-auto">
            <div class="grid gap-1 col-span-4">
                <h4 class="text-lg font-bold font-patrick">${char['name']}</h4>
                <p class="font-patrick">Level: ${char['level']} | Love: ${char['love']}</p>
            </div>
        </div>
        `
    })
}

function go_to_battle_with(element) {
    toggle_loading()
    fetch(base_url('/get-random-enemy'))
    .then(res => res.json())
    .then(data => {
        battle_char = player_data['char_data'][element.getAttribute('data-char-id')]
        battle_data.char = battle_char
        battle_data.char_hp = battle_char.hp
        battle_data.enemy = data
        battle_data.enemy_hp = data.hp
        battle_data.success = get_chance_of_success()

        update_battle_field_ui()
        toggle_loading()
        transition(screen_battle_fight)
    })
    .catch(err => {
        alert(err)
        toggle_loading()
        load_panel()
    })
}

function update_battle_state() {

}

function update_battle_field_ui() {
    console.log(battle_data)
    document.querySelector('#player_fighter_sprite_1').src = battle_data.char.sprite_idle_1
    document.querySelector('#player_fighter_sprite_2').src = battle_data.char.sprite_idle_2
    document.querySelector('#enemy_fighter_sprite_1').src = battle_data.enemy.sprite_idle_1
    document.querySelector('#enemy_fighter_sprite_2').src = battle_data.enemy.sprite_idle_2
    document.querySelector('#player_fight_hp').innerHTML = battle_data.char.name
    document.querySelector('#enemy_fight_hp').innerHTML = battle_data.enemy.name
    document.querySelector('#view_chance_of_success').innerHTML = `${Math.floor((battle_data.success) * 100)}%`
}

function get_chance_of_success() {
    let player_total = battle_data.char.hp * (Math.random() * 2)
    let enemy_total = (battle_data.enemy.hp) * (Math.random() * 10)
    let chance = player_total/enemy_total
    return Math.min(.9, chance)
}

function fight() {
    toggle_loading()
    let won = Math.random() < battle_data.success
    if (won) {
        setupWin()
    } else {
        setupLose()
    }
}

function setupWin() {
    fetch(base_url('/char_win?player_id='+get_player_from_local()['id']+'&char_id='+battle_data.char.rowid), {method: 'POST'})
    .then(res => res.json())
    .then(data => {
        document.querySelector('#battle_result').innerHTML = 'You Won!'
        document.querySelector('#coin_result').innerHTML = `You earned 5 coins and earned 1 love for ${battle_data.char.name}.`
        toggle_loading()
        transition(screen_battle_finish)
    }) 
}

function setupLose() {
    fetch(base_url('/char_lose?player_id='+get_player_from_local()['id']), {method: 'POST'})
    .then(res => res.json())
    .then(data => {
        document.querySelector('#battle_result').innerHTML = 'You Lost!'
        document.querySelector('#coin_result').innerHTML = `You earned 1 coin`
        toggle_loading()
        transition(screen_battle_finish)
    })
}