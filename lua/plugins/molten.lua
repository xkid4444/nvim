return {
  "benlubas/molten-nvim",
  version = "^1.0.0", -- use version <2.0.0 to avoid breaking changes
  build = ":UpdateRemotePlugins",
  init = function()
    -- this is an example, not a default. Please see the readme for more configuration options
    vim.g.molten_output_win_max_height = 12

    -- "open_then_enter" | "open_and_enter" | "no_open"
    vim.g.molten_enter_output_behavior = "open_and_enter"
    vim.g.molten_auto_open_output = false
    vim.g.molten_virt_text_output = true
    -- vim.g.molten_wrap_output = true
    vim.g.molten_virt_text_max_lines = 50
    vim.g.molten_virt_text_truncate = "top"
    -- vim.g.molten_floating_window_focus = "bottom"
    -- vim.g.molten_output_win_border = "-"
    if vim.env.TERM_PROGRAM == "WezTerm" then
      vim.g.molten_image_provider = "wezterm"
    end
  end,
}
