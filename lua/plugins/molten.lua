return {
  "benlubas/molten-nvim",
  version = "^1.0.0", -- use version <2.0.0 to avoid breaking changes
  build = ":UpdateRemotePlugins",
  init = function()
    -- this is an example, not a default. Please see the readme for more configuration options
    vim.g.molten_output_win_max_height = 12

    -- "open_then_enter" | "open_and_enter" | "no_open"
    vim.g.molten_enter_output_behavior = "no_open"
    vim.g.molten_auto_open_output = false
    vim.g.molten_virt_text_output = true
    -- vim.g.molten_output_win_border = "-"
    vim.g.molten_virt_text_max_lines = 30
  end,
}
