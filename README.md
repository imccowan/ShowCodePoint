ShowCodePoint
=============

A Sublime Text 2/3 plugin to show the code point under the cursor like the 'ga' command in Vim.

By default, this plugin doesn't set up key bindings for you; we're all grownups here. Here's the JSON to set it up yourself. Replace the key with whatever you want and drop this in your User/Default.sublime-keymap file:
```json
{
  "keys": ["ctrl+a"],
  "command": "show_code_point"
}
```

To trigger this key binding with "ga" like in Vim while in the normal mode of the [Vintageous](https://github.com/guillermooo/Vintageous) plugin, you must instead use the following to avoid interfering with other key bindings starting with "g":
```json
{
  "keys": ["a"],
  "command": "show_code_point",
  "context": [{"key": "setting.command_mode"},
              {"key": "vi_in_key_namespace", "operand": "g"}]
}
```
