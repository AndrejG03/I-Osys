/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        ncrAccent: '#6c2bb5',
        offBlack: '#272829'
      }
    }
  },
  plugins: []
}
