/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme');

module.exports = {
  content: [
    "./templates/*.{html,js}"
  ],
  theme: {
    extend: {
      fontFamily: {
        gamer: ['"Press Start 2P"', ...defaultTheme.fontFamily.sans],
        koulen: ['"Koulen"', ...defaultTheme.fontFamily.sans],
        patrick: ['"Patrick Hand SC"', ...defaultTheme.fontFamily.sans],
        bowlby: ['"Bowlby One SC"', ...defaultTheme.fontFamily.sans],
        rubik: ['"Rubik Iso"', ...defaultTheme.fontFamily.sans],
        skranji: ['"Skranji"', ...defaultTheme.fontFamily.sans],
        expletus: ['"Expletus Sans"', ...defaultTheme.fontFamily.sans],
      }
    },
  },
  plugins: [],
}