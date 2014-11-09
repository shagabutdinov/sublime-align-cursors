# Sublime AlignCursors plugin

Align multicursors at one line. Useful when making tables in markdown-files.


### Demo

![Demo](https://github.com/shagabutdinov/sublime-enhanced-demos/raw/master/align_cursors.gif "Demo")


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

Align cursors example:

  ```
  # before
  | Open project folder | f10 [cursor]| OpenPath: Open project folder |
  | Open file folder    | ctrl+f10 [cursor]| OpenPath: Open file folder    |

  # after
  | Open project folder | f10      [cursor]| OpenPath: Open project folder |
  | Open file folder    | ctrl+f10 [cursor]| OpenPath: Open file folder    |
  ```


### Usage

Add several cursors to view. Hit keyboard shortcut to align cursors.


### Commands

| Description   | Keyboard shortcuts | Command palette     |
|---------------|--------------------|---------------------|
| Align cursors | ctrl+u, ctrl+q     | AlignCursors: Align |


### Dependencies

None