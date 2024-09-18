/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "media",
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      fontFamily: {
        sarabun: ["Sarabun", "sans-serif"],
        mitr: ["Mitr", "sans-serif"],
        prompt: ["Prompt", "sans-serif"],
      },
    },
  },
  plugins: [require('@tailwindcss/aspect-ratio')],
}
