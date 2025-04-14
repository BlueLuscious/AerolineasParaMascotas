tailwind.config = {
  theme: {
    extend: {
      colors: {
        tertiary: {
            whatsapp_green_tone: "#00bb2d",
        },
      },
      keyframes: {
        mini_bounce: {
          "0%, 100%": { transform: "translateY(-2.5%)", animationTimingFunction: "cubic-bezier(0.8,0,1,1)", },
          "50%": { transform: "translate(0)", animationTimingFunction: "cubic-bezier(0,0,0.2,1)", },
        },
      },
      animation: {
        mini_bounce: 'mini_bounce 1.5s ease-in-out infinite',
      },
    }
  }
}
