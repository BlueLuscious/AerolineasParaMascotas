tailwind.config = {
  theme: {
    extend: {
      // Fonts
      fontFamily: {
        primary_font: ["Fira Sans", "sans-serif"],
        secondary_font: ["Archivo", "sans-serif"],
        parisienne_font: ["Parisienne", "cursive"],
      },
      // Colours
      colors: {
        primary: {
          red: "#dc2626",
          red_light: "#fee2e2",
          red_dark: "#991b1b",
          blue: "#2563eb",
          blue_extralight: "#eff6ff",
          blue_light: "#dbeafe",
          blue_dark: "#1e3a8a",
        },
        secondary: {
          grey: "#9ca3af",
          grey_light: "#f9fafb",
          grey_dark: "#1f2937",
        },
        tertiary: {
          whatsapp_green_tone: "#00bb2d",
        },
      },
      // Key Frames
      keyframes: {
        mini_bounce: {
          "0%, 100%": { transform: "translateY(-5%)", animationTimingFunction: "cubic-bezier(0.8,0,1,1)", },
          "50%": { transform: "translateY(5%)", animationTimingFunction: "cubic-bezier(0,0,0.2,1)", },
        },
      },
      // Animations
      animation: {
        mini_bounce_fast: "mini_bounce 1s ease-in-out infinite",
        mini_bounce_medium_fast: "mini_bounce 1.5s ease-in-out infinite",
        mini_bounce_medium: "mini_bounce 2s ease-in-out infinite",
        mini_bounce_medium_slow: "mini_bounce 2.5s ease-in-out infinite",
        mini_bounce_slow: "mini_bounce 3s ease-in-out infinite",
      },
    }
  }
}
