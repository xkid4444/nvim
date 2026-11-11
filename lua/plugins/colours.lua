-- Using Lazy
return {
  {
    "navarasu/onedark.nvim",
    priority = 1000, -- make sure to load this before all the other start plugins
    config = function()
      require("onedark").setup({
        style = "darker",
        transparent = true,
      })
      -- require("onedark").load()
    end,
  },
  {
    "scottmckendry/cyberdream.nvim",
    lazy = false,
    priority = 1000,
    config = function()
      require("cyberdream").setup({
        -- Variant: "default", "light", "muted", or "auto"
        variant = "default",
        -- Enable transparent background
        transparent = false,
        -- Saturation: 0 (greyscale) to 1 (full color)
        saturation = 1,
        -- Italic comments
        italic_comments = false,
        -- Clean look by hiding fillchars
        hide_fillchars = false,
        -- Modern borderless pickers (Telescope, Snacks, Fzf-lua)
        borderless_pickers = false,
        -- Terminal colors
        terminal_colors = true,

        -- NOTE: This function nullifies the `highlights` option
        overrides = function(colors)
            return {
              -- Python variables
              ["@variable.member.python"] = { fg = "#ffcfff"},
              ["@constant.python"] = { fg = "#ffcfff"},
            }
        end,
      })
      require("cyberdream").load()
    end,
  },
}
