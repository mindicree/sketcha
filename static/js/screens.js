// screen initializations
let game_screen_container = document.querySelector('#game_screen_container')
// loading
let screen_loading = document.querySelector('#screen_loading')
// home screens
let screen_home_new = document.querySelector('#screen_home_new')
let screen_new_player = document.querySelector('#screen_new_player')
let screen_home_continue = document.querySelector('#screen_home_continue')
let screen_home_panel = document.querySelector('#screen_home_panel')
let screen_home_options = document.querySelector('#screen_home_options')
let screen_home_credits = document.querySelector('#screen_home_credits')
let screen_home_tutorial = document.querySelector('#screen_home_tutorial')
// gacha char screens
let screen_gacha_char_buy = document.querySelector('#screen_gacha_char_buy')
let screen_gacha_char_open = document.querySelector('#screen_gacha_char_open')
let screen_gacha_char_result = document.querySelector('#screen_gacha_char_result')
// gacha item screens
let screen_gacha_item_buy = document.querySelector('#screen_gacha_item_buy')
let screen_gacha_item_open = document.querySelector('#screen_gacha_item_open')
let screen_gacha_item_result = document.querySelector('#screen_gacha_item_result')
// character screens
let screen_char_list = document.querySelector('#screen_char_list')
let screen_char_select = document.querySelector('#screen_char_select')
let screen_char_equip = document.querySelector('#screen_char_equip')
// item screens
let screen_item_list = document.querySelector('#screen_item_list')
let screen_item_select = document.querySelector('#screen_item_select')
let screen_item_equip = document.querySelector('#screen_item_equip')
// battle screens
let screen_battle_team = document.querySelector('#screen_battle_team')
let screen_battle_select = document.querySelector('#screen_battle_select')
let screen_battle_fight = document.querySelector('#screen_battle_fight')
let screen_battle_finish = document.querySelector('#screen_battle_finish')

// transition function
function transition_screen(old_screen, new_screen) {
    old_screen.classList.add('inactive_screen')
    new_screen.classList.remove('inactive_screen')
    new_screen.classList.add('z-50')
    new_screen.classList.add('active_screen')
    old_screen.classList.remove('active_screen')
    old_screen.classList.remove('z-50')
}

// toggle loading icons
function toggle_loading() {
    document.querySelector('#loading_icon').classList.toggle('hidden')
}